from fasthtml.fastapp import *
from ws_tcg import rt, commonHead


@rt("/disclaimer")
def get():
    return disclaimerPage


disclaimerPage = Html(
    commonHead,
    Body(
        P("I do not own any of the images shown. This is just for fun."),
        P(
            "This is just something that I made to play this card game with my friends irl."
        ),
        P("Once again, I do not claim any of the images or even the game itself."),
        style="text-align: center;",
    ),
)
