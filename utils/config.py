#! /usr/bin/python3
# ================================================
# Author        : Astik Anand
# Project       : speech_to_text
# File          : utils/config.py
# Description   : config variables for the project
# Date Created  : 20-12-2018
# Date Modified : 20-12-2018
# Python Version: 3.7
# ================================================


##
# List of the languages and their "l10n" code
#
languages = {
    # Indian Languages 
    "assamese": "as",
    "bengali": "bn-IN",
    "english": "en-IN",
    "gujarati": "gu-IN",
    "hindi": "hi-IN",
    "kannada": "ka",
    "maithili": "mai",
    "malyalam": "ml",
    "marathi": "mr",
    "oriya": "or",
    "punjabi": "pa-IN",
    "tamil": "ta",
    "telugu": "te",
    "urdu": "ur",
    
    # Foreign Languages
    "czech": "cs",
    "danish": "da",
    "dutch": "nl",
    "german": "de",
    "greek": "el",
    "spanish": "es",
    "french": "fr",
    "italian": "it",
    "japaneese": "ja",
    "korean": "ka",
    "latin": "la",
    "nepali": "ne-NP",
    "russian": "ru",
    "serbian": "sr",
    "chinese": "zh-CN"
}

noise_adjust_duration = 0.5
timeout = 4
normal_phrase_time_limit = 7
content_phrase_time_limit = 20