import pytest
import cv2
from moonmask import collage_generator
from copy import copy
from res.constants import *
import numpy as np
def pytest_namespace():
    return {'cg': None}

class TestCollageGenerator(object):
    def test_makes_collage_generator(self):
        pytest.cg = collage_generator.CollageGenerator(SIZE)
    
    def test_makes_correct_image_from_two_value_mask(self):
        pytest.cg.load_new_image("red", color=(0,0,255))
        pytest.cg.load_new_image("white", color=(255,255,255))
        pytest.cg.duplicate_image("white", "white_copy")
        pytest.cg.image_store["white"].add_vertical_stripe(0, 0.3, (0,0,0))
        pytest.cg.image_store["white"].add_vertical_stripe(0.3, 0.7, (100,100,100))
        pytest.cg.image_to_mask("white", "two_value_mask", alpha_values=2)
        mask = pytest.cg.mask_store["two_value_mask"].mask.tolist()
        pytest.cg.start_new_collage("red_white_collage")
        pytest.cg.selected_collage.set_negative_space(pytest.cg.image_store["red"])
        pytest.cg.selected_collage.set_positive_space(pytest.cg.image_store["white_copy"])
        pytest.cg.selected_collage.set_mask(pytest.cg.mask_store["two_value_mask"])
        pytest.cg.selected_collage.combine()
        #self.show_image(pytest.cg.selected_collage.positive_space.image, key="positive_space_image")
        #self.show_image(pytest.cg.selected_collage.negative_space.image, key="negative_space_image")
        #self.show_image(pytest.cg.selected_collage.mask.image, key="mask image")
        #self.show_image(pytest.cg.selected_collage.mask.mask.astype(np.uint8), key="mask mask")
        #self.show_image(pytest.cg.selected_collage.composite, key="composite")
        print(1 - pytest.cg.selected_collage.mask.mask)
        print(pytest.cg.selected_collage.mask.mask)
        assert pytest.cg.selected_collage.composite.tolist()[0][0] == [0,0,255] and pytest.cg.selected_collage.composite.tolist()[2][0] == [255,255,255]



    def show_image(self, image, key="test"):
        cv2.imshow(key, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return

