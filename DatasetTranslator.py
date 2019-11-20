
import os, re, shutil

def read(path, params, master_dict={}, disp=False, tab_level=0):
	if disp:
		head, tail = os.path.split(path)
		print(' '*tab_level + tail)
	all_files = [] # That which will be returned
	curr_param = params[0]
	if type(curr_param) == str: # We're just going down a level in the file hierarchy
		all_files += read(os.path.join(path, curr_param), params[1:], master_dict=master_dict, tab_level=tab_level+1, disp=disp)
	else: # We're looping through every file in this level to collect attributes
		for curr_path_head in os.listdir(path):
			curr_attrs = master_dict.copy()
			if len(curr_param) >= 2: # There are attributes to be added at this level of the hierarchy
				pattern_to_match = curr_param[0]
				attrs_to_read = curr_param[1:]
				matches = re.findall(pattern_to_match, curr_path_head)[0]
				if type(matches) == str:
					matches = (matches,)
				for idx in range(len(matches)):
					curr_attrs[attrs_to_read[idx]] = matches[idx] # Add attributes
			curr_path = os.path.join(path, curr_path_head)
			if os.path.isdir(curr_path): # Recursion if we're currently on a folder
				all_files += read(curr_path, params[1:], master_dict=curr_attrs, tab_level=tab_level+1, disp=disp)
			else: # Bottom of file hierarchy
				all_files += [{
					'path': curr_path,
					'attrs': curr_attrs.copy()
				}]
	return all_files # List of dicts

def translate(all_files, translation, direction='forward'):
	if direction != 'forward': # Swap values and keys
		translation = {attr: {new: old for old, new in entry.items()} for attr, entry in translation.items()}
	for attr in translation.keys():
		for fileidx in range(len(all_files)):
			curr_val = all_files[fileidx]['attrs'][attr]
			if curr_val in translation[attr]:
				new_val = translation[attr][curr_val]
				all_files[fileidx]['attrs'][attr] = new_val
	return all_files

def write(all_files, path, params, disp=False, move=True):
	destinations = []
	for file in all_files:
		curr_destination = ''
		for param in params:
			if type(param) == str: # We are adding a static name to the path
				curr_path_head = param
			else: # We are adding a formatted name to the path
				curr_path_head = param[0] % tuple(file['attrs'][attr] for attr in param[1:])
			curr_destination = os.path.join(curr_destination, curr_path_head)
		curr_destination = os.path.join(path, curr_destination)
		destinations.append(curr_destination)
		if disp: # Let the user double check that the destination paths are ok
			print(curr_destination)
		if move: # Commit to copying the files
			os.makedirs(os.path.dirname(curr_destination), exist_ok=True)
			shutil.copy(file['path'], curr_destination)
	return destinations