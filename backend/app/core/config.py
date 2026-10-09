import os

class Settings:
    PROJECT_NAME: str = "WEATHERNEXUS · National Weather Big Data Analytics Platform (SIH-26069)"
    VERSION: str = "2.0.0-PROD"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./weather_bigdata.db")
    H3_RESOLUTION: int = 7
    RADAR_CORROBORATION_RADIUS_KM: float = 35.0
    SIMHASH_THRESHOLD: int = 3
    SPAM_RATE_LIMIT_PER_HOUR: int = 5
    TWITTER_BEARER_TOKEN: str = os.getenv("TWITTER_BEARER_TOKEN", "")
    SERPAPI_API_KEY: str = os.getenv("SERPAPI_API_KEY", "b846afb1931336e99f21d4348a725a2a55f953cb1bc0d0ac4d6f293f74c75e96")

settings = Settings()

