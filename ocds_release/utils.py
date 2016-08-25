# -*- coding: utf-8 -*-
import argparse
import datetime
import uuid
import iso8601


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', required=True)
    return parser


def generate_ocid(prefix, tenderID):
    return "{}-{}".format(prefix, tenderID)


def now():
    return iso8601.parse_date(datetime.datetime.now().isoformat())


def get_db_url(user, password, host, port, db_name=''):
    if user:
        prefix = "{}:{}".format(user, password)
    else:
        prefix = ""
    return "http://{}@{}:{}/{}".format(
        prefix,
        host,
        port,
        db_name
    )


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



def generate_uri():
    return 'https://prozorro.gov.ua/releases/{}'.format(uuid.uuid4().hex)


def generate_id():
    return uuid.uuid4().hex


def get_tender_awards(tender):

    if 'awards' in tender:
        return tender['awards']

    return []
