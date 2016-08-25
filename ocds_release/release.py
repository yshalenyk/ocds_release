from .tags import Tag
from .utils import (
    generate_ocid,
    now,
    generate_uri,
    generate_id,
    get_publisher
)


class Release(object):

    def __init__(self, prefix, tender):

        self.tag = ['tender']
        self.language = 'uk'
        self.ocid = generate_ocid(prefix, tender['tenderID'])
        self.id = generate_id()
        self.date = tender['dateModified']
        self.initiationType = 'tender'
        self.buyer = Tag('buyer', tender).serialize()
        self.tender = Tag('tender', tender).serialize()

        if 'awards' in tender:
            self.tag.append('award')
            setattr(self, 'awards',
                    [Tag('award', award).serialize() for award in tender['awards']])

        if 'contracts' in tender:
            self.tag.append('contract')
            setattr(self, 'contracts',
                    [Tag('contract', contract).serialize() for contract in tender['contracts']]) 

    def serialize(self):
        return self.__dict__


class Package(object):

    def __init__(
        self,
        prefix,
        tenders,
        publisher,
        license,
        publicationPolicy
    ):
        self.publishedDate = now().isoformat()
        self.uri = generate_uri()
        self.releases = [Release(prefix, tender).serialize()
                         for tender in tenders]
        self.publisher = publisher
        self.license = license
        self.publicationPolicy = publicationPolicy

    def serialize(self):
        return self.__dict__


