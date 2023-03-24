from fastapi import FastAPI
from fastapi.responses import FileResponse

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
async def chatgpt_route(
    text: str, 
    action: str
):
    return chatgpt.get_text_from_input(text, action)

@app.get("/whisper")
async def whisper_route():
    pass

@app.get("/tts")
async def tts_route(text: str):
    return FileResponse(tts.get_audio_from_text(text))
    