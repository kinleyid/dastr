
import os, dastr

translation = {
	'ses': {
		'01': 'Pre',
		'02': 'Mid'
	},
	'sub': {
		'01': 'One',
		'02': 'Two'
	}
}

# From example 1 to example 2

parse_params = [('sub-(\d+)', 'sub'), ('ses-(\d+)', 'ses'), ()]
parse_params = [('sub-(.+)', 'sub'), ('ses-(.+)', 'ses'), ()]
example_path = os.path.join(os.getcwd(), 'example1')
data = do.parse(example_path, parse_params)
files = dt.read(example_path, parse_params)
files = dt.translate(files, translation, direction='forward')
new_path = os.path.join(os.getcwd(), 'example2')
do.write(new_path, [('sub-%s_ses-%s', 'sub', 'ses'), 'x.txt'], data)
dt.write(files, new_path, [('sub-%s_ses-%s', 'sub', 'ses'), 'x.txt'], print_only=True)
# dt.write(new_path, [('sub-%s_ses-%s', 'sub', 'ses'), 'x.txt'], files)

# From example 2 to example 1

parse_params = [('sub-(\d+)_ses-(\d+)', 'sub', 'ses'), ()]
parse_params = [('sub-(.+)_ses-(.+)', 'sub', 'ses'), ()]
example_path = os.path.join(os.getcwd(), 'example2')
data = do.parse(example_path, parse_params)
files = dt.read(example_path, parse_params)
files = dt.translate(files, translation, direction='backward')
new_path = os.path.join(os.getcwd(), 'example1')
do.write(new_path, [('sub-%s', 'sub'), ('ses-%s', 'ses'), 'x.txt'], data)
dt.write(files, new_path, [('sub-%s', 'sub'), ('ses-%s', 'ses'), 'x.txt'], print_only=True)
# dt.write(files, new_path, [('sub-%s', 'sub'), ('ses-%s', 'ses'), 'x.txt'])