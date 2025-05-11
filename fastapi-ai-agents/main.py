from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from agent_core import initialize_agent

app = FastAPI()

class ChatRequest(BaseModel):
    user_input: str
    business_id: str

@app.post("/chat")
async def chat(request: ChatRequest):
    business_id = request.business_id
    user_input = request.user_input

    config_path = f"configs/{business_id}.json"
    
    if not os.path.exists(config_path):
        raise HTTPException(status_code=404, detail="Business configuration not found.")

    with open(config_path) as config_file:
        config = json.load(config_file)

    agent = initialize_agent(config)
    response = agent.handle_input(user_input)

    return {"response": response}

@app.post("/onboard")
async def onboard(business_id: str, config: dict):
    config_path = f"configs/{business_id}.json"
    
    if os.path.exists(config_path):
        raise HTTPException(status_code=400, detail="Business already onboarded.")

    with open(config_path, 'w') as config_file:
        json.dump(config, config_file)

    # Initialize memory and tools for the new business here
    # ...

    return {"message": "Business onboarded successfully."}