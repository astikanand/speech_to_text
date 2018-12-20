# speech_to_text
Converts different language spoken text to speech and writes to a text file.

### Steps:

- Asks user to select a microphone from list of available microphones which they want to use.
- Asks the file name where they want to save the text output.
- Asks for the language choice in which they want to speak.
- Asks for the content for the conversion
- Converts the spoken content into text and writes into the file specified earlier

---------

## Language Supported

**Major Languages:**

- English, Hindi, German, French, Spanish

**Other Indian Languages:**

- Assamese, Bengali, Gujarati, Kannada, Maithili, Malyalam
- Marathi, Oriya, Punjabi, Tamil, Telugu, Urdu
    
**Other Foreign Languages:**

- Czech, Danish, Dutch, Greek, Italian, Japaneese
- Korean, Latin, Nepali, Russian, Serbian, Chinese

---------

## Reuirements

- python3.5+
- pip3
- SpeechRecognition (For speech recognition)
- PyAudio (For working with microphones)
- PortAudio (Pre-requisite for PyAudio: Only in MacOS)


--------


## Dependencies Installation

**SpeechRecognition**

    pip3 install SpeechRecognition

**PyAudio**

    # Debian Linux
    sudo apt-get install python3-pyaudio

    # MacOs
    brew install portaudio
    pip3 install pyaudio

    # Windows
    pip3 install pyaudio
