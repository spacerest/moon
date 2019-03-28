# UI TEXT STRINGS -- TODO WRITE FOR DIFFERENT LANGUAGES
# TODO - organize these so they aren't random lists / strings, and instead consolidated in some dictionaries or something

PURPOSES_OF_PACKAGE_TUTORIAL_STEP = [
    "Let's talk about what we can do with this package.",
    "* We can get a 'mask' of the current moon phase",
    "* We can use this mask to create an image of the current moon phase.",
    "* We can save this image as is.",
    "* We can get custom images from outside sources, like urls, files, or instagram posts.",
    "* We can use these images as masks together with the mask we got from the moonphase, and create collages."
]
IMPORT_CLASS_TUTORIAL_STEP = [
    "To use this package, it needs to be imported into wherever we're running it. Considering you're already running this tutorial, you've probably already imported it in one way or another.",
    "So, the first line in your code should read:",
     "{}",
    "This import statement imports a class called MoonMaskUI, which is what we'll use to interact with the package.",
]

INITIALIZE_UI_TUTORIAL_STEP = [
    "Now that we have the class MoonMaskUI imported, let's use it. We do this like this:",
    "{}",
    "This code makes a new variable, which we're choosing to call 'ui', and sets it equal to an instance of our class.",
    "Now, we will be able to use this variable 'ui' to make an image."
]

SET_MOON_PHASE_TUTORIAL_STEP = [
    "Since we're here to get the moonphase, let's start there. To get the current moonphase, we call a method 'set_moon_phase' on our ui.",
    "{}",
    "This method will ask for current moon phase from the nasa repository of images, and use it to create a mask, which will later be used to make an image.",
]


INTRO_SAVE_COLLAGE_TUTORIAL_STEP = ["Now that we've set the moonphase mask, let's see what it looks like when transformed to an image.",
                        "We will try this command:",
                        "{}",
                        "This method will make an image and (depending on how we're running this script) show it to us."
                        ]

SET_POSITIVE_SPACE_TUTORIAL_STEP = [
    "Now, let's try customizing this moonphase image a bit. Let's change the positive space in the moon.",
    "Take a look at the little sketch above for what part we are considering the 'positive space' in an image of a full moon.",
    "Now, we change this positive space to having a yellow color like this:",
    "{}"
]

SET_POSITIVE_SPACE_COMMAND = "ui.set_positive_space(color='yellow')"

#TODO set command_prompt icons for these command2-4 in the way you're setting the others
SET_POSITIVE_SPACE_COMMAND2 = ">>  ui.set_positive_space(url='https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png')"
SET_POSITIVE_SPACE_COMMAND3 = ">>  ui.set_positive_space(instagram_url='https://www.instagram.com/p/Bjo2ftsH2KC/')"
SET_POSITIVE_SPACE_COMMAND4 = ">>  ui.set_positive_space(filename='i_am_not_a_real_file.jpg')"

LETS_SAVE_TUTORIAL_STEP = [
    "Let's save this to take a look at it.",
    "{}"
]

SET_NEGATIVE_SPACE_TUTORIAL_STEP = [
    "Now let's change the negative space to yellow with this command:",
    "Take a look at the little sketch above for what part we are considering the 'negative space' in an image of a full moon.",
    "{}"
]

SET_MAIN_IMAGE_TUTORIAL_STEP = [
    "Finally, let's change the 'main image' here. The 'main image' is what these masks are being 'pasted' onto.",
    "We change the main image like this:",
    "{}",
    "We are using a different way of declaring the color here -- it's in 'RGB' format."
]

MORE_INFO = [
    "In this tutorial, we only changed the colors of the positive space, negative space, and main image.",
    "We used the keyword argument 'color' to do this, like ",
    "{}",
    "To use images instead of colors, we can use different keyword arguments, like 'url', 'instagram_url', and 'filename'.",
    "For example:",
    SET_POSITIVE_SPACE_COMMAND2,
    SET_POSITIVE_SPACE_COMMAND3,
    SET_POSITIVE_SPACE_COMMAND4,
    "If you'd like to play around with these different keyword arguments, please give it a try outside of this tutorial!"
]

SET_NEGATIVE_SPACE_COMMAND = "ui.set_negative_space(color='yellow')"

SET_MAIN_IMAGE_COMMAND = "ui.set_main_image(color=(240, 128, 128))"

SAVE_COLLAGE_COMMAND = "ui.save_collage(filename='moon')"

TUTORIAL_PROMPT_FOR_COMMAND = "Try out the above command below (type it just how you see it): "

TUTORIAL_TRY_AGAIN_PROMPT = "That doesn't match '{}', please try again:"

SET_MOON_PHASE_COMMAND = "ui.set_moon_phase()"

IMPORT_UI_COMMAND = "from moonmask.moonmask_ui import MoonMaskUI"

INITIALIZE_UI_COMMAND = "ui = MoonMaskUI()"

