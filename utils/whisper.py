import os
import openai

os.environ['OPENAI_API_KEY'] = "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"

class WhisperHandler:
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def get_text_from_audio(self, file, usecase="transcribe"):
        """
        Function to get text from audio file

        Args:
            file : Audio File
            usecase (str, optional): The required usecase of the function. 
                                     Available options are "transcribe" and "translate".
                                     "transcribe": Transcribe audio into whatever language the audio is in. 
                                     "translate": Translate and transcribe the audio into english
                                     Defaults to "transcribe".

        Returns:
            transcript (str): The transcript of the audio file
        """

        # ---------------------- Supported Languages ---------------------- #
        # Supported languages for transcribe and translate
        #
        # Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, 
        # Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, 
        # German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, 
        # Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, 
        # Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, 
        # Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.
        # ------------------------------------------------------------------ #

        # Supported file formats: mp3, mp4, mpeg, mpga, m4a, wav, and webm
        # Supported file size: 25MB
        audio_file= open(file, "rb")

        # Transcribe audio into whatever language the audio is in. 
        if usecase == "transcribe":
            transcript = self.__transcribe(audio_file)
            return transcript
        
        # Translate and transcribe the audio into english
        # Translations to only English are supported
        elif usecase == "translate":
            transcript = self.__translate(audio_file)
            return transcript

    def __transcribe(self, file):
        """
        Function to transcribe audio into whatever language the audio is in.

        Args:
            file: Audio File

        Returns:
            transcript: The transcript of the audio file
        """
        return openai.Audio.transcribe("whisper-1", file)

    def __translate(self, file):
        """
        Function to translate and transcribe the audio into english

        Args:
            file: Audio File

        Returns:
            transcript: The english transcript of the audio file
        """
        return openai.Audio.translate("whisper-1", file)

    def __asr(self, stream):
        pass