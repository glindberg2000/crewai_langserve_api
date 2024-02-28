from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
import os
from app.crewaiapp import chain as crewaiapp

app = FastAPI()
openai_api_key = os.getenv("OPENAI_API_KEY")


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
# add_routes(app, NotImplemented)

add_routes(app, crewaiapp, path="/crewai")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
