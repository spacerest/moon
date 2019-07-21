import pytest
import cv2
from .. import collage_generator
from copy import copy
from moonmask.opencv_2.tests.res.constants import *
import numpy as np
def pytest_namespace():
    return {'cg': None}

class TestCollageGenerator(object):
    def test_has_collage_store(self):
        pytest.cg = collage_generator.CollageGenerator(SIZE)
        assert pytest.cg.collage_store == {}

    def test_has_image_store(self):
        assert pytest.cg.image_store == {}

    def test_has_mask_store(self):
        assert pytest.cg.mask_store == {}

    def test_adds_collages(self):
        pytest.cg.start_new_collage("keyword1")
        pytest.cg.start_new_collage("keyword2")
        assert len(pytest.cg.collage_store) == 2

    def test_adds_images(self):
        pytest.cg.add_new_image("keyword1")
        pytest.cg.add_new_image("keyword2")
        assert len(pytest.cg.image_store) == 2

    def test_adds_masks(self):
        pytest.cg.add_new_mask("keyword1")
        pytest.cg.add_new_mask("keyword2")
        assert len(pytest.cg.mask_store) == 2

    def test_selects_collage_when_adding(self):
        pytest.cg.start_new_collage("keyword3")
        assert str(pytest.cg.selected_collage) == "keyword3"

    def test_collage_has_type_collage(self):
        assert type(pytest.cg.selected_collage).__name__ == "Collage"

    def test_change_selected_collage(self):
        pytest.cg.select_collage("keyword2")
        assert str(pytest.cg.selected_collage) == "keyword2"

    def test_load_moon(self):
        pytest.cg.set_moon(DATE, date=DATE)
        assert pytest.cg.image_store[DATE].size == SIZE

    def test_gets_moon_by_keyword(self):
        assert str(pytest.cg.image_store[DATE]) == DATE

    def test_loads_new_image_from_url(self):
        pytest.cg.load_new_image("keyword4", url=IMAGE_URL)
        #self.show_image(pytest.cg.image_store["keyword4"].image)
        assert type(pytest.cg.image_store["keyword4"]).__name__ == "CustomImage"

    def test_loads_new_image_from_array(self):
        pytest.cg.load_new_image("dots_array", image_array=DOT_IMAGE)
        assert pytest.cg.image_store["dots_array"].image.tolist() == DOT_IMAGE.tolist()

    def test_makes_mask_from_array_image(self):
        pytest.cg.add_new_mask("dots_array", image=pytest.cg.image_store["dots_array"].image)
        assert pytest.cg.mask_store["dots_array"].mask.tolist()[0][0] == [0.0, 0.0, 0.0] 

    def test_sets_positive_space_image(self):
        pytest.cg.start_new_collage("keyword5")
        pytest.cg.selected_collage.set_positive_space(pytest.cg.image_store["keyword4"])
        assert pytest.cg.selected_collage.positive_space is pytest.cg.image_store["keyword4"] 

    def test_sets_negative_space_image(self):
        pytest.cg.load_new_image("blue", color=(255,0,0))
        pytest.cg.selected_collage.set_negative_space(pytest.cg.image_store["blue"])
        assert pytest.cg.selected_collage.negative_space.image.tolist()[0][0] == [255, 0, 0]

    def test_sets_mask(self):
        pytest.cg.selected_collage.set_mask(pytest.cg.mask_store["dots_array"])
        assert pytest.cg.selected_collage.mask is pytest.cg.mask_store["dots_array"]
 
    def test_combine_images(self):
        pytest.cg.selected_collage.combine()
        self.show_image(pytest.cg.selected_collage.composite)

    def test_sets_moon_mask(self):
        pytest.cg.add_new_mask(DATE, image=pytest.cg.image_store[DATE].image)
        pytest.cg.selected_collage.set_mask(pytest.cg.mask_store[DATE])
        pytest.cg.selected_collage.combine()
        self.show_image(pytest.cg.selected_collage.composite)


    def show_image(self, image):
        cv2.imshow("test", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

