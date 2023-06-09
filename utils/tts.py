import base64
import banana_dev as banana

class TTSHandler:
    def __init__(self) -> None:
        self.api_key = "656ac1d7-8902-4193-9e5c-c1504aa7b1d9"
        self.model_key = "a16b6c4a-83d6-4663-8b71-d576fc72b669"
    
    def get_audio_from_text(self, text):
        inputs = {
            "text": text,
        }

        speech = banana.run(self.api_key, self.model_key, inputs)
        return self.__prepare_output(speech)

    def __prepare_output(self, speech):
        encoded_bytes = speech['modelOutputs'][0]['audio'].split(',')[1].encode("ascii")
        decoded_bytes = base64.decodebytes(encoded_bytes)

        with open("speech.mp3", "wb") as mp3_file:
            mp3_file.write(decoded_bytes)
        return "speech.mp3"