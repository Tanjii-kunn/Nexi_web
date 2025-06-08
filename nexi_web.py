from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allow your Vercel frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_bot(request: Request):
    data = await request.json()
    question = data.get("question", "").lower()

    # Your dumb AI brain (if-else)
    if "Hey" in question:
        return {"response": "I'm Nexi, your lil AI homie 🤖"}
    elif "game" in question:
        return {"response": "I'm currently building Doom and some other fire projects!"}
    elif "age" in question:
        return {"response": "I'm timeless, but my dev is still in school 😎"}
    elif "skills" in question:
        return {"response": "HTML, JS, Python, Godot, Unity – the whole toolbox 🔧"}
    else:
        return {"response": "Hmm, I didn't get that. Try asking about my skills or projects!"}
