from flask import g, jsonify, Blueprint, current_app as app
from ocds_release.models.models import Package


releases = Blueprint('releases', __name__)


@releases.route('/release/<tender_id>')
def release(tender_id):
    tender = g.couch.get(tender_id)
    pack = Package(
        app.package['prefix'],
        [tender],
        app.package['publisher'],
        app.package['license'],
        app.package['publicationPolicy'],
    )
    return jsonify(pack.serialize())
