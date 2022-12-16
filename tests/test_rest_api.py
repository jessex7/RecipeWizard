import pytest

def test_get_all_recipes(client, app):
    ## arrange
    API_VERSION = app.config.get("API_VERSION")
    SITE_ADDRESS = app.config.get("SITE_ADDRESS")
    endpoint = "/".join([SITE_ADDRESS, "api", API_VERSION, "recipes"])

    ## act
    response = client.get(endpoint)

    ## assert
    assert response.status_code == 200
    json_data = response.get_json()
    recipes = json_data["data"]
    assert len(recipes) == 3

def test_get_specific_recipe(client, app):
    ## arrange
    API_VERSION = app.config.get("API_VERSION")
    SITE_ADDRESS = app.config.get("SITE_ADDRESS")
    endpoint = "/".join([SITE_ADDRESS, "api", API_VERSION, "recipes", "1"])
    
    ## act
    response = client.get(endpoint)

    ## assert
    assert response.status_code == 200
    json_data = response.get_json()
    recipe = json_data["data"][0]
    assert recipe["recipe_name"] == "Dan Dan Noodles"

def test_post_recipe(client, app):
    ## arrange
    import json
    API_VERSION = app.config.get("API_VERSION")
    SITE_ADDRESS = app.config.get("SITE_ADDRESS")
    endpoint = "/".join([SITE_ADDRESS, "api", API_VERSION, "recipes"])

    sample_recipe = {
        "recipe_name": "Breakfast bagel",
        "author": "Joe",
        "ingredients": [
                {
                    "ingredient_name":"Plain bagel",
                    "unit":"Bagel",
                    "amount":"1"
                },
                {
                    "ingredient_name":"Eggs",
                    "unit":"Egg",
                    "amount":"3"
                },
                {"ingredient_name":"Cheddar cheese"}
            ],
        "instructions": "Make eggs, toast bagel, put eggs on bagel",
        "prep_time": 1.0,
        "cook_time": 5.0,
        "rating":7
    }
    
    ## act
    # take initial action
    response = client.post(endpoint, json=sample_recipe)
    # take follow-up action to get confirmation data
    recipe_str = (response.get_json())["data"]
    recipe_json = json.loads(recipe_str)
    recipe_id = recipe_json["recipe_id"]
    endpoint = "/".join([SITE_ADDRESS, "api", API_VERSION, "recipes", f"{recipe_id}"])
    second_response = client.get(endpoint)

    ## assert
    assert response.status_code == 200
    assert second_response.status_code == 200

def test_delete_recipe(client, app):
    ## arrange
    API_VERSION = app.config.get("API_VERSION")
    SITE_ADDRESS = app.config.get("SITE_ADDRESS")
    endpoint = "/".join([SITE_ADDRESS, "api", API_VERSION, "recipes", "1"])

    ## act
    response = client.delete(endpoint)

    ## assert
    assert response.status_code == 200
