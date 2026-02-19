from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello(name:str = "Alan"):
    return {"message":f"Hello {name}"}

