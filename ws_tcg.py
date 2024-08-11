from fasthtml.fastapp import *

app, rt = fast_app()

websiteName = "Unofficial Weiss Schwarz"

commonHead = Head(
    Title(websiteName),
    Meta(charset="utf-8"),
    Meta(
        name="viewport",
        content="width=device-width, initial-scale=1, viewport-fit=cover",
    ),
    Script(src="https://unpkg.com/htmx.org@next/dist/htmx.min.js"),
    Script(src="https://cdn.jsdelivr.net/gh/answerdotai/surreal@1.3.0/surreal.js"),
    Script(src="https://cdn.jsdelivr.net/gh/gnat/css-scope-inline@main/script.js"),
    Link(rel="icon", type="image/x-icon", href="ws.ico"),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css",
    ),
    Style(":root { --pico-font-size: 100%; }"),
    Style(
        ".center{ display: flex;justify-content: center; align-items: center; height: 250px;}"
    ),
)

import __init__

serve()
