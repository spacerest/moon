import pytest
import cv2
from .. import collage
from copy import copy

SIZE = (1000,1000)
HALF_SIZE = (int(SIZE[0]/2), int(SIZE[1]/2))
DATE = "2019-07-17"
FRAME_ID = '4729'
URL = "https://svs.gsfc.nasa.gov/vis/a000000/a004400/a004442/frames/730x730_1x1_30p/moon.4729.jpg"


def pytest_namespace():
    return {'collage': None}

class TestClass(object):
    def test_moon_has_size_defined(self):
        pytest.collage = collage.Collage()
        pytest.collage.set_moon(date=DATE)
        assert pytest.collage.moon_image.size == SIZE

    def test_gets_nasa_id(self):
        assert pytest.collage.moon_image.frame_id == FRAME_ID

    def test_moon_has_url(self):
        assert 'url' in dir(pytest.collage.moon_image)

    def test_gets_moon_url(self):
        assert pytest.collage.moon_image.url == URL

    def test_combines_same_image(self):
        im = pytest.collage.moon_image.image
        pytest.collage.overlay_image_alpha(im,
                                      im,
                                      (0,0),
                                      im[:, :, 2] / 255.0)
        assert im.all() == pytest.collage.image.all()
        #assert im.all() == pytest.collage.image.all()

    def test_combines_different_images(self):
        pytest.collage.set_main_image("white", color=(255,255,255))
        original_image = copy(pytest.collage.image)
        pytest.collage.set_mask_positive_space("black", color=(0,0,0))
        pytest.collage.overlay_image_alpha(pytest.collage.image,
                                           pytest.collage.moon_mask_positive_space,
                                           (0,0),
                                           original_image[:, :, 2] / 155.0)

        assert original_image[HALF_SIZE[0]][500][0] != pytest.collage.image[HALF_SIZE[0]][500][0]

    def test_show_moon_image(self):
        cv2.imshow("test", pytest.collage.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


