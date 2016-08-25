# -*- coding: utf-8 -*-
import yaml
import flaskext.couchdb
from flask import Flask
from .utils import update_config, get_argparser
from .views import releases


app = Flask(__name__)
app.register_blueprint(releases)


def main():
    parser = get_argparser()
    args = parser.parse_args()
    with open(args.config, 'r') as config_file:
        config = yaml.load(config_file.read().encode("utf-8"))
    update_config(app, config, admin=True)
    manager = flaskext.couchdb.CouchDBManager()
    manager.setup(app)
    app.run('0.0.0.0', 8080)
