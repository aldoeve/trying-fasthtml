from fasthtml.fastapp import *
from ws_tcg import rt, commonHead


@rt("/")
def get():
    return HomePage


HomePage = Html(
    commonHead,
    Body(
        Div(
            P(A(Button("Play"), href="/game"), style="text-align: center;"),
            cls="center",
        ),
        Div(
            P(
                A("DISCLAIMER", href="/disclaimer", target="_blank"),
                style="text-align: center;",
            ),
            cls="center",
        ),
    ),
)
