import os

DEFAULT_FLIGHT_URL = os.environ.get("SPICE_FLIGHT_URL", "grpc+tls://flight.spiceai.io")
DEFAULT_FIRECACHE_URL = os.environ.get("SPICE_FIRECACHE_URL", "grpc+tls://firecache.spiceai.io")
DEFAULT_HTTP_URL = os.environ.get("SPICE_HTTP_URL", "https://data.spiceai.io")

DEFAULT_LOCAL_FLIGHT_URL = os.environ.get("SPICE_LOCAL_FLIGHT_URL", "grpc://localhost:50051")
DEFAULT_LOCAL_HTTP_URL = os.environ.get("SPICE_LOCAL_HTTP_URL", "http://localhost:3000 ")