THIS_IS_A_TUTORIAL_MESSAGE = "This is a small tutorial on how to use it. For more info on this package, please head over to https://github.com/spacerest/moonmask/README.md"

FINISHED_TUTORIAL_MESSAGE = "Well, this is the end of the moonmask tutorial! For more info on this package, please head over to https://github.com/spacerest/moonmask/README.md. If anything isn't working, please submit an issue on github. Thanks! :)"

NAVIGATION_REMINDER = "To exit this tutorial you can press ctrl-C at any time. To go back in the tutorial you can scroll up ^."

USER_SUCCESS_MESSAGE = "Perfect."

CREDITS_LIST = ["Thanks to Ernie Wright of Nasa for creating the moon visualizations that the generated moon masks are based on. Check out his visualizations here: https://svs.gsfc.nasa.gov/cgi-bin/search.cgi?person=105 ","Thanks to Joan Stark for the ascii art used in this tutorial. I read a nice interview by her here: http://www.lastplace.com/ASCIIart/starkascii.htm.", "If you'd like to help on this project and get added to this credits list, please contact me <3 (my github username is spacerest)"]

SHOW_INFO = "Welcome to moonmask! You can use this package to get a 'mask' of the moonphase for a particular day. You can use this mask to create an image of the current moon phase, or to make a collage using your own photos."

PRESS_ENTER_TO_CONTINUE = "(Please press enter to continue...)"

SAVE_COLLAGE_CONFIRMATION = "A sample image of your collage should have opened up just now. This is a temporary file. You should have a saved version of the image by this name: "

OVERWRITE_FILENAME_NOTICE = "Since you haven't specified a different filename, it will be saved as '{}.jpg'. If you already have a file called '{}.jpg', this will probably overwrite your original file."

HOW_TO_NAME_FILENAME = "To specify a unique filename, you can write filename='mycustomfilename' in the arguments of your method call. For example: ui.save_collage(filename='mycustomfilename') will save a file called 'mycustomfilename.jpg'"

CANCEL_OPTION = "If you'd like to cancel this operation and knowing what you know now, type 'c' and then press enter. Otherwise, just press enter."

WHITESPACE = "\n"

CANCEL_CONFIRMATION = "You've requested to cancel, so the method you called will not be completed as dialed."

PROMPT_FOR_USERNAME = "Please enter your instagram username here and then press enter:\n\n"

PROMPT_FOR_PASSWORD = "Please enter your instagram password below and then press enter (don't worry that the cursor doesn't move while you type):\n\n"

SET_POSITIVE_SPACE_CONFIRMATION = "You have updated the positive space in your collage."

SET_MAIN_IMAGE_CONFIRMATION = "You have updated the main image in your collage."

SET_MOON_PHASE_CONFIRMATION = "You have set a moonphase for the date: "

SET_NEGATIVE_SPACE_CONFIRMATION = "You have updated the negative space in your collage."

SIGNING_INTO_INSTAGRAM_WARNING = "Some notes about this: In how this package is currently set up, you need to type your username and password in the command line to log into Instagram. Do this at your own risk... As a general rule of thumb, it's obviously not good to type your passwords just anywhere. If you want a more secure way of getting your photo to instagram, just email the file to yourself to get it to your phone."

INSTAGRAM_BOT_WARNING = "Another note: This package uses a python package called InstagramAPI that isn't officially approved by Instagram. Using it may violate terms of service with Instagram, and you might run into some issues 'verifying' your login."

INSTAGRAM_BRAND_GROWTH_RAMBLE= "A last note: Instagram doesn't like 3rd party API packages like this, since they're often used to automate accounts to create brand growth (and because bots can be annoying when used in certain ways). By using this InstagramAPI package, you *may* be violating some Instagram rules."

SAVING_INSTAGRAM_SESSION_MESSAGE = "Would you like to save your instagram login for next time? This means that your instagram information (including your username and password and the 'object' that is your instagram account information), will be saved so that you don't need to login next time."

PROMPT_FOR_INSTAGRAM_CAPTION = "If you would like to include a caption with this post, please type it below and press enter. If you don't want one, just type nothing and press enter."

INSTAGRAM_POST_FINAL_CHECK = "OK, you're about to try to post your collage to instagram. You'll probably see some messages from the InstagramAPI package here (like 429 and 404 errors). You can probably ignore those, but if something ends up not working, they could be clues as to why the post didn't work.\n\nIf you'd like to go ahead and try to post your image to instagram, type 'y' and press enter. Otherwise, just press enter to cancel.\n\n"

INSTAGRAM_POST_ATTEMPT_CONFIRMATION = "If you didn't see any major errors, then your picture must have posted to instagram! Check you account. If there *were* issues, don't worry too much about it and just email your picture to yourself if you'd like to post it somewhere."

SKIP_TEXT_MATCH = "pass"
