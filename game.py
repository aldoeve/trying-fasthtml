from fasthtml.fastapp import *
from ws_tcg import rt


@rt("/game")
def get():
    return Titled("Still in progress")
