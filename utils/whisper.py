import os
import openai

class WhisperHandler:
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def get_text_from_audio(self, usecase):
        pass

    def __transcribe(self, file_path):
        pass

    def __translate(self, file_path):
        pass

    def __asr(self, stream):
        pass