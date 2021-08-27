def convert_rgb_to_hsl(red, green, blue, max_value=1.0, min_value=0.0):
	red = (red - min_value) / max_value
	green = (green - min_value) / max_value
	blue = (blue - min_value) / max_value

	red = min(1.0, max(0.0, red/max_value))
	green = min(1.0, max(0.0, green))
	blue = min(1.0, max(0.0, blue))

	maximum = max(red, green, blue)
	minimum = min(red, green, blue)

	chroma = maximum - minimum

	if chroma == 0:
		hue = 0
	else:
		if red == maximum:
			segment = (green - blue) / chroma
			shift = 360/60 if segment < 0 else 0/60

		elif green == maximum:
			segment = (blue - red) / chroma
			shift = 120/60

		else:
			segment = (red - green) / chroma
			shift = 240/60

		hue = segment + shift

