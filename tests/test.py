
import json, os, sys
prevdir = os.path.dirname(os.path.realpath(__file__))
os.chdir(os.path.join(prevdir, '..', 'dastr'))
sys.path.append(os.getcwd())
import dastr
os.chdir(prevdir)

# hardcoded translation
translation1 = {
	'ses': {
		'01': 'Pre',
		'02': 'Mid'
	},
	'sub': {
		'01': 'One',
		'02': 'Two'
	}
}
# translation from json
with open(os.path.join(os.getcwd(), 'translation.json'), 'r') as f:
	translation2 = json.load(f)
# they should be the same
assert translation1 == translation2
translation = translation1

## From example 1 to example 2

example_path = os.path.join(os.getcwd(), 'example-1')
# read files using hardcoded params
read_params = [('sub-(.+)', 'sub'), ('ses-(.+)', 'ses'), ()]
files1 = dastr.read(example_path, read_params, v=1)
# read files using json params
files2 = dastr.read(example_path,
	dastr.json_to_params(os.path.join(os.getcwd(), 'read_params_1to2.json')))
# they should be the same
assert files1 == files2
files = files1
# apply translation
translated = dastr.translate(files, translation, direction='forward')
# write using hardcoded params
write_params = [('sub-%s_ses-%s', 'sub', 'ses'), 'x.txt']
destinations1 = dastr.write(translated,
	os.path.join(os.getcwd(), 'example-2'),
	write_params,
	disp=False,
	key='n')
# write using json params
destinations2 = dastr.write(translated,
	os.path.join(os.getcwd(), 'example-2'),
	dastr.json_to_params(os.path.join(os.getcwd(), 'write_params_1to2.json')),
	disp=False,
	key='n')
assert destinations1 == destinations2

# From example 2 to example 1

example_path = os.path.join(os.getcwd(), 'example-2')
# read files using hardcoded params
read_params = [('sub-(.+)_ses-(.+)', 'sub', 'ses'), ()]
files1 = dastr.read(example_path, read_params)
# read files using json params
files2 = dastr.read(example_path,
	dastr.json_to_params(os.path.join(os.getcwd(), 'read_params_2to1.json')))
# they should be the same
assert files1 == files2
files = files1
# apply translation
translated = dastr.translate(files, translation, direction='forward')
# write using hardcoded params
write_params = [('sub-%s', 'sub'), ('ses-%s', 'ses'), 'x.txt']
destinations1 = dastr.write(translated,
	os.path.join(os.getcwd(), 'example-1'),
	write_params,
	disp=False,
	key='n')
# write using json params
destinations2 = dastr.write(translated,
	os.path.join(os.getcwd(), 'example-1'),
	dastr.json_to_params(os.path.join(os.getcwd(), 'write_params_2to1.json')),
	disp=False,
	key='n')
assert destinations1 == destinations2

print('Passed all tests!')