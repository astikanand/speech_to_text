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
from .constants import logger, recognizer


def set_microphone(recognizer):
    """
    Sets the desired microphopne from list of available microphones.

    Steps:
      • Sets the default microphone for current voice conversation.
      • Gets the list of available microphones currently on the system and displays it.
      • Asks user for the Microphone choice they want to use.
      • Gets the microphone_number after listening.
      • Validates if microphone_number entered is correct.
      • After all validations, sets the microphone chosen.
      • If fails to set Microphone, asks user to set it again
      • Returns the microphone object.
    """

    logger.info("Setting the Microphone")
    logger.debug("set_microphone Input: {}".format(recognizer))

    microphone = sr.Microphone()

    available_microphones = sr.Microphone.list_microphone_names()
    number_of_microphones = len(available_microphones)

    print("There are " + str(number_of_microphones) + " Microphones available for your system currently.")
    for mic_number in range(number_of_microphones):
        print(str(mic_number+1) + ". " + available_microphones[mic_number])

    microphone_status = False
    while(microphone_status is False):
        print("\n\nSay which Microphone you want to use (say number ex: 1,2,3) ?: ")
        microphone_number = listen_from_microphone(microphone, "Microphone choice", normal_phrase_time_limit)

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
      • Asks the user to say the file_name where they want to save text.
      • Gets the file_name after listening.
      • Adds the ".txt" type to the file_name.
      • Returns the file_name.
    """

    logger.info("Getting the file name.")
    logger.debug("get_filename Input: {}".format((recognizer, microphone)))

    file_name = "created_text"

    print("\n\nSay the file name where you want to save the converted text: ")
    file_name = listen_from_microphone(microphone, "file_name choice", normal_phrase_time_limit)

    file_name += ".txt"
    print("Your chosen file name is: " + file_name)
    
    logger.debug("get_filename Output: {}".format(file_name))
    return file_name



def set_language(recognizer, microphone):
    """
    Sets the language in which user want to speak and convert to text.

    Steps:
      • Asks user in which Language the want to speak.
      • Gets the lang name after listening.
      • Checks if language chosen is available in list of languages.
      • If available, gets the "l10n" code of that language from languages dict.
      • Else asks user to chose the language again.
      • Returns the chosen language.

    """

    logger.info("Setting the language for text conversion.")
    logger.debug("set_language Input: {}".format((recognizer, microphone)))

    language_status = False
    language = "english"
    while(language_status is False):
        print("\n\nSay which language you want to speak in (English, Hindi, Gujarati, Spanish etc.) ?: ")
        
        lang = listen_from_microphone(microphone, "Language choice", normal_phrase_time_limit)
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


def listen_from_microphone(microphone, message_text, phrase_time_limit):
    """
    Listens from the microphone returns the converted text.

    Steps:
      • Adjusts for the noise cancellation and starts listening.
      • Listen from the Microphone source.
      • Converts the listened audio to text.
      • If fails to listen or convert, times out to re-listen.
      • Returns the converted_text.
    """

    logger.info("Listening from the microphone.")
    logger.debug("listen_from_microphone Input: {}".format((microphone, message_text, phrase_time_limit)))

    recognizer = sr.Recognizer()

    with microphone as source:
        listened = False
        while(not listened):
            try:
                print("Listening for the " + message_text + "...")
                recognizer.adjust_for_ambient_noise(source, duration=noise_adjust_duration)
                audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                converted_text = recognizer.recognize_google(audio, language="en-IN")
                listened = True
            except:
                print("Listening for the " + message_text + " <<<< TIMED OUT >>>>. Trying again...")
        print("Listening for the " + message_text + " over. Thanks!")
    
    logger.debug("listen_from_microphone Output: {}".format(converted_text))
    return converted_text
