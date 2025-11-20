import argparse
import logging
import os
from pathlib import Path

import vertexai
from vertexai import agent_engines


def deploy(
    project_id: str,
    location: str,
    staging_bucket: str,
    agent_name: str,
):
    """Deploys the weather agent to Vertex AI Agent Engine."""
    logging.basicConfig(level=logging.INFO)
    vertexai.init(project=project_id, location=location, staging_bucket=staging_bucket)

    # Determine the absolute path to the directory containing the 'weather_data_agent' package.
    # This makes the script runnable from anywhere.
    package_parent_dir = os.path.abspath(Path(__file__).parent)

    logging.info(f"Using package path: {package_parent_dir}")

    # Define the agent using ModuleAgent to handle the package structure.
    local_agent = agent_engines.ModuleAgent(
        module_name="weather_data_agent.agent",
        agent_name="root_agent",
        sys_paths=[package_parent_dir],
        register_operations={
            "stream": ["query"],
        },
    )

    logging.info(f"Deploying agent: {agent_name}")
    remote_agent = agent_engines.create(
        agent_engine=local_agent,
        display_name=agent_name,
        description="Provides Answers to Users about Weather and Climate related disasters.",
    )

    logging.info(f"Agent deployed successfully. Resource name: {remote_agent.resource_name}")
    return remote_agent

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