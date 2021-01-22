import unittest
from ..dialamoon import Moon
from ..terminal_ui import TerminalUi
from datetime import datetime
from time import sleep
import numpy
import copy

class TestAsciiMoon(unittest.TestCase):
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

    def test_gets_json_year_data(self):
    	m = Moon()
    	m.set_moon_datetime("2019-01-01")
    	m.make_json_year_data_url()
    	m.set_json_year_data()
    	assert m.moon_year_info[0]["time"] == '01 Jan 2019 00:00 UT'

    def test_caches_json_year_data(self):
    	m = Moon()
    	m.set_moon_datetime(date="2019-01-01")
    	m.make_json_year_data_url()
    	time1 = datetime.now()
    	m.set_json_year_data()
    	time2 = datetime.now()
    	sleep(5)
    	time3 = datetime.now()
    	m.set_json_year_data()
    	time4 = datetime.now()
    	#print(time1, time2, time3, time4, sep="\n")
    	assert (time4 - time3).seconds == 0

    def test_gets_json_for_requested_datetime(self):
    	m = Moon()
    	m.set_moon_datetime("2019-01-01")
    	m.make_json_year_data_url()
    	m.set_json_year_data()
    	m.set_json_specific_data()
    	#print(m.moon_datetime_info)
    	assert m.moon_datetime_info["time"] == '01 Jan 2019 01:00 UT'

    def test_gets_moon_image_as_numpy_array(self):
    	m = Moon()
    	m.set_moon_datetime("2019-01-01")
    	m.request_moon_image()
    	#print(type(m.image))
    	#assert type(m.image) == "<class 'numpy.ndarray'>"	
    	self.assertIs(type(m.image), numpy.ndarray)

    def test_saves_time_getting_same_moon_image(self):
    	m = Moon()
    	m.set_moon_datetime("2019-01-01")
    	m.request_moon_image()
    	m.set_moon_datetime("2019-01-02")
    	m.request_moon_image()
    	time1 = datetime.now()
    	m.request_moon_image()
    	time2 = datetime.now()
    	assert (time2 - time1).seconds == 0

    def test_changes_moon_image_on_second_request(self):
    	m = Moon()
    	m.set_moon_datetime("2019-01-01")
    	m.request_moon_image()
    	url1 = m.url
    	im1 = copy.deepcopy(m.image)
    	m.set_moon_datetime("2020-01-01")
    	url2 = m.url
    	m.request_moon_image()
    	im2 = m.image
    	assert url1 != url2 and not numpy.array_equal(im1,im2)

    def test_caches_moon_image_from_first_request(self):
    	m = TerminalUi()
    	m.set_moon_datetime("2020-01-06")
    	m.request_moon_image()
    	print("im source 1", m.image_src)
    	url1 = m.url
    	im1 = copy.deepcopy(m.image)
    	m.show()
    	m.set_moon_datetime("2020-01-01")
    	url2 = m.url
    	m.request_moon_image()
    	print("im source 2", m.image_src)
    	im2 = copy.deepcopy( m.image)
    	m.show()
    	m.set_moon_datetime("2020-01-06")
    	url3 = m.url
    	time2 = datetime.now()
    	m.request_moon_image()
    	print("im source 3", m.image_src)
    	time3 = datetime.now()
    	im3 = copy.deepcopy(m.image)
    	m.show()
    	print((time3 - time2).seconds)
    	print(url1, url3, sep="\n")
    	#assert url1 == url3 and numpy.array_equal(im1,im3) and (time3 - time2).seconds == 0
    	assert numpy.array_equal(im1,im3)

    # todo: does lru_cache speed up getting json from separate urls?
    # def test_only_caches_max2_json_year_data(self):
    # 	m = Moon()
    # 	for date in ["2019-01-01", "2018-01-01", "2017-01-01", "2019-01-01"]:
    # 		m.set_moon_datetime(date=date)
	   #  	m.make_json_year_data_url()
	   #  	time1 = datetime.now()
	   #  	m.set_json_year_data()
	   #  	time2 = datetime.now()
	   #  	#print(date, m.moon_year_info[0]['time'], time1, time2, sep="\n")
	   #  	#sleep(5)


    # 	assert (time2 - time1).seconds != 0


if __name__ == '__main__':
    unittest.main()