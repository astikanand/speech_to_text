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

import speech_recognition as sr
from utils.constants import logger
from utils.speech_to_text_utils import(
    set_microphone,
    get_filename,
    set_language
)
from utils.config import noise_adjust_duration, content_phrase_time_limit, timeout


def speech_to_text():
    """
    Converts speech to text and saves to a file.

    Steps:
      • Gets a speech recognizer object.
      • Sets the microphone from available list of microphones.
      • Gets the file name wherer the converted text is to be saved.
      • Sets the knowledge for the speech.
      • Adjusts for the noise cancellation and starts listening.
      • Converts the text and save to the given file
    """

    logger.info("Into speech to text conversion")

    recognizer = sr.Recognizer()
    microphone = set_microphone(recognizer)
    file_name = get_filename(recognizer, microphone)
    language = set_language(recognizer, microphone)

    with microphone as source:
        print("\nListening for the content...")
        recognizer.adjust_for_ambient_noise(source, duration=noise_adjust_duration)
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=content_phrase_time_limit)
        print("Listening to content over. Thanks!")

    text_content = recognizer.recognize_google(audio, language=language)

    with open(file_name,'w+') as file:
        file.write(text_content)
    
    print("Your file " + file_name + " is created with the spoken text content.")
    

# Start the speech to text conversion 
speech_to_text()
