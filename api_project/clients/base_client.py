import httpx
from api_project.utils.api_logger import log_request, log_response

class BaseClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(base_url=self.base_url, event_hooks={"response": [log_response], "request": [log_request]})
    def _request(self, method: str, endpoint: str, **kwargs):
        return self.client.request(method, endpoint, **kwargs)