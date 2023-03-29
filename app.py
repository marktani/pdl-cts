from capitains_nautilus.flask_ext import FlaskNautilus
from capitains_nautilus.cts.resolver import NautilusCtsResolver
from flask import Flask

resolver = NautilusCtsResolver(
    ["./PDL"])
resolver.parse()

app = Flask("pdl-cts-server")
nautilus = FlaskNautilus(
    name="nautilus",
    app=app,
    resolver=resolver
)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
