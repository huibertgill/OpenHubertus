from src.config import get_api_key, get_api_url, get_model

def test_configuration():
    assert get_api_key() is not None
    assert get_api_url() is not None
    assert get_model() is not None