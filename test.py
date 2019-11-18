
import DatasetOrganizer as do
import os

# From example 1 to example 2

parse_params = [('sub-(\d+)', 'sub'), ('ses-(\d+)', 'ses'), ()]
example_path = os.path.join(os.getcwd(), 'example1')
data = do.parse(example_path, parse_params)
new_path = os.path.join(os.getcwd(), 'example2')
do.write(new_path, [('sub-%s_ses-%s', 'sub', 'ses'), 'x.txt'], data)

# From example 2 to example 1

parse_params = [('sub-(\d+)_ses-(\d+)', 'sub', 'ses'), ()]
example_path = os.path.join(os.getcwd(), 'example2')
data = do.parse(example_path, parse_params)
new_path = os.path.join(os.getcwd(), 'example1')
do.write(new_path, [('sub-%s', 'sub'), ('ses-%s', 'ses'), 'x.txt'], data)
