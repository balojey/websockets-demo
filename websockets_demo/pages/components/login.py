from fasthtml.common import *


@dataclass
class LoginPage:
    # email: str
    # password: str

    def __ft__(self):
        return Div(
            Main(
                Form(
                    Input(id="email", type="email", placeholder="Email"),
                    Input(id="password", type="password", placeholder="Password"),
                    Button("Login")
                )
            )
        )