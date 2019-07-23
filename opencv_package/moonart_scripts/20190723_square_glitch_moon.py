from moonmask.terminal_ui import TerminalUi
DATE = "2019-07-23"
ui = TerminalUi((1000,1000))

ui.start_new_collage("glitchy_square_moon")

ui.set_moon(DATE, date=DATE)
ui.load_new_image("blue", color=(0,0,255))
ui.load_new_image("white", color=(255,255,255))
ui.selected_collage.set_positive_space(ui.image_store["blue"])

ui.selected_collage.set_negative_space(ui.image_store["white"])
ui.image_to_mask(DATE, DATE, alpha_values=4, mask_divisor=1, prep_mask_divisor=255)
ui.selected_collage.set_mask(ui.mask_store[DATE])
ui.selected_collage.combine()

ui.show_collage("glitchy_square_moon")

ui.image_to_mask(DATE, "no glitch", alpha_values=4)
ui.selected_collage.set_mask(ui.mask_store["no glitch"])
ui.selected_collage.combine()

ui.show_collage("glitchy_square_moon")




