from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent_core import get_agent_response, onboard_business # type: ignore

app = FastAPI()

# Request model for the /chat endpoint
class ChatRequest(BaseModel):
    user_input: str
    business_id: str

# Request model for the /onboard endpoint
class OnboardRequest(BaseModel):
    business_id: str
    config: dict

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = get_agent_response(request.business_id, request.user_input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/onboard")
async def onboard(request: OnboardRequest):
    try:
        onboard_business(request.business_id, request.config)
        return {"message": f"Business {request.business_id} onboarded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))