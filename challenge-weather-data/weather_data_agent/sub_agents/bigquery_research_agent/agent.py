import google.auth
from google.genai import types
from google.adk.agents import Agent
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig, WriteMode
 
from weather_data_agent.config import Config
from weather_data_agent.sub_agents.bigquery_research_agent.bigquery_schema import GSOD_DS_SCHEMA, GHCND_DS_SCHEMA


PROJECT_ID = Config.GOOGLE_CLOUD_PROJECT
GSOD_DS = Config.GSOD_DS
GHCND_DS = Config.GHCND_DS
MODEL = Config.MODEL

# Read-only tool config (blocks DDL/DML). You can change to WriteMode.ALLOWED later if needed.
bq_tool_cfg = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

# Instantiate the BigQuery toolset
bq_tools = BigQueryToolset(bigquery_tool_config=bq_tool_cfg)

# Instruct the agent to **only** use your dataset
INSTR = f"""
You are a data analysis agent with access to BigQuery tools. Your queries will run in project `{PROJECT_ID}`.
The dataset you have access to contains information from NOAA Global Surface Summary of the day (GSOD) dataset and
the Global Historical Climatology Network Daily (GHCND).
To query tables from `{GSOD_DS}` for a range of years, use a wildcard table query like `FROM \`{GSOD_DS}.gsod*\`` and filter by the `year` column or by using the `_TABLE_SUFFIX` pseudo column. For example, to query between 2020 and 2022, you can use `WHERE year IN ('2020', '2021', '2022')` or `WHERE _TABLE_SUFFIX BETWEEN '2020' AND '2022'`.
To query tables from `{GHCND_DS}` for a range of years, use a wildcard table query like `FROM \`{GHCND_DS}.ghcnd_*\`` and filter by extracting the year from the `date` column or by using the `_TABLE_SUFFIX` pseudo column.
Always fully qualify table names.
Never perform DDL/DML; SELECT-only. Return the SQL you ran along with a concise answer.
The schema for all `gsod` tables is the same. Here is the schema for one of them, please study it: {GSOD_DS_SCHEMA}
The schema for all `ghcnd` tables is the same. Here is the schema for one of them, please study it: {GHCND_DS_SCHEMA}
"""

agent_generation = types.GenerateContentConfig(
    temperature=0.6,
    top_p=0.9,
    max_output_tokens=32768,
)  


bigquery_research_agent = Agent(
    model=MODEL,         # Works with ADK; requires a Gemini API key or Vertex AI setup
    name="bigquery_research_agent",
    description="""Analyzes tables in a BigQuery dataset that contains weather information. Tables.""",
    instruction=INSTR,
    tools=[bq_tools],
    generate_content_config=agent_generation,
)