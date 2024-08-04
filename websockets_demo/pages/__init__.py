from fasthtml.common import *
from websockets_demo import rt
from websockets_demo.pages.api import *
from websockets_demo.pages.components import (
    LoginPage,
    SignupPage
)


@rt("/")
def get():
    return Titled("Home Page")

@rt("/login")
def get():
    return Titled("Login Page", LoginPage())

@rt("/signup")
def get():
    return Titled("Signup Page", SignupPage())