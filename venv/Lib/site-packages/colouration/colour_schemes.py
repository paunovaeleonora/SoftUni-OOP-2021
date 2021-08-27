import pickle
import os
my_path = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(my_path, 'data_files')
x11_path = os.path.join(data_dir, 'x11_colours.pickle')
svg_path = os.path.join(data_dir, 'svg_colours.pickle')
colour_schemes_path = os.path.join(data_dir, 'colour_schemes.pickle')

with open(file=x11_path, mode='rb') as x11_file:
	hexadecimal_to_x11 = pickle.load(file=x11_file)

with open(file=svg_path, mode='rb') as svg_file:
	hexadecimal_to_svg = pickle.load(file=svg_file)

hexadecimal_to_name = {}
name_to_hexadecimal = {}
for hexadecimal, name in hexadecimal_to_svg.items():
	if hexadecimal not in hexadecimal_to_name:
		hexadecimal_to_name[hexadecimal] = name
	if name not in name_to_hexadecimal:
		name_to_hexadecimal[name] = hexadecimal

for hexadecimal, name in hexadecimal_to_x11.items():
	if hexadecimal not in hexadecimal_to_name:
		hexadecimal_to_name[hexadecimal] = name
	if name not in name_to_hexadecimal:
		name_to_hexadecimal[name] = hexadecimal

with open(file=colour_schemes_path, mode='rb') as colour_schemes_file:
	colour_schemes = pickle.load(file=colour_schemes_file)
