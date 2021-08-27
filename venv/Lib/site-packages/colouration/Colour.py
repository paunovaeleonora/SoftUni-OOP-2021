import colorsys
from .colour_schemes import hexadecimal_to_name, name_to_hexadecimal, colour_schemes
from .colourize import colourize

DEFAULT_INCREASE_RATIO = 0.2
DEFAULT_INCREASE_AMOUNT = 0.1


def scale(x, minimum, maximum):
	return (x - minimum) / (maximum - minimum)


def limit(x, minimum=0.0, maximum=1.0):
	return min(maximum, max(minimum, x))


class Colour:
	def __init__(
			self, obj=None, red=None, green=None, blue=None, hexadecimal=None,
			hue=None, saturation=None, lightness=None, value=None,
			min_value=0.0, max_value=1.0, name=None, id=None, scheme=None,
			weight=1.0
	):
		"""
		:type obj: str or NoneType or Colour
		:type red: float or NoneType
		:type green: float or NoneType
		:type blue: float or NoneType
		:type min_value: float
		:type max_value: float
		:type name: NoneType or str
		:type id: NoneType or int
		:type scheme: NoneType or .Scheme.Scheme
		"""
		self._id = id
		self._scheme = scheme
		self._weight = weight

		if obj is not None:
			if isinstance(obj, self.__class__):
				red, green, blue = obj.rgb

			elif isinstance(obj, str):
				if obj.startswith('#'):
					hexadecimal = obj

				else:
					name = obj

			elif isinstance(obj, (list, tuple)):
				red, green, blue = obj

			else:
				raise TypeError(f'obj should be one of str, Colour, tuple, or list but it is {type(obj)}')
			min_value = 0.0
			max_value = 1.0

		if red is not None and green is not None and blue is not None:
			pass

		elif hue is not None and saturation is not None and lightness is not None:
			red, green, blue = colorsys.hls_to_rgb(h=hue, l=lightness, s=saturation)
			min_value = 0.0
			max_value = 1.0

		elif hue is not None and saturation is not None and value is not None:
			red, green, blue = colorsys.hsv_to_rgb(h=hue, s=saturation, v=value)
			min_value = 0.0
			max_value = 1.0

		elif hexadecimal is not None:
			red, green, blue = self.convert_hexadecimal_to_rgb(hexadecimal=hexadecimal)
			min_value = 0.0
			max_value = 255.0

		elif name is not None:
			hexadecimal = name_to_hexadecimal[name.lower()]
			red, green, blue = self.convert_hexadecimal_to_rgb(hexadecimal=hexadecimal)
			min_value = 0.0
			max_value = 255.0

		else:
			raise ValueError(f'obj: "{obj}" not acceptable. It is of type "{type(obj)}"')

		self._red = scale(x=red, minimum=min_value, maximum=max_value)
		self._green = scale(x=green, minimum=min_value, maximum=max_value)
		self._blue = scale(x=blue, minimum=min_value, maximum=max_value)
		self._name = name

	@property
	def scheme(self):
		"""
		:rtype: .Scheme.Scheme or NoneType
		"""
		return self._scheme

	@property
	def id(self):
		"""
		:rtype: int or NoneTy[e
		"""
		return self._id

	def use(self, log=None):
		"""
		logs the usage of a colour
		:type log:
		:rtype: NoneType
		"""
		if self.scheme is not None:
			self.scheme.use(colour=self, log=log)

	@property
	def logs(self):
		if self.scheme is not None:
			return self.scheme._usage_logs[self.id]
		else:
			return None

	@property
	def usage(self):
		"""
		:rtype: int
		"""
		if self.scheme is not None:
			return self.scheme.get_usage(colour=self)
		else:
			return 0

	def __delete_identity(self):
		self._name = None
		self._id = None
		self._scheme = None

	@property
	def red(self):
		return limit(x=self._red)

	@red.setter
	def red(self, red):
		self.__delete_identity()
		self._red = red

	@property
	def green(self):
		return limit(x=self._green)

	@green.setter
	def green(self, green):
		self.__delete_identity()
		self._green = green

	@property
	def blue(self):
		return limit(x=self._blue)

	@blue.setter
	def blue(self, blue):
		self.__delete_identity()
		self._blue = blue

	def copy(self, keep_id=True):
		if keep_id:
			return self.__class__(
				red=self.red, green=self.green, blue=self.blue, name=self._name, id=self._id, scheme=self._scheme,
				weight=self._weight
			)
		else:
			return self.__class__(
				red=self.red, green=self.green, blue=self.blue, name=self._name, id=None, scheme=None,
				weight=self._weight
			)

	def __str__(self):
		return f'{self.name}: {self.hexadecimal}'

	def __repr__(self):
		return str(self)

	@staticmethod
	def _get_names():
		"""
		:rtype: dict[str,str]
		"""
		return hexadecimal_to_name

	@staticmethod
	def _get_hexadecimals():
		"""
		:rtype: dict[str, str]
		"""
		return name_to_hexadecimal

	@classmethod
	def get_standard_colours(cls):
		"""
		:rtype: list[Colour]
		"""
		return [cls(hexadecimal=hexadecimal, name=name) for hexadecimal, name in cls._get_names().items()]

	@staticmethod
	def get_schemes():
		"""
		:rtype: dict[str, list[str]]
		"""
		return colour_schemes.copy()

	@staticmethod
	def convert_hexadecimal_to_rgb(hexadecimal):
		if hexadecimal.startswith('#'):
			hexadecimal = hexadecimal[1:]

		if len(hexadecimal) == 3:
			hexadecimal = \
				hexadecimal[0] + hexadecimal[0] + \
				hexadecimal[1] + hexadecimal[1] + \
				hexadecimal[2] + hexadecimal[2]

		if len(hexadecimal) != 6:
			raise ValueError('The hex value should be 3 or 6 characters long!')

		red = int(f"0x{hexadecimal[0:2]}", 16)
		green = int(f"0x{hexadecimal[2:4]}", 16)
		blue = int(f"0x{hexadecimal[4:6]}", 16)
		return red, green, blue

	@property
	def name(self):
		if self._name is None:
			self._name = self.find_nearest(colours=self.get_standard_colours()).name
		return self._name

	@property
	def rgb(self):
		"""
		:rtype: tuple
		"""
		return self.red, self.green, self.blue

	@property
	def hsl(self):
		"""
		:rtype: tuple
		"""
		h, l, s = colorsys.rgb_to_hls(r=self.red, g=self.green, b=self.blue)
		return h, s, l

	@property
	def yig(self):
		"""
		:rtype: tuple
		"""
		return colorsys.rgb_to_yiq(r=self.red, g=self.green, b=self.blue)

	@property
	def hsv(self):
		"""
		:rtype: tuple
		"""
		return colorsys.rgb_to_hsv(r=self.red, g=self.green, b=self.blue)

	@property
	def hue(self):
		"""
		:rtype: float
		"""
		return self.hsl[0]

	@hue.setter
	def hue(self, hue):
		_, saturation, lightness = self.hsl
		hue = hue % 1.0
		self.__delete_identity()
		self.red, self._green, self._blue = colorsys.hls_to_rgb(h=hue, l=lightness, s=saturation)

	@property
	def saturation(self):
		"""
		:rtype: float
		"""
		return self.hsl[1]

	@saturation.setter
	def saturation(self, saturation):
		saturation = min(1.0, max(0, saturation))
		hue, _, lightness = self.hsl
		self._name = None
		self.red, self._green, self._blue = colorsys.hls_to_rgb(h=hue, l=lightness, s=saturation)

	def set_lightness_and_saturation(self, lightness, saturation):
		hue = self.hue
		self.red, self._green, self._blue = colorsys.hls_to_rgb(h=hue, l=lightness, s=saturation)

	@property
	def lightness(self):
		"""
		:rtype: float
		"""
		return self.hsl[2]

	@lightness.setter
	def lightness(self, lightness):
		lightness = min(1.0, max(0.0, lightness))
		hue, saturation, _ = self.hsl
		self._name = None
		self.red, self._green, self._blue = colorsys.hls_to_rgb(h=hue, l=lightness, s=saturation)

	@property
	def value(self):
		"""
		:rtype: float
		"""
		return self.hsv[2]

	@value.setter
	def value(self, value):
		value = min(1.0, max(0.0, value))
		hue, saturation, _ = self.hsv
		self._name = None
		self.red, self._green, self._blue = colorsys.hsv_to_rgb(h=hue, v=value, s=saturation)

	@property
	def hexadecimal(self):
		"""
		:rtype: str
		"""
		r = int(min(max(0.0, self.red * 255), 255))
		g = int(min(max(0.0, self.green * 255), 255))
		b = int(min(max(0.0, self.blue * 255), 255))
		return '#{:02x}{:02x}{:02x}'.format(r, g, b)

	def get_hexadecimal(self, opacity=None):
		"""
		:rtype: str
		"""
		if opacity is None:
			result = self.hexadecimal
		else:
			o = int(min(max(0.0, opacity * 255), 255))
			result = '{}{:02x}'.format(self.hexadecimal, o)
		return result

	def get_distance(self, other):
		"""
		:type other: Colour
		:rtype: float
		"""
		red2 = (self.red - other.red) ** 2
		green2 = (self.green - other.green) ** 2
		blue2 = (self.blue - other.blue) ** 2
		return (red2 + green2 + blue2) ** 0.5

	def find_nearest(self, colours):
		"""
		:type colours: list[Colour]
		:rtype:
		"""
		return sorted(colours, key=lambda x: self.get_distance(other=x))[0]

	def limit(self):
		self._red = self.red
		self._green = self.green
		self._blue = self.blue

	@classmethod
	def _tuple_as_colour(cls, other):
		if isinstance(other, (tuple, list)):
			if len(other) == 3:
				other = cls(red=other[0], green=other[1], blue=other[2])
		return other

	def __add__(self, other):
		"""
		:type other: Colour
		:rtype: Colour
		"""
		other = self._tuple_as_colour(other=other)

		if isinstance(other, Colour):
			return self.__class__(
				red=self._red + other._red,
				green=self._green + other._green,
				blue=self._blue + other._blue,
				weight=self._weight
			)
		else:
			return self.__class__(
				red=self._red + other, green=self._green + other, blue=self._blue + other, weight=self._weight
			)

	def __sub__(self, other):
		"""
		:type other: Colour
		:rtype: Colour
		"""
		other = self._tuple_as_colour(other=other)

		return self.__class__(
			red=self._red - other._red,
			green=self._green - other._green,
			blue=self._blue - other._blue
		)

	def __mul__(self, other):
		"""
		:type other: float or tuple or Colour
		:rtype: Colour
		"""
		if isinstance(other, (list, tuple)):
			other = self._tuple_as_colour(other=other)

		if isinstance(other, Colour):
			return self.__class__(
				red=self.red * other.red,
				green=self.green * other.green,
				blue=self.blue * other.blue
			)
		else:
			return self.__class__(red=self._red, green=self._green, blue=self._blue, weight=self._weight * other)

	def __neg__(self):
		"""
		:rtype: Colour
		"""

		return self.__class__(red=1 - self.red, green=1 - self.green, blue=1 - self.blue)

	def __invert__(self):
		return -self

	def __and__(self, other):
		if isinstance(other, (int, float)):
			if other > 1 or other < 0:
				raise ValueError('other cannot be negative or greated than one.')
		other = self._tuple_as_colour(other=other)

		return self * other

	def __or__(self, other):
		if isinstance(other, (int, float)):
			if other > 1 or other < 0:
				raise ValueError('other cannot be negative or greated than one.')
		other = self._tuple_as_colour(other=other)

		return self + other

	def __hashkey__(self):
		return self.__class__.__name__, self.__getstate__()

	def __getstate__(self):
		return self.red, self.green, self.blue, self._name, self._id, self._weight, None

	def __setstate__(self, state):
		self._red, self._green, self._blue, self._name, self._id, self._weight, self._scheme = state

	@classmethod
	def _from_state(cls, state):
		red, green, blue, name, id, weight, _ = state
		return cls(red=red, green=green, blue=blue, id=id, weight=weight)

	def colourize(self, string, background=None):
		if background == 'auto':
			background = self.farthest_gray

		if background is None:
			bg_red, bg_green, bg_blue = None, None, None
		else:
			if not isinstance(background, self.__class__):
				background = self.__class__(obj=background)
			bg_red, bg_green, bg_blue = background.rgb

		return colourize(
			string=string, red=self.red, green=self.green, blue=self.blue,
			bg_red=bg_red, bg_green=bg_green, bg_blue=bg_blue
		)

	def colourize_background(self, string, text_colour='auto'):
		if isinstance(text_colour, str) and text_colour == 'auto':
			text_colour = self.farthest_gray

		if text_colour is not None:
			bg_red, bg_green, bg_blue = text_colour.rgb
		else:
			bg_red, bg_green, bg_blue = self.__class__(hexadecimal='#808080').rgb

		return colourize(
			string=string, bg_red=self.red, bg_green=self.green, bg_blue=self.blue,
			red=bg_red, green=bg_green, blue=bg_blue
		)

	def print(self, string, secondary='auto', end=None, main_colour='background'):
		if main_colour == 'background':
			print(self.colourize_background(string=string, text_colour=secondary), end=end)
		else:
			print(self.colourize(string=string, background=secondary), end=end)

	def display(self, string=None, secondary='auto', end=None, main_colour='background', length=None):
		string = string or f' {self.name} '
		if length is not None:
			string = ('{:^' + str(int(length)) + '}').format(string)
		self.print(string=string, secondary=secondary, end=end, main_colour=main_colour)

	def mix_with_gray(self, gray_weight=None):
		"""
		:type gray_weight: NoneType or float
		:rtype: Colour
		"""
		gray = self.nearest_gray
		if gray_weight:
			gray._weight = gray_weight
		return self.mix(colours=gray)

	def darken(self, ratio=DEFAULT_INCREASE_RATIO, amount=None, keep_id=True):
		"""
		:type ratio: float or NoneType
		:type amount: float or NoneType
		:type keep_id: bool
		:rtype: Colour
		"""
		ratio = min(1.0, max(-1.0, ratio))
		darker = self.copy(keep_id=keep_id)

		if amount is None:
			amount = self.lightness ** 0.5 * ratio

		darker.lightness = darker.lightness - amount
		return darker

	def lighten(self, ratio=DEFAULT_INCREASE_RATIO, amount=None, keep_id=True):
		"""
		:type ratio: float or NoneType
		:type amount: float or NoneType
		:type keep_id: bool
		:rtype: Colour
		"""
		ratio = min(1.0, max(-1.0, ratio))
		lighter = self.copy(keep_id=keep_id)

		if amount is None:
			amount = (1 - self.lightness) * ratio

		lighter.lightness = lighter.lightness + amount
		return lighter

	def saturate(self, ratio=DEFAULT_INCREASE_RATIO, amount=None, keep_id=True):
		"""
		:type ratio: float or NoneType
		:type amount: float or NoneType
		:type keep_id: bool
		:rtype: Colour
		"""
		ratio = min(1.0, max(-1.0, ratio))
		more_saturated = self.copy(keep_id=keep_id)

		if amount is None:
			amount = (1 - self.saturation) * ratio

		more_saturated.saturation = more_saturated.saturation + amount
		return more_saturated

	def pale(self, ratio=DEFAULT_INCREASE_RATIO, amount=None, keep_id=True):
		"""
		:type ratio: float or NoneType
		:type amount: float or NoneType
		:type keep_id: bool
		:rtype: Colour
		"""
		ratio = min(1.0, max(-1.0, ratio))
		less_saturated = self.copy(keep_id=keep_id)

		if amount is None:
			amount = self.saturation * ratio

		less_saturated.saturation = less_saturated.saturation - amount
		return less_saturated

	def darken_or_lighten(self, ratio=DEFAULT_INCREASE_RATIO, amount=None, keep_id=True):
		"""
		:type ratio: float or NoneType
		:type amount: float or NoneType
		:type keep_id: bool
		:rtype: Colour
		"""
		if self.lightness <= 0.5:
			return self.lighten(ratio=ratio, amount=amount, keep_id=keep_id)
		else:
			return self.darken(ratio=ratio, amount=amount, keep_id=keep_id)

	def blacken_or_whiten(self):
		"""
		:rtype: Colour
		"""
		return self.farthest_gray

	brighten = lighten

	def increase_hue(self, amount=DEFAULT_INCREASE_AMOUNT, keep_id=False):
		"""
		:type amount: float
		:type keep_id: bool
		:type keep_id: bool
		:rtype: Colour
		"""
		changed = self.copy(keep_id=keep_id)
		changed.hue = changed.hue + amount
		return changed

	@property
	def farthest_gray(self):
		"""
		:rtype: Colour
		"""
		if self.lightness < 0.5:
			return self.__class__(hexadecimal='#FFFFFF', weight=self._weight)
		else:
			return self.__class__(hexadecimal='#000000', weight=self._weight)

	@property
	def nearest_gray(self, keep_id=False):
		"""
		:type keep_id: bool
		:rtype: Colour
		"""
		gray = self.copy(keep_id=keep_id)
		gray.saturation = 0
		return gray

	@property
	def nearest_red(self, keep_id=False):
		"""
		:type keep_id: bool
		:rtype: Colour
		"""
		red = self.copy(keep_id=keep_id)
		red.hue = 0
		return red

	@property
	def nearest_green(self, keep_id=False):
		"""
		:type keep_id: bool
		:rtype: Colour
		"""
		green = self.copy(keep_id=keep_id)
		green.hue = 1.0/3.0
		return green

	@property
	def nearest_blue(self, keep_id=False):
		"""
		:type keep_id: bool
		:rtype: Colour
		"""
		blue = self.copy(keep_id=keep_id)
		blue.hue = 2.0/3.0
		return blue

	def reverse_lightness(self, keep_id=True):
		"""
		:type keep_id: bool
		:rtype: Colour
		"""
		_reversed = self.copy(keep_id=keep_id)
		_reversed.lightness = 1 - _reversed.lightness
		return _reversed

	def invert(self):
		"""
		:rtype: Colour
		"""
		result = self.__class__(red=1 - self.red, green=1 - self.green, blue=1 - self.blue)
		return result

	def mix(self=None, colours=None):
		"""
		:type colours: NoneType or Colour or list[Colour]
		:rtype: Colour
		"""
		if colours is None or colours == []:
			return self.copy(keep_id=True)
		else:
			if isinstance(colours, Colour):
				colours = [colours]

		if self is not None:
			colours = [self] + colours

		red = green = blue = lightness = saturation = 0.0
		id = colours[0].id
		scheme = colours[0].scheme
		for colour in colours:
			red += colour.red * colour._weight
			green += colour.green * colour._weight
			blue += colour.blue * colour._weight
			#lightness += colour.lightness * colour._weight
			#saturation += colour.saturation * colour._weight
			if id != colour.id:
				id = None
				scheme = None

		total_weight = sum([colour._weight for colour in colours])
		red = red / total_weight
		green = green / total_weight
		blue = blue / total_weight
		#lightness = lightness / total_weight
		#saturation = saturation / total_weight
		if self is not None:
			result = self.__class__(
				red=red, green=green, blue=blue, min_value=0.0, max_value=1.0, id=id, scheme=scheme,
				weight=total_weight
			)
		else:
			result = Colour(
				red=red, green=green, blue=blue, min_value=0.0, max_value=1.0, id=id, scheme=scheme,
				weight=total_weight
			)

		#result.set_lightness_and_saturation(lightness=lightness, saturation=saturation)
		return result

	@property
	def weight(self):
		"""
		:rtype: float
		"""
		return self._weight

	@weight.setter
	def weight(self, weight):
		"""
		:type weight: float
		"""
		self._weight = weight

	def __eq__(self, other):
		if not isinstance(other, self.__class__):
			other = self.__class__(obj=other)
		return self.hexadecimal == other.hexadecimal

	def __hash__(self):
		return hash(self.hexadecimal)
