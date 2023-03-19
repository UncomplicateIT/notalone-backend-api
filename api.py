from fastapi import FastAPI

from utils.tts import TTSHandler
from utils.whisper import WhisperHandler
from utils.chatgpt import ChatGPTHandler

app = FastAPI()
tts = TTSHandler()
whisper = WhisperHandler()
chatgpt = ChatGPTHandler()

@app.get("/")
async def root():
    return "NotAlone Backend API"

@app.get("/chatgpt")
async def chatgpt(
    text: str, 
    action: str
):
    chatgpt.get_text_from_input(text, action)

@app.get("/whisper")
async def whisper():
    pass

@app.get("/tts")
async def tts(text: str):
    tts.get_audio_from_text(text)