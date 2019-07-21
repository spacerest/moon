import pytest
import cv2
from moonmask.opencv import custom_image

SIZE = (1000,1000)

def pytest_namespace():
    return {'custom_image': None}

class TestClass(object):
    def test_imports_work(self):
        pytest.custom_image = custom_image.CustomImage((1000,1000))
        assert type(pytest.custom_image).__name__ == "CustomImage"

    def test_makes_image_right_size(self):
        assert pytest.custom_image.size == SIZE

    def test_make_black_image(self):
        pytest.custom_image.make_custom_image((0,0,0))
        assert pytest.custom_image.image[0][0].tolist() == [0, 0, 0]

    def test_pull_from_url(self):
        pytest.custom_image.load_from_url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-v0jIG6GMLRO_Wel0PV6cHmzc8iwve_1hW7GeiSUq_wosKJXysw")
        assert pytest.custom_image.image.shape[0:2] == SIZE

    def test_makes_vertical_stripe_half_image(self):
        #make a white / black striped image
        im = custom_image.CustomImage((2,2))
        im.add_vertical_stripe(0, 0.5, (255, 255, 255))
        assert im.image[0][0].tolist() == [255,255,255] and im.image[0][1].tolist() == [0,0,0]

    def test_makes_horizontal_stripe_half_image(self):
        im = custom_image.CustomImage((2,2))
        im.add_horizontal_stripe(0, 0.5, (255,255,255))
        assert im.image[0][0].tolist() == [255,255,255] and im.image[1][0].tolist() == [0,0,0]

    def test_rotates_image_90_deg(self):
        im = custom_image.CustomImage((2,2))
        im.add_horizontal_stripe(0, 0.5, (255,255,255))
        im2 = custom_image.CustomImage((2,2))
        im2.add_vertical_stripe(0, 0.5, (255, 255, 255))
        im.rot90()
        assert im.image.tolist() == im2.image.tolist()

    def test_rotates_image_180_deg(self):
        im = custom_image.CustomImage((2,2))
        im.add_vertical_stripe(0.5, 1, (255,255,255))
        im2 = custom_image.CustomImage((2,2))
        im2.add_vertical_stripe(0, 0.5, (255, 255, 255))
        im.rot90(times=2)
        assert im.image.tolist() == im2.image.tolist()

    def show_image(self, image):
        cv2.imshow("test", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
