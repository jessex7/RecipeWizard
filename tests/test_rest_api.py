import pytest
#from recipe_wizard import

def test_get_all_recipes(client, app):
    API_VERSION = app.config.get("API_VERSION")
    SITE_ADDRESS = app.config.get("SITE_ADDRESS")
    endpoint = "/".join([SITE_ADDRESS, "api", API_VERSION, "recipes"])
    assert client.get(endpoint).status_code == 200
