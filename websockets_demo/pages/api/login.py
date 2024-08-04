from fasthtml.common import *
from websockets_demo.pages import rt

@rt("/api/login")
def post(email: str, password: str):
    pass