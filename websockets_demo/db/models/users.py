from websockets_demo.db import db

users = db.t.users

if users not in db.t:
    users.create(id=int, email=str, password=str, created_at=str, pk="id")

User = users.dataclass()