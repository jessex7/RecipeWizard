import pytest
from os import close, unlink
from tempfile import mkstemp
from recipe_wizard import create_app
from recipe_wizard.database import init_db, insert_recipes



@pytest.fixture
def app():
    db_file_descriptor, db_path = mkstemp()
    app = create_app(testing=True)
    with app.app_context():
        init_db()
        insert_recipes(app.config.get("SAMPLE_RECIPES_FILE"))

    yield app
    close(db_file_descriptor)
    unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()

