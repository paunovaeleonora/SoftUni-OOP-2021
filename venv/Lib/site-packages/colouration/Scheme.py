from .colour_schemes import colour_schemes
from .Colour import Colour, DEFAULT_INCREASE_RATIO


DEFAULT_SCHEME_NAME = 'pastel19'

ADDITIONAL_SCHEMES = {
	'pensieve': ['#fbb4ae', '#ccebc5', '#decbe4', '#fed9a6', '#fff2ae', '#e5d8bd', '#fddaec'],
	'pensieve2': [
		'#8dd3c7', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#bc80bd', '#ccebc5', '#ffed6f'
	]
}


class Scheme:
	def __init__(self, colours=None, name=DEFAULT_SCHEME_NAME, normalize_lightness=0.5):
		if colours is None and name.lower() in ADDITIONAL_SCHEMES:
			colours = [Colour(hexadecimal=hex) for hex in ADDITIONAL_SCHEMES[name]]
		else:
			colours = colours or [Colour(hexadecimal=hex) for hex in colour_schemes[name.lower()]]

		if normalize_lightness is not None:
			mean_lightness = sum([colour.lightness for colour in colours]) / len(colours)
			mean_lightness = mean_lightness + (1 - mean_lightness) * normalize_lightness
			for colour in colours:
				colour.lightness = mean_lightness

		self._colours = {}
		self._colour_usages = {}
		self._usage_logs = {}
		self._set_colours(colours)
		self._name = name

	def _set_colours(self, colours):
		for colour_id, colour in enumerate(colours):
			try:
				colour_original_id = colour.id
			except AttributeError:
				colour_original_id = None
			self._colours[colour_id] = Colour(obj=colour, id=colour_original_id or colour_id, scheme=self)
			if colour_id not in self._colour_usages:
				self._colour_usages[colour_id] = 0
			self._usage_logs[colour_id] = []

	def __getstate__(self):
		return {
			'colours': [colour.__getstate__() for colour in self.colours],
			'colour_usages': self._colour_usages,
			'usage_logs': self._usage_logs,
			'name': self._name
		}

	def __setstate__(self, state):
		self._colour_usages = state['colour_usages']
		self._usage_logs = state['usage_logs']
		self._name = state['name']
		self._set_colours(colours=[Colour._from_state(colour_state) for colour_state in state['colours']])

	@property
	def num_colours(self):
		return len(self.colours)

	def pick_by_index(self, index):
		"""
		:rtype index: int
		:rtype: Colour
		"""
		return self._colours[index % self.num_colours]

	@property
	def colours_in_order_of_usage(self):
		return sorted(self.colours, key=lambda x: (x.usage, x.id))

	@property
	def least_used_colour(self):
		return self.colours_in_order_of_usage[0]

	@property
	def logs(self):
		return [
			{'id': colour.id, 'colour': colour, 'usage': colour.usage, 'logs': colour.logs}
			for colour in self._colours.values()
		]

	def use(self, colour, log=None):
		self._colour_usages[colour.id] += 1
		if log is not None:
			self._usage_logs[colour.id].append(log)

	def get_usage(self, colour):
		"""
		:type colour: Colour
		:rtype: int
		"""
		return self._colour_usages[colour.id]

	def copy(self):
		return self.__class__(colours=[colour.copy() for colour in self.colours], name=self._name)

	@property
	def _max_name_length(self):
		return max([len(colour.name) for colour in self.colours]) + 2

	@property
	def colours(self):
		"""
		:rtype: list[Colour]
		"""
		if any([c is None for c in self._colours]):
			for c in self._colours:
				print(c)
			raise TypeError('colour is None!')
		return [self._colours[i] for i in range(len(self._colours))]

	def display(self, main_colour='background'):
		for colour in self.colours:
			name = colour.name.ljust(self._max_name_length)
			hue = str(round(colour.hue, 3)).ljust(5, '0')
			sat = str(round(colour.saturation, 3)).ljust(5, '0')
			lig = str(round(colour.lightness, 3)).ljust(5, '0')
			string = f'  h:{hue} s:{sat} l:{lig} '
			string = string.rjust(25)
			colour.display(
				string=' ' + name + string,
				length=self._max_name_length + 26,
				main_colour=main_colour
			)

	def adjust(self, hue=None, saturation=None, lightness=None):
		new_colours = []
		for colour in self.colours:
			colour = colour.copy()
			if hue is not None:
				colour.hue = hue
			if saturation is not None:
				colour.saturation = saturation
			if lightness is not None:
				colour.lightness = lightness
			new_colours.append(colour)
		return self.__class__(colours=new_colours)

	def increase(self, hue=0, saturation=0, lightness=0):
		new_colours = []
		for colour in self.colours:
			colour = colour.copy()
			colour.hue += hue
			colour.saturation += saturation
			colour.lightness += lightness
			new_colours.append(colour)
		return self.__class__(colours=new_colours)

	def invert(self):
		"""
		:rtype: Scheme
		"""
		return self.__class__(colours=[~colour for colour in self.colours])

	def __invert__(self):
		"""
		:rtype: Scheme
		"""
		return self.invert()

	def darken(self, ratio=0.5):
		"""
		:rtype: Scheme
		"""
		return self.__class__(colours=[colour.darken(ratio=ratio) for colour in self.colours])

	def lighten(self, ratio=0.5):
		"""
		:rtype: Scheme
		"""
		return self.__class__(colours=[colour.lighten(ratio=ratio) for colour in self.colours])

	brighten = lighten

	def darken_or_lighten(self, ratio=DEFAULT_INCREASE_RATIO):
		"""
		:rtype: Scheme
		"""
		return self.__class__(colours=[colour.darken_or_lighten(ratio=ratio) for colour in self.colours])

	@property
	def blacken_or_whiten(self):
		"""
		:rtype: Scheme
		"""
		return self.__class__(colours=[colour.blacken_or_whiten for colour in self.colours])

	@property
	def farthest_gray(self):
		"""
		:rtype: Scheme
		"""
		return self.__class__(colours=[colour.farthest_gray for colour in self.colours])

	@property
	def nearest_gray(self):
		"""
		:rtype: Scheme
		"""
		return self.__class__(colours=[colour.nearest_gray for colour in self.colours])

	@property
	def nearest_red(self):
		"""
		:rtype: Scheme
		"""
		return self.__class__(colours=[colour.nearest_red for colour in self.colours])

	@property
	def nearest_green(self):
		"""
		:rtype: Scheme
		"""
		return self.__class__(colours=[colour.nearest_green for colour in self.colours])

	@property
	def nearest_blue(self):
		"""
		:rtype: Scheme
		"""
		return self.__class__(colours=[colour.nearest_blue for colour in self.colours])
