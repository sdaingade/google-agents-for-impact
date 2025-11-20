import argparse
import logging
import os
from pathlib import Path

import vertexai
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp

from weather_data_agent.agent import root_agent

def deploy(
    project_id: str,
    location: str,
    staging_bucket: str,
    agent_name: str,
):
    """Deploys the weather agent to Vertex AI Agent Engine."""
    logging.basicConfig(level=logging.INFO)
    vertexai.init(project=project_id, location=location, staging_bucket=staging_bucket)

    # Wrap the ADK agent with AdkApp to make it compatible with Agent Engine
    adk_app_agent = AdkApp(agent=root_agent)

    logging.info(f"Deploying agent: {agent_name}")
    remote_agent = agent_engines.create(
        agent_engine=adk_app_agent,
        display_name=agent_name,
        description="Provides Answers to Users about Weather and Climate related disasters.",
        extra_packages=["./weather_data_agent"],
        requirements=[
            "google-cloud-aiplatform[adk,agent_engines]==1.110.0",
            "vertexai>=1.0.0",
            "google-cloud-bigquery",
            "google-cloud-storage",
            "google-cloud-aiplatform",
            "google-api-python-client",
            "google-auth-httplib2",
            "google-auth-oauthlib",
            "google-auth",
        ],
    )

    logging.info(f"Agent deployed successfully. Resource name: {remote_agent.resource_name}")
    return remote_agent

# From student_04_9385d4f57898@cloudshell:~/google-agents-for-impact/challenge-weather-data$
# python deploy.py   --project-id "qwiklabs-gcp-04-a2f8b45168e3"   --staging-bucket "gs://qwiklabs-gcp-04-a2f8b45168e3-bucket"
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy the weather agent to Vertex AI Agent Engine.")
    parser.add_argument("--project-id", required=True, help="Your Google Cloud project ID.")
    parser.add_argument("--location", default="us-central1", help="The GCP region for deployment.")
    parser.add_argument("--staging-bucket", required=True, help="GCS bucket for staging deployment artifacts (e.g., gs://your-bucket).")
    parser.add_argument("--agent-name", default="Weather Data App", help="Display name for the deployed agent.")

    args = parser.parse_args()

    deploy(
        project_id=args.project_id,
        location=args.location,
        staging_bucket=args.staging_bucket,
        agent_name=args.agent_name,
    )