# src/scrap_generator/server.py

import uvicorn
from scrap_generator.app import create_app
from scrap_generator.config import settings

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.port)
