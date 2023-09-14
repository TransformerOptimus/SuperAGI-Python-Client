import requests as requests

from superagi_client.exceptions import UnauthorizedException


def validate_api_key(base_url: str, api_key: str):
    response = requests.get(
        f"{base_url}/api/api-keys/validate", headers={"X-API-Key": api_key}
    )

    if response.status_code == 401:
        raise UnauthorizedException(additional_info=response.text)
