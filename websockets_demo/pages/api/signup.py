from datetime import datetime
from fasthtml.common import *
from websockets_demo.pages import rt
from websockets_demo.db.models import User, users

@dataclass
class UserDataclass:
    email: str
    password: str
    confirm_password: str

@rt("/api/signup")
def post(user: UserDataclass, session):
    if user.password != user.confirm_password:
        print("password not the same")
        add_toast(session, "Password not the same", "error")
    else:
        new_user = User(email=user.email, password=user.password, created_at=datetime.now().isoformat())
        users.insert(new_user)
