from datetime import datetime
from fasthtml.common import *
from websockets_demo.pages import rt
from websockets_demo.db.models import User, users, get_user

@dataclass
class UserDataclass:
    email: str
    password: str
    confirm_password: str

@rt("/api/signup")
def post(user: UserDataclass, session):
    print(user)
    if user.password != user.confirm_password:
        print("password not the same")
        add_toast(session, "Password not the same", "error")
        # RedirectResponse("/signup", status_code="401")
    else:
        result = get_user(user.email)
        if len(result) > 0:
            add_toast(session, "User already exist. Try logging in!", "error")
        else:
            new_user = User(email=user.email, password=user.password, created_at=datetime.now().isoformat())
            users.insert(new_user)
