import os


def get_postgres_uri():
    return os.environ.get("POSTGRES_URL")


def get_api_url():
    return os.environ.get("API_URL")
