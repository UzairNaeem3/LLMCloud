from LLMCloud.app import app
from LLMCloud.api.api import router

app.include_router(router=router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
