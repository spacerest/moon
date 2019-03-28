from moonmask.collage import Collage
from moonmask.instagram_wrapper import InstagramWrapper
from moonmask.res.constants import *
from moonmask.res.ascii_art import *
from moonmask.res.ui_text import *
import getpass
import os
from time import sleep
import textwrap
import shutil

class MoonMaskUI():

    def __init__(self):
        self.collage = Collage()
        self.instagram = None
        self.moonmask_filename = None
        self.terminal_width = shutil.get_terminal_size().columns
        self.text_width = int(self.terminal_width * 0.75)
        self.text_margin = int(self.terminal_width * 0.12)
        self.text_wrapper = textwrap.TextWrapper(width=self.text_width)
        self.margin_symbols = "|"*(self.text_margin - 2)+"  "
        self.command_prompt = ">"*3+"  "

    def set_moon_phase(self, date=None, relative_date="today", filename=None):
        """Sets the moon phase that will be used as a mask on the image

        Keyword arguments:
        date -- the date in format YYYYMMDD
        relative_date -- defaults to "today". Other accepted options are "yesterday" and "tomorrow"
        """
        self.print_text((WHITESPACE))
        self.collage.set_mask(date, relative_date, filename)
        moon_phase_date = str(self.collage.get_moon_phase_date())
        self.print_text((WHITESPACE))
        self.print_text((SET_MOON_PHASE_CONFIRMATION))
        self.print_text((WHITESPACE))
        self.print_text((moon_phase_date))

    def set_main_image(self, url="", instagram_url="", filename="", color=""):
        self.print_text((WHITESPACE))
        self.collage.set_main_image(url, instagram_url, filename, color)
        self.print_text((WHITESPACE))
        self.print_text((SET_MAIN_IMAGE_CONFIRMATION))

    def set_negative_space(self, url="", instagram_url="", filename="", color=""):
        self.print_text((WHITESPACE))
        self.collage.set_mask_negative_space(url, instagram_url, filename, color)
        self.print_text((WHITESPACE))
        self.print_text((SET_NEGATIVE_SPACE_CONFIRMATION))

    def set_positive_space(self, url="", instagram_url="", filename="", color=""):
        self.print_text((WHITESPACE))
        self.collage.set_mask_positive_space(url, instagram_url, filename, color)
        self.print_text((WHITESPACE))
        self.print_text((SET_POSITIVE_SPACE_CONFIRMATION))

    def save_collage(self, filename="moonmask", main_image_file=None, mask_file=None, positive_space_file=None, negative_space_file=None, positive_space_transparency=200, negative_space_transparency=50, dimensionality=3, img_size=1000):
        self.print_text((WHITESPACE))
        if (filename.lower() == "moonmask"):
            self.print_text((OVERWRITE_FILENAME_NOTICE.format("moonmask", "moonmask")))
            self.print_text((WHITESPACE))
            self.print_text((HOW_TO_NAME_FILENAME))
            self.print_text((WHITESPACE))
            user_decision = self.get_input((CANCEL_OPTION))
            if (user_decision.strip().lower() == "c"):
                return
        self.collage.make_collage(filename, main_image_file, mask_file, positive_space_file, negative_space_file, positive_space_transparency, negative_space_transparency, dimensionality, img_size)
        self.moonmask_filename = filename + ".jpg"
        self.print_text((WHITESPACE))
        self.print_text((SAVE_COLLAGE_CONFIRMATION))
        self.print_text((WHITESPACE))
        self.print_text((self.moonmask_filename))

    def post_to_instagram(self, save_session=False, usertags=[]):
        self.print_text((WHITESPACE))
        self.print_text((SIGNING_INTO_INSTAGRAM_WARNING))
        self.enter_to_continue()
        self.print_text((WHITESPACE))
        self.print_text((INSTAGRAM_BOT_WARNING))
        self.enter_to_continue()
        self.print_text((INSTAGRAM_BRAND_GROWTH_RAMBLE))
        self.enter_to_continue()
        self.print_text((WHITESPACE))
        user_decision = self.get_input((CANCEL_OPTION))
        if (user_decision.strip().lower() == "c"):
            self.print_text((CANCEL_CONFIRMATION))
            self.print_text((WHITESPACE))
            return
        self.print_text((WHITESPACE))
        username = self.get_input((PROMPT_FOR_USERNAME))
        self.print_text((WHITESPACE))
        password = getpass.getpass(self.text_format(PROMPT_FOR_PASSWORD))
        self.print_text((WHITESPACE))
        save_session = self.get_input((SAVING_INSTAGRAM_SESSION_MESSAGE))
        self.print_text((WHITESPACE))

        if save_session.strip().lower() == "y": save_session = True

        caption = self.get_input((PROMPT_FOR_INSTAGRAM_CAPTION))
        self.print_text((WHITESPACE))

        user_decision = self.get_input((INSTAGRAM_POST_FINAL_CHECK))
        if user_decision.strip().lower() == "y":
            self.instagram = InstagramWrapper(username, password, save_session)
            self.instagram.post_image(self.moonmask_filename, caption, usertags=usertags)
        else:
            self.print_text((CANCEL_CONFIRMATION))
            return
        self.print_text((INSTAGRAM_POST_ATTEMPT_CONFIRMATION))


    def show_info(self):
        self.clear_screen()
        self.print_text((WHITESPACE))
        self.print_ascii_art(MOON_WAXING_ASCII_ART)
        self.print_ascii_art(TITLE_ASCII_ART)
        self.print_text((SHOW_INFO))
        self.print_text((WHITESPACE))
        self.print_text(THIS_IS_A_TUTORIAL_MESSAGE)
        self.print_ascii_art(MOON_WANING_ASCII_ART)
        self.print_text((WHITESPACE))
        self.enter_to_continue()

    def show_credits(self):
        self.clear_screen()
        self.print_ascii_art(MOON_WAXING_ASCII_ART)
        self.print_ascii_art(CREDITS_ASCII_ART)
        self.print_list(CREDITS_LIST)
        self.print_ascii_art(MOON_WANING_ASCII_ART)
        self.enter_to_continue()

    def show_commands(self):
        self.clear_screen()
        self.print_ascii_art(MOON_WAXING_ASCII_ART)
        self.print_ascii_art(ASCII_ART_NUMBERS[0])
        self.print_multiline_text(PURPOSES_OF_PACKAGE_TUTORIAL_STEP)
        self.enter_to_continue()
        self.clear_screen()
        self.print_ascii_art(MOON_WANING_ASCII_ART)

        self.print_ascii_art(ASCII_ART_NUMBERS[1])
        self.print_multiline_text(IMPORT_CLASS_TUTORIAL_STEP, substitute_text = IMPORT_UI_COMMAND)
        self.ask_user_to_repeat_command(IMPORT_UI_COMMAND)
        self.enter_to_continue()
        self.clear_screen()
        self.print_ascii_art(MOON_WAXING_ASCII_ART)

        self.print_ascii_art(ASCII_ART_NUMBERS[2])
        self.print_multiline_text(INITIALIZE_UI_TUTORIAL_STEP, substitute_text=INITIALIZE_UI_COMMAND)
        self.ask_user_to_repeat_command(INITIALIZE_UI_COMMAND)
        self.enter_to_continue()
        self.clear_screen()
        self.print_ascii_art(MOON_WANING_ASCII_ART)

        self.print_ascii_art(ASCII_ART_NUMBERS[3])
        self.print_multiline_text(SET_MOON_PHASE_TUTORIAL_STEP, SET_MOON_PHASE_COMMAND)
        self.ask_user_to_repeat_command(SET_MOON_PHASE_COMMAND)
        self.set_moon_phase()
        self.enter_to_continue()
        self.clear_screen()

        self.print_ascii_art(ASCII_ART_NUMBERS[4])
        self.print_multiline_text(INTRO_SAVE_COLLAGE_TUTORIAL_STEP, SAVE_COLLAGE_COMMAND)
        self.ask_user_to_repeat_command(SAVE_COLLAGE_COMMAND)
        self.save_collage(filename='moon')
        self.enter_to_continue()
        self.clear_screen()

        self.print_ascii_art(ASCII_ART_NUMBERS[5])
        self.print_ascii_art(DIAGRAM_ASCII_ART_POSITIVE_SPACE)
        self.print_multiline_text(SET_POSITIVE_SPACE_TUTORIAL_STEP, SET_POSITIVE_SPACE_COMMAND)
        self.ask_user_to_repeat_command(SET_POSITIVE_SPACE_COMMAND)
        self.set_positive_space(color='yellow')
        self.enter_to_continue()
        self.clear_screen()

        self.print_ascii_art(ASCII_ART_NUMBERS[6])
        self.print_multiline_text(LETS_SAVE_TUTORIAL_STEP, SAVE_COLLAGE_COMMAND)
        self.ask_user_to_repeat_command(SAVE_COLLAGE_COMMAND)
        self.save_collage(filename='moon')
        self.enter_to_continue()
        self.clear_screen()

        #set negative space to yellow and save it
        self.print_ascii_art(ASCII_ART_NUMBERS[7])
        self.print_ascii_art(DIAGRAM_ASCII_ART_NEGATIVE_SPACE)
        self.print_multiline_text(SET_NEGATIVE_SPACE_TUTORIAL_STEP, SET_NEGATIVE_SPACE_COMMAND)
        self.ask_user_to_repeat_command(SET_NEGATIVE_SPACE_COMMAND)
        self.set_negative_space(color='yellow')
        self.enter_to_continue()
        self.clear_screen()

        self.print_ascii_art(ASCII_ART_NUMBERS[8])
        self.print_multiline_text(LETS_SAVE_TUTORIAL_STEP, SAVE_COLLAGE_COMMAND)
        self.ask_user_to_repeat_command(SAVE_COLLAGE_COMMAND)
        self.save_collage(filename='moon')
        self.enter_to_continue()
        self.clear_screen()

        #set main image to color light coral and save it
        self.print_ascii_art(ASCII_ART_NUMBERS[9])
        self.print_ascii_art(DIAGRAM_ASCII_ART_COMPLETE)
        self.print_multiline_text(SET_MAIN_IMAGE_TUTORIAL_STEP, SET_MAIN_IMAGE_COMMAND)
        self.ask_user_to_repeat_command(SET_MAIN_IMAGE_COMMAND)
        self.set_main_image(color=(240,128,128))
        self.enter_to_continue()
        self.clear_screen()

        #save it
        self.print_ascii_art(ASCII_ART_NUMBERS[10])
        self.print_multiline_text(LETS_SAVE_TUTORIAL_STEP, SAVE_COLLAGE_COMMAND)
        self.ask_user_to_repeat_command(SAVE_COLLAGE_COMMAND)
        self.save_collage(filename='moon')
        self.enter_to_continue()
        self.clear_screen()

        #more info
        self.print_ascii_art(ASCII_ART_NUMBERS[11])
        self.print_multiline_text(MORE_INFO, SET_POSITIVE_SPACE_COMMAND)
        self.enter_to_continue()
        self.clear_screen()

    def goodbye_message(self):
        self.print_ascii_art(MOON_WAXING_ASCII_ART)
        self.print_text(FINISHED_TUTORIAL_MESSAGE)
        self.print_text((WHITESPACE))
        self.print_ascii_art(MOON_WANING_ASCII_ART)
        self.enter_to_continue()
        self.clear_screen()
        self.show_credits()

    def show_tutorial(self):
        self.show_info()
        self.print_text(NAVIGATION_REMINDER)
        self.enter_to_continue()
        self.show_commands()
        self.goodbye_message()

    def print_ascii_art(self, ascii_art_list):
        for element in ascii_art_list:
            self.print_text(element[:self.text_width])
        print("")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.mini_sleep()

    def mini_sleep(self):
        sleep(0.2)

    def enter_to_continue(self):
        self.print_text((WHITESPACE))
        self.get_input((PRESS_ENTER_TO_CONTINUE))
        self.print_text((WHITESPACE))

    def print_list(self, list_to_print):
        for element in list_to_print:
            self.print_text((" * " + element))
            print("")

    def print_text(self, text):
        print(self.text_format(text))

    def print_multiline_text(self, text_list, substitute_text=""):
        for text in text_list:
            self.print_text(text.format(self.command_prompt + substitute_text))
            print("")

    def get_input(self, prompt, command_prompt=False):
        if True:
            return input(self.text_format(prompt)+"\n\n" + self.margin_symbols + self.command_prompt)
        else:
            return input(self.text_format(prompt)+"\n\n"+self.margin_symbols)

    def ask_user_to_repeat_command(self, command):
        user_input = self.get_input(TUTORIAL_PROMPT_FOR_COMMAND, command_prompt=True)
        while user_input != command and user_input != SKIP_TEXT_MATCH:
            self.print_text(WHITESPACE)
            user_input = self.get_input(TUTORIAL_TRY_AGAIN_PROMPT.format(command, command_prompt=True))
        self.print_text(WHITESPACE)
        self.print_text(USER_SUCCESS_MESSAGE)

    def text_format(self,text):
        return textwrap.indent(text=self.text_wrapper.fill(text=text), prefix=self.margin_symbols)

