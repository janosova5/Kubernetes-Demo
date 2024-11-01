from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    try:
        response = requests.get("http://service-b")
        service_b_message = response.json().get("message", "No response from Service B")
    except requests.exceptions.RequestException:
        service_b_message = "Service B unavailable"
    
    return {"Hello": "World", "service_b_response": service_b_message}
