from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import httpx
import json

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:11b"

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat(prompt: dict):
    async def generate():
        async with httpx.AsyncClient(timeout=None) as client:
            payload = {
                "model": MODEL,
                "prompt": prompt.get("prompt", ""),
                "stream": True
            }
            async with client.stream("POST", OLLAMA_URL, json=payload) as response:
                async for line in response.aiter_lines():
                    if line:
                        yield line + "\n"

    return StreamingResponse(generate(), media_type="application/x-ndjson")
