from fasthtml.common import *
from websockets_demo import rt


@rt("/")
def get():
    return Titled("Home Page")

@rt("/login")
def get():
    return Titled("Login Page")

@rt("/signup")
def get():
    return Titled("Signup Page")