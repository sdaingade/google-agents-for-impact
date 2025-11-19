from google.adk.agents import Agent
from google.genai import types
from google.adk.tools import google_search 


# ---- Agent that uses climate related online webite Data Store ----
INSTR = f"""
You do online research on weather and climate related disasters. 
Also, use your own knowledge about weather and climate related disasters.
You can also use the Google Search tool to find relevant information on the web.
When you use the Google Search tool, always cite the source of the information you find.
"""

MODEL = "gemini-2.5-flash"

agent_generation = types.GenerateContentConfig(
    temperature=0.6,
    top_p=0.9,
    max_output_tokens=32768,
)  

online_research_agent = Agent(
    model=MODEL,   # or your preferred Gemini model
    name="online_research_agent",
    description=f"Answer questions about climate and weather related disasters by doing online research.",
    instruction=INSTR,
    tools=[
        google_search
    ],  
    generate_content_config=agent_generation,
)
