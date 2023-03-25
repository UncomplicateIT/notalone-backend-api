from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

from utils.tts import TTSHandler
from utils.whisper import WhisperHandler
from utils.chatgpt import ChatGPTHandler

app = FastAPI()
tts = TTSHandler()
whisper = WhisperHandler()
chatgpt = ChatGPTHandler()

@app.middleware("http")
async def addmiddleware(request: Request, call_next):
   print("Middleware works!")
   response = await call_next(request)
   return response

@app.post("/")
async def root():
    return "NotAlone Backend API"

@app.post("/chatgpt")
async def chatgpt_route(
    text: str, 
    action: str
):
    return chatgpt.get_text_from_input(text, action)

@app.post("/whisper")
async def whisper_route(
    token: str,
    usecase: str = "transcribe"
):
    return whisper.get_text_from_audio(token, usecase)

@app.post("/tts")
async def tts_route(text: str):
    return FileResponse(tts.get_audio_from_text(text))
    