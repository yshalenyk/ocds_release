import argparse
import datetime
import uuid
import iso8601


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', required=True)
    return parser


def generate_ocid(tender_id):
    return "ocid-32d4gz-fake-{}".format(tender_id)


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


def generate_uri():
    return 'https://fake-url/tenders-{}'.format(uuid.uuid4().hex)


def generate_id():
    return "{}-{}".format(uuid.uuid4().hex, uuid.uuid4().hex)


def get_tender_awards(tender):

    if 'awards' in tender:
        return tender['awards']

    return []
