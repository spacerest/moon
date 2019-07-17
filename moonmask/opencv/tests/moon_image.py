import pytest
import cv2
from .. import moon_image

SIZE = (1000,1000)
DATE = "2019-07-17"
FRAME_ID = '4729'
URL = "https://svs.gsfc.nasa.gov/vis/a000000/a004400/a004442/frames/730x730_1x1_30p/moon.4729.jpg"


def pytest_namespace():
    return {'moon_image': None}

class TestClass(object):
    def test_moon_has_size_defined(self):
        pytest.moon_image = moon_image.MoonImage(SIZE)
        pytest.moon_image.set_moon_image(date=DATE)
        assert pytest.moon_image.size == SIZE

    def test_gets_nasa_id(self):
        assert pytest.moon_image.frame_id == FRAME_ID

    def test_gets_moon_url(self):
        assert pytest.moon_image.url == URL

    def test_show_image(self):
        cv2.imshow("test", pytest.moon_image.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


