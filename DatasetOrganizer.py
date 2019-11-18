
import re, os, shutil

def parse(path, params, master_dict={}):
	all_entities = [] # That which will be returned
	curr_param = params[0]
	if type(curr_param) == str: # We're just going down a level in the file hierarchy
		all_entities += parse(os.path.join(path, curr_param), params[1:], master_dict=master_dict)
	else: # We're looping through every file in this level to collect attributes
		for curr_path_head in os.listdir(path):
			curr_dict = master_dict.copy()
			if len(curr_param) >= 2: # There are attributes to be added at this level of the hierarchy
				pattern = curr_param[0]
				curr_attrs = curr_param[1:]
				matches = re.findall(pattern, curr_path_head)[0]
				if type(matches) == str:
					matches = (matches,)
				for idx in range(len(matches)):
					curr_dict[curr_attrs[idx]] = matches[idx] # Add attributes
			curr_path = os.path.join(path, curr_path_head)
			if os.path.isdir(curr_path): # Recursion if we're currently on a folder
				all_entities += parse(curr_path, params[1:], master_dict=curr_dict)
			else: # Bottom of file hierarchy
				all_entities += [{
					'path': curr_path,
					'attrs': curr_dict.copy()
				}]
	return all_entities # List of dicts

def write(path, params, all_entities):
	for entity in all_entities:
		destination = ''
		for param in params:
			if type(param) == str:
				curr_path_head = param
			else: # Param is a tuple
				fmt = param[0]
				args = param[1:]
				curr_path_head = fmt % tuple([entity['attrs'][attr] for attr in args])
			destination = os.path.join(destination, curr_path_head)
		destination = os.path.join(path, destination)
		os.makedirs(os.path.dirname(destination), exist_ok=True)
		shutil.copy(entity['path'], destination)