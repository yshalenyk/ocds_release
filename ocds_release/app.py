# -*- coding: utf-8 -*-
import yaml
from logging.config import dictConfig
from logging import getLogger
from utils import get_argparser, get_db_url
from flask import Flask, jsonify
from flask.views import View
from .release import Package
import flaskext.couchdb
import json


app = Flask(__name__)


def setup_database(app):
    manager = flaskext.couchdb.CouchDBManager()
    manager.setup(app)
    setattr(app, 'db', manager.connect_db(app))


def update_config(app, config, admin=False):

    db_config = config['db']

    if admin:
        user = db_config['user.admin']['user']
        password = db_config['user.admin']['password']
    else:
        user = db_config['user.user']['user']
        password = db_config['user.user']['password']

    db_url = get_db_url(
        user,
        password,
        db_config['net']['host'],
        db_config['net']['port'],
    )
    app.config.update(
        COUCHDB_SERVER=db_url,
        COUCHDB_DATABASE=db_config['net']['name'],
    )

    app.config.update(config['app'])
    setattr(app, 'package', config.get('package', ''))


class Release(View):

    def dispatch_request(self, tender_id):
        tender = app.db.get(tender_id)
        pack = Package(
            app.package['tags'],
            [tender],
            app.package['publisher'],
            app.package['license'],
            app.package['publicationPolicy'],
        )
        return jsonify(pack.serialize())


def main():
    parser = get_argparser()
    args = parser.parse_args()
    with open(args.config, 'r') as config_file:
        config = yaml.load(config_file.read())
    app.add_url_rule('/release/<tender_id>', view_func=Release.as_view('release'))
    update_config(app, config, admin=True)
    setup_database(app)
    app.run('0.0.0.0', 8080)
