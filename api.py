from fastapi import FastAPI
from fastapi.responses import StreamingResponse

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
    return chatgpt.get_text_from_input(text, action)

@app.get("/whisper")
async def whisper():
    pass

@app.get("/tts")
async def tts(text: str):
    def iterfile():
        with open(tts.get_audio_from_text(text), mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="audio/mp3")
    