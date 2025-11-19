import os

class Config:
    """Application configuration."""
    
    # Read from env var, fallback to a default
    GOOGLE_GENAI_USE_VERTEXAI = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", True)
    GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "qwiklabs-gcp-04-a2f8b45168e3")
    GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
    GSOD_DS = os.getenv("GSOD_DS", "bigquery-public-data.noaa_gsod")
    GHCND_DS = os.getenv("GHCND_DS", "bigquery-public-data.ghcn_d")
    MODEL = os.getenv("MODEL", "gemini-2.5-flash")

    # Need to create a bucket in your project. (It must be public)
    # Image generation will write images to this bucket.
    #IMAGE_BUCKET = os.getenv("IMAGE_BUCKET", "food-agent-generated-images-dar")
                               
    




