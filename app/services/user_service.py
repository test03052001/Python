from app.models import user_model

def register_user(data):
    user_model.create_user(
        data["name"],
        data["email"],
        data["password"]
    )

def list_users():
    return user_model.get_users()