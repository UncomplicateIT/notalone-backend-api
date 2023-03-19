import torch
import soundfile as sf

from datasets import load_dataset
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan

class TTSHandler:
    def __init__(self) -> None:
        self.processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
        self.model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
        self.vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

        self.embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    
    def get_audio_from_text(self, text):
        inputs = self.__prepare_inputs(text)
        speaker_embeddings = torch.tensor(self.embeddings_dataset[7306]["xvector"]).unsqueeze(0)

        speech = self.model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=self.vocoder)
        return self.__prepare_output(speech)

    def __prepare_inputs(self, text):
        return self.processor(text=text, 
                         return_tensors="pt"
        )
    
    def __prepare_output(self, speech):
        sf.write("speech.wav", speech.numpy(), samplerate=16000)
        return "speech.wav"