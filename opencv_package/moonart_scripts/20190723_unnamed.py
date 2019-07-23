from moonmask.terminal_ui import TerminalUi
DATE = "2019-07-23"
ui = TerminalUi((1000,1000))
import cv2

ui.start_new_collage("pixel_from_glitch")

ui.set_moon(DATE, date=DATE)
ui.load_new_image("cricket", url="https://lh3.googleusercontent.com/_pruqrGApI06RabIHm_Y1d7_YbsfYmd4xiGk3Mhtn6TPVh662auD53NPW50nvBYBzC-NIg_N7eT0X_eTLhFEgAB0YjgpTvlAQFtrpWQsEj7FgGgNJngekkU_AzqYY-3SBoQ341R4yHgwb6HOv-Wh8mMeX_im9D0e5aSROK_EBZEyG-i8zVMRhRl3YuS61UcmPB5Lymk7xyiJow79C6D4uzqhmvIkZzqdJTFEMYGrqtGosLn0ozFi_RPPUBbYU7c_oVxzfhdCfnBwTNgpIQmCpiGbe8EhBA-y83ZVfm4ztiNkk73wAjkBBaRbb4C1D_aoCsSEPnDVts241iPo9LcQdUp-AG3pJaWlf-zdHPz2G0J2fGYif1t5w8b-_56tn_6TPoTNG88cE5dWt3rxsI5V-h09Llet99s60rUd1_-aXvOwqy6TOyqe2rluCw-QpQvVDnHfJaatvK1fT4PRln0Po3-paxrY7BuW0F1aNaGsnQ8FNFHjASueP7RDU8j-PpXR21t5J63RPVH9mG-nDOnBgX_NAv-EFN-T1C_8ufRhvA2HsidnAXGvFJA6FyaTaHHupOwc5rxNkbrSKwPPYgfPRH85vIEclXJqzRbFyK1ctuIiPGy3T-clkXP8fhiANTbysYCHS2k3Y9c9u9Gr6jGHKSgbAsINSfAj=w784-h585-no")
ui.load_new_image("white", color=(255,255,255))
ui.selected_collage.set_positive_space(ui.image_store["cricket"])

ui.selected_collage.set_negative_space(ui.image_store["white"])
ui.image_to_mask(DATE, DATE, mask_divisor=0.5, prep_mask_divisor=255)
ui.image_to_mask(DATE, "smooth")
ui.selected_collage.set_mask(ui.mask_store[DATE])
ui.selected_collage.combine()
#ui.show_collage("pixel_from_glitch")

ui.collage_to_image("pixel_from_glitch", "pixels")
ui.show_image("pixels")
ui.duplicate_image("pixels", "pixelated")
ui.selected_collage.set_negative_space(ui.image_store["white"])
ui.selected_collage.set_positive_space(ui.image_store["pixels"])

ui.selected_collage.set_mask(ui.mask_store["smooth"])
ui.selected_collage.combine()
ui.show_collage("pixel_from_glitch")

ui.collage_to_image("pixel_from_glitch", "pixel_from_glitch2")
ui.selected_collage.set_positive_space(ui.image_store["pixel_from_glitch2"])
ui.image_store["pixelated"].pixelate_image(radius=3, step = 7)
ui.selected_collage.set_negative_space(ui.image_store["pixelated"])

ui.selected_collage.combine()
ui.show_collage("pixel_from_glitch")

ui.collage_to_image("pixel_from_glitch", "2")

ui.selected_collage.set_positive_space(ui.image_store["2"])
ui.selected_collage.set_negative_space(ui.image_store["white"])
ui.selected_collage.combine()

ui.show_collage("pixel_from_glitch")

cv2.imwrite("2019-07-23.jpg", ui.selected_collage.composite)

