import unittest
from ..dialamoon import Moon
from ..terminal_ui import TerminalUi
from datetime import datetime
from time import sleep
import numpy
import copy

class TestMoon(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestMoon, self).__init__(*args, **kwargs)
		self.sm = Moon()

	def test_returns_error_for_datetime_format_issue(self):
		m = Moon()
		self.assertRaises(ValueError, m.set_moon_datetime, "190-01-01")

	def test_returns_helpful_error_for_datetime_range_issue(self):
		m = Moon()
		self.assertRaisesRegex(KeyError, r"Cannot find year .* in this version "\
				"of the package. This package can get moons for years .* -"\
				" .*. Please try a different year or check for an update "\
				"for this package.",
		 m.set_moon_datetime, "1900-01-01")

	def test_makes_a_moon_image_url(self):
		m = Moon()
		m.set_moon_datetime("2019-01-01")
		assert m.url == "https://svs.gsfc.nasa.gov/vis/a000000/a004400/"\
		"a004442/frames/730x730_1x1_30p/moon.0001.jpg"

	def test_makes_a_json_data_url(self):
		m = Moon()
		m.set_moon_datetime("2019-01-01")
		m.make_json_year_data_url()
		assert m.json_url == "https://svs.gsfc.nasa.gov/vis/a000000/a004400/a004442/mooninfo_2019.json"

	def test_gets_moon_image_as_numpy_array(self):
		m = Moon()
		m.set_moon_datetime("2019-01-01")
		m.request_moon_image()
		self.assertIs(type(m.image), numpy.ndarray)


if __name__ == '__main__':
	unittest.main()