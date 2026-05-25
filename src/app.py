from fastapi import FastAPI

app = FastAPI()

@app.get("/values")
def get_values():

    return latest_data
