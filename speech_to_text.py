#! /usr/bin/python3
# =======================================
# Author        : Astik Anand
# Project       : speech_to_text
# File          : speech_to_text.py
# Description   : Converts speech to text
# Date Created  : 20-12-2018
# Date Modified : 20-12-2018
# Python Version: 3.7
# =======================================

from utils.constants import logger, recognizer
from utils.speech_to_text_utils import(
    set_microphone,
    get_filename,
    set_language,
    listen_from_microphone
)
from utils.config import noise_adjust_duration, content_phrase_time_limit, timeout


def speech_to_text():
    """
    Converts speech to text and saves to a file.

    Steps:
      • Gets a speech recognizer object.
      • Sets the Microphone from available list of microphones.
      • Gets the file_name where the converted text is to be saved.
      • Sets the Language for the speech.
      • Gets the text_content after listening.
      • Saves the text_content to the given file_name.
    """

    logger.info("Into speech to text conversion.")

    microphone = set_microphone(recognizer)
    file_name = get_filename(recognizer, microphone)
    language = set_language(recognizer, microphone)

    text_content = listen_from_microphone(microphone, "Content", content_phrase_time_limit)

    with open(file_name,'w+') as file:
        file.write(text_content)
    
    print("Your spoken content: \n" + text_content)
    print("Your file " + file_name + " is created with the spoken text content.")
    

# Start the speech to text conversion 
speech_to_text()
