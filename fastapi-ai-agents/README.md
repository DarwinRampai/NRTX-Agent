# FastAPI AI Agents

This project provides a FastAPI-powered backend that serves personalized AI agents tailored for businesses. Each agent is designed to understand the business's identity, marketing strategy, tone, and advertising goals. The agents are trained, customized, and deployed for each business, allowing for dynamic interaction and support.

## Project Structure

```
fastapi-ai-agents
├── main.py                # Entry point for the FastAPI application
├── agent_core.py          # Core logic for the AI agent
├── tools                  # Directory containing custom tools
│   ├── crm_tool.py        # Dummy CRM tool
│   ├── ad_analytics_tool.py # Dummy ad analytics tool
│   └── web_searcher.py    # Web searcher wrapper
├── configs                # Directory for business configuration files
│   └── examplecorp.json   # Configuration for a specific business
├── embeddings             # Directory for vector databases
│   └── README.md          # Documentation for embeddings
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Features

- **Dynamic AI Agents**: Each agent is customized based on the business's configuration, allowing for tailored interactions.
- **Memory Management**: Agents can remember past interactions and adapt their responses based on previous context.
- **Business-Specific Tools**: Includes dummy tools for CRM and ad analytics, as well as a web searcher for enhanced functionality.
- **Scalability**: Supports onboarding of new businesses through a dedicated endpoint, allowing for easy configuration and initialization.
- **Future-Ready**: Designed to allow for agent fine-tuning and scheduling of tasks in the future.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-ai-agents.git
   cd fastapi-ai-agents
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Usage

- To interact with the AI agent, send a POST request to the `/chat` endpoint with the following JSON body:
  ```json
  {
    "user_input": "Your message here",
    "business_id": "examplecorp"
  }
  ```

- To onboard a new business, send a POST request to the `/onboard` endpoint with the business configuration.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.