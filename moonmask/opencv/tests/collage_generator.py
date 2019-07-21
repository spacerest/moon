import pytest
import cv2
from .. import collage_generator
from .. import custom_image
from copy import copy
from moonmask.opencv.tests.res.constants import *
import numpy as np
def pytest_namespace():
    return {'collage_generator': None}

class TestClass(object):
    def test_moon_has_size_defined(self):
        pytest.collage_generator = collage_generator.CollageGenerator(SIZE)
        pytest.collage_generator.set_moon(date=DATE)
        assert pytest.collage_generator.moon_image.size == SIZE

    def test_gets_nasa_id(self):
        assert pytest.collage_generator.moon_image.frame_id == FRAME_ID

    def test_moon_has_url(self):
        assert 'url' in dir(pytest.collage_generator.moon_image)

    def test_gets_moon_url(self):
        assert pytest.collage_generator.moon_image.url == URL

    # collage_generator has a dictionary of collages
    def test_has_no_collages(self):
        assert pytest.collage_generator.collage_store == {}

    def test_has_no_masks(self):
        assert pytest.collage_generator.mask_store == {}

    #def test_stores_a_mask(self):
    #    mask = np.zeros((3,3,3), 'uint8')
    #    mask[1][1] = [255, 255, 255]
    #    RED, GREEN, BLUE = (2, 1, 0)
    #    reds = mask[:, :, RED]
    #    greens = mask[:, :, GREEN]
    #    blues = mask[:, :, BLUE]
    #    mask = (greens > 35) | (reds > greens) | (blues > greens)

    #    pytest.collage_generator.store_mask("test_mask", mask)

    #def test_makes_a_mask(self):
    #    pytest.collage_generator.create_mask("test2_mask", IMAGE)

    def test_adds_a_collage(self):
        pytest.collage_generator.create_collage("test_key", SIZE)
        assert type(pytest.collage_generator.collage_store["test_key"]).__name__ == "Collage"

    def test_has_image_store(self):
        pytest.collage_generator.store_image("image1", custom_image.CustomImage(SIZE, image_array=IMAGE))
        assert pytest.collage_generator.image_store["image1"].image.tolist() == IMAGE.tolist()

    def test_copies_image(self):
        pytest.collage_generator.duplicate_image("image1", "image1_copy")
        assert pytest.collage_generator.image_store["image1"] is not pytest.collage_generator.image_store["image1_copy"] and pytest.collage_generator.image_store["image1"].image.tolist() == pytest.collage_generator.image_store["image1_copy"].image.tolist()

    def test_passes_image_into_mask_generator(self):
        pytest.collage_generator.create_mask("passes_image_test", IMAGE)
        im = pytest.collage_generator.mask_store["passes_image_test"].image
        assert IMAGE is im

    def test_opens_moon_image(self):
        pytest.collage_generator.store_image("moon", custom_image.CustomImage(SIZE, filename="tests/res/testmoon.jpg"))
        self.show_image(pytest.collage_generator.image_store["moon"].image)

    def test_sets_moon_image_as_mask(self):
        moon_im = pytest.collage_generator.image_store["moon"].image
        collage = pytest.collage_generator.create_collage("test1", SIZE)
        blue_im = pytest.collage_generator.store_image("blue", custom_image.CustomImage(SIZE, color=(255,0,0)))
        white_im = pytest.collage_generator.store_image("white", custom_image.CustomImage(SIZE, color=(255,255,255)))
        collage.set_positive_space(blue_im)
        collage.set_negative_space(white_im)
        pytest.collage_generator.create_mask("moon", moon_im)
        mask = collage.set_mask(pytest.collage_generator.mask_store["moon"])
        print(mask)
        collage.create()
        self.show_image(pytest.collage_generator.collage_store["test1"].composite)
        

    #def test_sets_mask_to_collage(self):
    #    pytest.collage_generator.create_mask("passes_image_test", IMAGE)
    #    pytest.collage_generator.create_collage("sets_mask_test", SIZE)
    #    pytest.collage_generator.create_mask("mask_test", DOT_IMAGE)
    #    pytest.collage_generator.collage_store["sets_mask_test"].set_mask(pytest.collage_generator.mask_store["mask_test"])
    #    print("mask:")
    #    print(pytest.collage_generator.mask_store["mask_test"].mask)

    #    print(pytest.collage_generator.mask_store)
    #    pytest.collage_generator.collage_store["sets_mask_test"].create()
    #    self.show_image(pytest.collage_generator.collage_store["sets_mask_test"].image)

    #    assert pytest.collage_generator.collage_store["sets_mask_test"].mask.tolist() == pytest.collage_generator.mask_store["passes_image_test"].mask.tolist()

    #def test_sets_moon_as_mask(self):
    #    pytest.collage_generator.create_mask("moon_mask", pytest.collage_generator.moon_image.image)
    #    self.show_image(pytest.collage_generator.moon_image.image)
    #    pytest.collage_generator.collage_store["test_key"].set_mask(pytest.collage_generator.mask_store["moon_mask"])
    #    assert pytest.collage_generator.mask_store["moon_mask"].mask.tolist() == pytest.collage_generator.collage_store["test_key"].mask.tolist()

    #def test_sets_moon_as_mask(self):
    #    pytest.collage_generator.create_mask("moon_mask", pytest.collage_generator.moon_image.image)
    #    self.show_image(pytest.collage_generator.moon_image.image)
    #    pytest.collage_generator.collage_store["test_key"].set_base_array()
    #    pytest.collage_generator.collage_store["test_key"].set_positive_space(color=(255,0,0))
    #    pytest.collage_generator.collage_store["test_key"].set_negative_space(color=(255,255,255))
    #    pytest.collage_generator.collage_store["test_key"].set_mask(pytest.collage_generator.mask_store["moon_mask"])
    #    pytest.collage_generator.collage_store["test_key"].create()
    #    self.show_image(pytest.collage_generator.collage_store["test_key"].composite)
    #    assert pytest.collage_generator.mask_store["moon_mask"].mask.tolist() == pytest.collage_generator.collage_store["test_key"].mask.tolist()

    def show_image(self, image):
        cv2.imshow("test", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

