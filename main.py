import os
from flask_scss import Scss
from website import create_app

# name the database variable with the database file
DB_NAME = "database.db"
# outline the database file path
INSTANCE_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')

app = create_app(instance_path=INSTANCE_FOLDER_PATH)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(INSTANCE_FOLDER_PATH, DB_NAME)}'

if __name__ == '__main__':
    app.run(debug=True)