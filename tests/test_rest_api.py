import pytest

def test_get_all_recipes(client, app):
    API_VERSION = app.config.get("API_VERSION")
    SITE_ADDRESS = app.config.get("SITE_ADDRESS")
    endpoint = "/".join([SITE_ADDRESS, "api", API_VERSION, "recipes"])
    response = client.get(endpoint)
    assert response.status_code == 200
    json_data = response.get_json()
    recipes = json_data["data"]
    assert len(recipes) == 3

def test_get_specific_recipe(client, app):
    API_VERSION = app.config.get("API_VERSION")
    SITE_ADDRESS = app.config.get("SITE_ADDRESS")
    endpoint = "/".join([SITE_ADDRESS, "api", API_VERSION, "recipes", "1"])
    response = client.get(endpoint)
    assert response.status_code == 200
    json_data = response.get_json()
    recipe = json_data["data"][0]
    assert recipe["name"] == "Dan Dan Noodles"

