#CURRENTLY ROTATES 90 DEG

from moonmask.terminal_ui import TerminalUi
ui = TerminalUi()
ui.load_new_image("test", filename="test.jpg")
ui.load_new_image("white", color=(255,255,255))
ui.load_new_image("red", color=(0,0,255))
ui.load_new_image("grey", color=(50,50,50))
ui.preview()

#gscale2 = '@%#*+=-:. '
#txt = ui.covertImageToAscii(ui.image_store["test"].image, 100, .5, gscale2)
#
#def reverse_string1(s):
#    """Return a reversed copy of `s`"""
#    return s[::-1]
#
#for x in txt:
##    x = reverse_string1(x)
#    print(x)
#
