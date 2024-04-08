from website import create_app, db
from website.models import User, Note, Activity  # Import all your models

def drop_all_tables():
    app = create_app()  # Create Flask app instance
    with app.app_context():
        # Drop all tables
        db.drop_all()
        print("All tables dropped successfully.")

if __name__ == "__main__":
    drop_all_tables()  # Execute the function if the script is run directly
