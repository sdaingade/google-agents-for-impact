
import os
import google.auth
from google.genai import types
from google.adk.agents import Agent
from google.adk.tools import agent_tool
import vertexai
from vertexai import agent_engines
import logging
import argparse

from .online_research_agent import online_research_agent
from .bigquery_research_agent import bigquery_research_agent

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

MODEL = "gemini-2.5-flash"

agent_generation = types.GenerateContentConfig(
    temperature=0.6,
    top_p=0.9,
    max_output_tokens=32768,
)  


MAIN_AGENT_INSTRUCTIONS="""
You are a friendly weather agent.
Answer questions related to weather and climate related disasters.
You have two helper agent.
- The weather_bigquery_agent has access to a large database containing information from NOAA Global Surface Summary of the day (GSOD) dataset
 and the Global Historical Climatology Network Daily (GHCND) dataset. It includes all sorts of weather and disaster related information.
- The online_research_agent does research for information about climate and weather related disasters online.
You need to combine the results of both the agents to give a comprehensive answer
Do not return SQL commands in the response
"""

root_agent = Agent(
    name="weather_data_agent",
    model=MODEL,
    description="Provides Answers to Users about Weather and Climate related disasters.",
    instruction=MAIN_AGENT_INSTRUCTIONS,
     tools=[
         agent_tool.AgentTool(agent=online_research_agent),
         agent_tool.AgentTool(agent=bigquery_research_agent),
     ],
    generate_content_config=agent_generation,
)
