from langchain import OpenAI, ConversationBufferMemory # type: ignore
from langchain.agents import initialize_agent # type: ignore
import json
import os

class BusinessAgent:
    def __init__(self, business_id: str):
        self.business_id = business_id
        self.config = self.load_config()
        self.memory = ConversationBufferMemory()
        self.llm = OpenAI(model_name=self.config['model_name'])
        self.agent = self.initialize_agent()

    def load_config(self):
        config_path = os.path.join('configs', f'{self.business_id}.json')
        with open(config_path, 'r') as file:
            return json.load(file)

    def initialize_agent(self):
        tools = self.load_tools()
        return initialize_agent(tools, self.llm, memory=self.memory)

    def load_tools(self):
        tools = []
        for tool_name in self.config['tools']:
            tool_module = __import__(f'tools.{tool_name}', fromlist=[''])
            tools.append(tool_module.Tool())
        return tools

    def chat(self, user_input: str):
        response = self.agent.run(user_input)
        return response

    def remember_context(self, context: str):
        self.memory.save_context({"input": context}, {"output": ""})  # Placeholder for output

    def adapt_tone(self, response: str):
        # Logic to adapt the response tone based on the business config
        return response  # Placeholder for tone adaptation logic
    import os
import json
from langchain.agents import initialize_agent, Tool # type: ignore
from langchain.memory import ConversationBufferMemory # type: ignore
from langchain.llms import OpenAI # type: ignore
from tools.crm_tool import CRMTool
from tools.ad_analytics_tool import AdAnalyticsTool
from tools.web_searcher import WebSearcher

# Load configuration for a specific business
def load_business_config(business_id: str) -> dict:
    config_path = f"configs/{business_id}.json"
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file for business_id '{business_id}' not found.")
    with open(config_path, "r") as file:
        return json.load(file)

# Initialize tools dynamically based on the config
def initialize_tools(config: dict) -> list:
    tools = []
    if "tools" in config:
        if "crm" in config["tools"]:
            tools.append(Tool(name="CRM Tool", func=CRMTool().run, description="Access CRM data."))
        if "ad_analytics" in config["tools"]:
            tools.append(Tool(name="Ad Analytics Tool", func=AdAnalyticsTool().run, description="Analyze ad performance."))
        if "web_search" in config["tools"]:
            tools.append(Tool(name="Web Searcher", func=WebSearcher().run, description="Search the web."))
    return tools

# Initialize the agent
def initialize_agent_for_business(business_id: str):
    config = load_business_config(business_id)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    tools = initialize_tools(config)
    llm = OpenAI(temperature=config.get("temperature", 0.7))  # Use OpenAI as the LLM backend
    agent = initialize_agent(tools, llm, memory=memory, agent_type="conversational-react-description")
    return agent

# Get agent response
def get_agent_response(business_id: str, user_input: str) -> str:
    agent = initialize_agent_for_business(business_id)
    response = agent.run(user_input)
    return response

# Onboard a new business
def onboard_business(business_id: str, config: dict):
    config_path = f"configs/{business_id}.json"
    if os.path.exists(config_path):
        raise FileExistsError(f"Business with ID '{business_id}' is already onboarded.")
    with open(config_path, "w") as file:
        json.dump(config, file)