import pytest
from unittest.mock import patch, MagicMock
from src.external_api import ExternalAPIError, fetch_user
"""
def test_check_url():

    fake_response =MagicMock()
    fake_response.status_code =200
    fake_response.json.return_value = {"id":1, "name": "Alice"}
    with patch("src.external_api.requests.get", return_value=fake_response) as mock_get:
        # Trigger the call
        fetch_user(1, "http://defaultapi.com")

        # Get the first positional argument from the call
        # args[0] is the URL, args[1] appears to be a timeout or other param (the '5' in your error)
        args, _ = mock_get.call_args
        actual_url = args[0] 
        
        # Now check if the expected domain is in the actual string
        assert "http://defaultapi.com" in actual_url

"""