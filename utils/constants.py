#! /usr/bin/python3
# ================================================
# Author        : Astik Anand
# Project       : speech_to_text
# File          : utils/constants.py
# Description   : Common constants for the project
# Date Created  : 20-12-2018
# Date Modified : 20-12-2018
# Python Version: 3.7
# ================================================

import logging

##
# Setting the logger for the entire text_to_speech app by mainly 2 steps
#
# Step-1: Create a console log handler:-> console_log_handler
#       • Initializes a Console Handler using StreamHandler() for the console logs
#       • Sets the level of the initilized handler
#       • Creates a formatter with the required format
#       • Sets the formatter for the initialized handler
#
# Step-2: Create a logger:-> text_to_speech_logger
#       • First get a logger with the name using getLogger()
#       • Add the handler created in Step-1 to the newly created logger
#       • Set the level for the created logger
#
console_log_handler = logging.StreamHandler()
log_formatter = logging.Formatter('%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s')
console_log_handler.setFormatter(log_formatter)
logger = logging.getLogger('text_to_speech_logger')
logger.addHandler(console_log_handler)
logger.setLevel(logging.CRITICAL)
