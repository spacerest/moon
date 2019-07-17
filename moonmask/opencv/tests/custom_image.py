import pytest
import cv2

SIZE = (1000,1000)

def pytest_namespace():
    return {'custom_image': None}

class TestClass(object):
    def test_imports_work(self):
        from .. import custom_image
        pytest.custom_image = custom_image.CustomImage((1000,1000))
        assert type(pytest.custom_image).__name__ == "CustomImage"
    def test_makes_image_right_size(self):
        assert pytest.custom_image.size == SIZE
    def test_make_black_image(self):
        pytest.custom_image.make_custom_image((0,0,0))
        assert pytest.custom_image.image[0][0].all() == 0
    def test_pull_from_url(self):
        pytest.custom_image.load_from_url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-v0jIG6GMLRO_Wel0PV6cHmzc8iwve_1hW7GeiSUq_wosKJXysw")
        assert pytest.custom_image.image.shape[0:2] == SIZE
    def test_show_image(self):
        cv2.imshow("test", pytest.custom_image.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


