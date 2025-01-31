import uvicorn
from core import config

if __name__ == "__main__":
    uvicorn.run(
        app="app:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True,
        workers=1,
    )