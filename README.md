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

- Assamese, Bengali, Gujarati, Kannada, Malyalam
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

    $ pip3 install SpeechRecognition

**PyAudio**

    # Debian Linux
    $ sudo apt-get install python3-pyaudio

    # MacOs
    $ brew install portaudio
    $ pip3 install pyaudio

    # Windows
    $ pip3 install pyaudio


--------

## Run Instructions

You can change the configurations in **utils/config.py**.

    # Noise adjust time: Time to adjust with surrounding noise for noise cancellation
    # Should be < 1, Ideal to keep it 0.5
    noise_adjust_duration = 0.5 

    # timeout: Time it will wait for you to start speaking, will time out after that
    timeout = 3

    # normal_phrase_time_limit: Time to speak normal phrases like (file_name, language etc.)
    normal_phrase_time_limit = 6

    # content_phrase_time_limit: Time to speak your entire content, recommended to increase in actual use
    content_phrase_time_limit = 20


**Running the project:**

    $ cd your/project/location/speech_to_text
    $ python3 speech_to_text.py


---------

## Working Screenshots

**Terminal:**
![speech_to_text_terminal](https://user-images.githubusercontent.com/8958028/50296460-8be79800-04a0-11e9-935c-95024ce36c60.png)

**Output:**
![text_to_speech_output](https://user-images.githubusercontent.com/8958028/50296585-d2d58d80-04a0-11e9-8a68-2e35a785b062.png)
