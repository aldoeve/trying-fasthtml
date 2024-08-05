from fasthtml.fastapp import *
import datetime

app, rt = fast_app()

@rt("/")
def get():
    nextBanner  = datetime.datetime(2024, 8, 20, 22, 0,0,0)
    currentTime = datetime.datetime.now()
    if currentTime > nextBanner:
        return Titled("Owner is also updating their game...")
    return Titled(f"Time till next banner {nextBanner - currentTime}")

serve()