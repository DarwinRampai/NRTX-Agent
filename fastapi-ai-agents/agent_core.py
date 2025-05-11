from langchain import OpenAI, ConversationBufferMemory
from langchain.agents import initialize_agent
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