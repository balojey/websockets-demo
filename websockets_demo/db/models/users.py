from websockets_demo.db import db

users = db.t.users

if users not in db.t:
    users.create(id=int, email=str, password=str, created_at=str, pk="id")

User = users.dataclass()

def get_user(email: str):
    query = f"SELECT * FROM users WHERE email = '{email}'"
    result = db.q(query)
    return result