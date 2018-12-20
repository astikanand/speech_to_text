#! /usr/bin/python3
# =============================================
# Author        : Astik Anand
# Project       : speech_to_text
# File          : utils/extras.py
# Description   : Extra methods for the project
# Date Created  : 20-12-2018
# Date Modified : 20-12-2018
# Python Version: 3.7
# =============================================

def is_number(input):
    """
    Checks and return True if a string input is a number else returns False
    """
    
    status = True
    try:
        int(input)
    except ValueError:
        status = False
    
    return status
