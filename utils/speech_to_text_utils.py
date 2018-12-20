#! /usr/bin/python3
# =======================================================
# Author        : Astik Anand
# Project       : speech_to_text
# File          : utils/speech_to_text_utils.py
# Description   : Utilities for speech to text conversion
# Date Created  : 20-12-2018
# Date Modified : 20-12-2018
# Python Version: 3.7
# =======================================================

import speech_recognition as sr
from .extras import is_number
from .config import languages, noise_adjust_duration, normal_phrase_time_limit, timeout
from .constants import logger


def set_microphone(recognizer):
    """
    Sets the desired microphopne from list of available microphones.

    Steps:
      • Sets the default microphone for current voice conversation.
      • Gets the list of available microphones currently on the system and displays it.
      • Asks user for the microphone choice they want to use.
      • Adjusts for the noise cancellation and starts listening.
      • Validates if microphone number entered is correct.
      • After all validations, sets the microphone chosen.
      • Returns the microphone object.
    """

    logger.info("Setting the Microphone")
    logger.debug("set_microphone Input: {}".format(recognizer))

    microphone = sr.Microphone()

    available_microphones = sr.Microphone.list_microphone_names()
    number_of_microphones = len(available_microphones)

    print("There are " + str(number_of_microphones) + " microphones available for your system currently.")
    for mic_number in range(number_of_microphones):
        print(str(mic_number+1) + ". " + available_microphones[mic_number])

    microphone_status = False
    while(microphone_status is False):
        print("\nSay which microphone you want to use (say number ex: 1,2,3) ?: ")
        with microphone as source:
            print("Listening for the microphone choice...")
            recognizer.adjust_for_ambient_noise(source, duration=noise_adjust_duration)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=normal_phrase_time_limit)
            print("Listening for the microphone choice over. Thanks!")

        microphone_number = recognizer.recognize_google(audio, language="en-IN")

        if(not is_number(microphone_number)):
            print("You didn't enter a number.\n Try again...")
        else:
            microphone_number = int(microphone_number)
            if(microphone_number > number_of_microphones):
                print("Only " + str(number_of_microphones) + " microphones are available.")
                print("And you are trying to use " + str(microphone_number) + "th microphone.\n Try again...")
            else:
                print("You chose to go with microphone: " + str(microphone_number))
                microphone = sr.Microphone(device_index=microphone_number-1)
                microphone_status = True

    logger.debug("set_microphone Output: {}".format(microphone))
    return microphone


def get_filename(recognizer, microphone):
    """
    Gets the file name from user to save the converted text content.

    Steps:
      • Asks the user to say the name of the file where they want to save text.
      • Adjusts for the noise cancellation and starts listening.
      • Adds the ".txt" type to the file name.
      • Returns the file_name.
    """

    logger.info("Getting the file name")
    logger.debug("get_filename Input: {}".format((recognizer, microphone)))

    file_name = "created_text"
    print("\nSay the file name where you want to save the text: ")
    with microphone as source:
        print("Listening for the file name...")
        recognizer.adjust_for_ambient_noise(source, duration=noise_adjust_duration)
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=normal_phrase_time_limit)
        print("Listening for the file name over. Thanks!")

    file_name = recognizer.recognize_google(audio, language="en-IN")
    file_name += ".txt"
    print("Your chosen file name is: " + file_name)
    
    logger.debug("get_filename Output: {}".format(file_name))
    return file_name



def set_language(recognizer, microphone):
    """
    Sets the language in which user want to speak and convert to text.

    Steps:
      • Asks user in which language the want to speak.
      • Adjusts for the noise cancellation and starts listening
      • Checks if language chosen is available in list of languages.
      • If available, gets the "l10n" code of that language from languages dict.
      • Else asks user to chose the language again.
      • Returns the chosen language.

    """

    logger.info("Setting the language for text conversion")
    logger.debug("set_language Input: {}".format((recognizer, microphone)))

    language_status = False
    language = "english"
    while(language_status is False):
        print("\nSay which language you want to speak in (English, Hindi, Gujarati, Spanish etc.) ?: ")
        with microphone as source:
            print("Listening for the language choice...")
            recognizer.adjust_for_ambient_noise(source, duration=noise_adjust_duration)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=normal_phrase_time_limit)
            print("Listening for the language choice over. Thanks!")

        lang = recognizer.recognize_google(audio, language="en-IN")
        language = lang.lower()
        
        if language in languages:
            language_status = True
        else:
            print("Your chosen language " + language + " is currently not available.")
            print("Try again for some other language...")
    
    print("Your chosen language is: " + language)
    lang_l10n = languages[language]

    logger.debug("set_language Output: {}".format(lang_l10n))
    return lang_l10n
