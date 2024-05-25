from fastapi import FastAPI

def create_app():
    return FastAPI(
        title='Chat with kafka',
        docs_url='/api/docs',
        description='Simple chat with kafka + DDD'
    )