from fasthtml.common import *


@dataclass
class SignupPage:
    # email: str
    # password: str

    def __ft__(self):
        return Div(
            Main(
                Form(
                    Input(id="email", type="email", name="email", placeholder="Email"),
                    Input(type="password", name="password", placeholder="Password"),
                    Input(type="password", name="confirm_password", placeholder="Confirm Password"),
                    Button("Signup"),
                    hx_post="/api/signup",
                    hx_target="main"
                ),
                id="main"
            )
        )