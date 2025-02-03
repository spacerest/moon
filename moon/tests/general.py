import unittest
from ..dialamoon import Moon
from ..terminal_ui import TerminalUi
from datetime import datetime
import numpy
import copy

class TestMoon(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestMoon, self).__init__(*args, **kwargs)
		self.sm = Moon()

	def test_returns_error_for_datetime_format_issue(self):
		m = Moon()
		self.assertRaises(ValueError, m.set_moon_datetime, "190-01-01")

	def test_returns_helpful_error_for_datetime_mismatch(self):
		m = Moon()
		self.assertRaisesRegex(ValueError, r"You asked for year .* but "\
				r"DialAMoon appears to have returned year .*.",
		 m.set_moon_phase, "1900-01-01")

	def test_makes_a_moon_image_url(self):
		m = Moon()
		m.set_moon_datetime(date="2019-01-01", hour=0)
		assert m.url == "https://svs.gsfc.nasa.gov/vis/a000000/a004400/"\
		"a004442/frames/730x730_1x1_30p/moon.0001.jpg"

	def test_gets_json_for_requested_datetime(self):
		m = Moon()
		m.set_moon_datetime(date="2019-01-01", hour=1)
		m.make_mooninfo_url()
		m.set_moon_datetime_info()
		assert m.moon_datetime_info["time"] == '2019-01-01T01:00'
		
	def test_gets_moon_image_as_numpy_array(self):
		m = Moon()
		m.set_moon_datetime("2019-01-01")
		m.request_moon_image()
		self.assertIs(type(m.image), numpy.ndarray)

	def test_takes_optional_hour_arg(self):
		m = Moon()
		m.set_moon_datetime(hour=1)
		assert m.requested_datetime.hour == 1

	def test_can_get_last_hour_of_nonleap_year(self):
		m = Moon()
		m.set_moon_datetime(date="2019-12-31", hour=23)
		m.request_moon_image()

		assert m.image_src == "https://svs.gsfc.nasa.gov/vis/a000000/a004400/a004442/"\
		"frames/730x730_1x1_30p/moon.8760.jpg"

	def test_can_get_last_hour_of_year(self):
		m = Moon()
		m.set_moon_datetime(date="2020-12-31", hour=23)
		m.request_moon_image()
		assert m.image_src == "https://svs.gsfc.nasa.gov/vis/a000000/a004700/a004768/"\
		"frames/730x730_1x1_30p/moon.8784.jpg"

	def test_can_get_moon_for_2024(self):
		# note: this is just helpful for testing a version of `moon` where
		# the SVS_ID has been added to the github repo but the
		# package hasn't been updated to include the new SVS_ID
		m = Moon()
		m.set_moon_datetime(date="2024-01-15", hour=1)
		m.request_moon_image()
		assert m.image_src == "https://svs.gsfc.nasa.gov/vis/a000000/a005100/a005187/frames/730x730_1x1_30p/moon.0338.jpg"

	def test_gets_new_moon_info_if_another_year_requested(self):
		m = Moon()
		m.set_moon_phase("2019-01-15", 9)
		m.set_moon_phase("2020-01-15", 9)
		assert m.moon_datetime_info['time'] == '2020-01-15T09:00'

	def test_no_errors_if_none_argument_for_date(self):
		m = Moon()
		m.set_moon_phase()
		assert m.requested_datetime


if __name__ == '__main__':
	unittest.main()