# 1. Install necessary libraries (Run this once if needed)
#!pip install -q langchain langchain-groq duckduckgo-search langchain-community langchain-classic gradio
#!pip install -U ddgs

import os
import gradio as gr
from google.colab import userdata
from langchain_groq import ChatGroq
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# 2. Setup your API Key securely from Colab Secrets 🔑
os.environ["GROQ_API_KEY"] = userdata.get('groq_API_key')

# 3. The Workers (Tools) 🛠️
search_tool = DuckDuckGoSearchRun()

@tool
def calculator(a: float, b: float, operation: str) -> float:
    """Performs math operations. operation can be 'add', 'subtract', 'multiply', or 'divide'."""
    if operation == 'add': return a + b
    if operation == 'subtract': return a - b
    if operation == 'multiply': return a * b
    if operation == 'divide': return a / b
    return 0.0

tools = [search_tool, calculator]

# 4. The Brain 🧠
llm = ChatGroq(model="openai/gpt-oss-20b")

# 5. STRICT JOB DESCRIPTION 📝 (Updated with Starting City)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert Travel Planner. Use the search tool to find live hotel prices, flight prices from the starting city, and REAL-TIME WEATHER. Use the calculator. IMPORTANT RULES: 1. Do not search more than 3 times. If you cannot find exact prices quickly, make a realistic estimate. 2. Always ensure total cost <= budget. 3. CRITICAL: When calling a tool, use EXACTLY the tool name (e.g., 'calculator'). Do NOT append any extra text or tags like <|channel|> to the tool name!"),
    ("human", "Starting City: {starting_city}, Destination: {destination}, Days: {days}, Budget: {budget}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 6. Build Agent 
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=5, handle_parsing_errors=True, early_stopping_method="generate")

# 7. GRADIO FUNCTION & UI 🎨 (Updated with starting_city)
def trip_planner(starting_city, destination, days, budget):
    try:
        result = agent_executor.invoke({
            "starting_city": starting_city,
            "destination": destination,
            "days": days,
            "budget": budget
        })
        return result['output']
    except Exception as e:
         return f"Oops, error in planning: {str(e)}"

interface = gr.Interface(
    fn=trip_planner,
    inputs=[
        gr.Textbox(label="📍 Starting City (e.g., Hyderabad, Telangana)"),
        gr.Textbox(label="✈️ Destination (e.g., Goa, Dubai)"),
        gr.Number(label="📅 Number of Days"),
        gr.Number(label="💰 Budget (in Rupees)")
    ],
    outputs=gr.Textbox(label="📝 Your Custom Travel Plan", lines=15),
    title="🌍 Smart AI Travel Planner",
    description="Enter your trip details below and let AI design the perfect itinerary from your city, with live weather and budget tracking!"
)

# Launch the Web App!
interface.launch(debug=True)
