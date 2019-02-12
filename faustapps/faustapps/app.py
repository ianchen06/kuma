# proj/app.py
import faust

app = faust.App(
    'faustapps',
    version=1,
    broker='kafka://10.30.0.101:9092',
    autodiscover=True,
    origin='faustapps'   # imported name for this project (import proj -> "proj")
)

def main() -> None:
    app.main()
