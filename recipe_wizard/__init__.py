from flask import Flask
from recipe_wizard import database


def create_app(testing=False):
    app = Flask("recipe_wizard", instance_relative_config=False)

    if testing:
        app.config.from_object("recipe_wizard.config_testing")
    else:
        app.config.from_object("recipe_wizard.config")

    with app.app_context():
        app.logger
        database.register_database_commands(app)
        database.db.init_app(app)

        @app.get("/")
        def the_index():
            return {"hello, ": "world"}

        from recipe_wizard.rest import recipes_api, grocery_list_api
        from recipe_wizard.web import web

        app.register_blueprint(recipes_api.bp)
        app.register_blueprint(grocery_list_api.bp)
        app.register_blueprint(web.bp)

        print(app.url_map)
    return app
