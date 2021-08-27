from .Colour import Colour


class Gradient:
	def __init__(self, colour_1, colour_2, num_levels=10):
		colour_1 = Colour(colour_1)
		colour_2 = Colour(colour_2)

		self._colours = [
			(colour_1 * (num_levels - i - 1)).mix(colour_2 * i)
			for i in range(num_levels)
		]
		self._num_levels = num_levels

	def __repr__(self):
		return '\n'.join([repr(colour) for colour in self._colours])

	def colourize(self, string):
		"""
		:type string: str
		:rtype: str
		"""
		denominator = len(string) - 1
		return ''.join([
			self.get(ratio=numerator / denominator).colourize(string=character, background=None)
			for numerator, character in enumerate(string)
		])

	def get(self, ratio):
		"""
		:type ratio: float
		:return: Colour
		"""
		ratio = max(0.0, min(1.0, ratio))
		return self._colours[round(ratio * (self._num_levels - 1))]
