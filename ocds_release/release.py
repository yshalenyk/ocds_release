from .utils import generate_ocid, now, generate_uri, generate_id
from .tags import Tag


class Release(object):

    def __init__(self, tags, tender):

        if not isinstance(tags, list):
            tags = [tags]

        self.tag = []
        self.language = 'uk'
        self.ocid = generate_ocid(tender['id'])
        self.id = generate_id()
        self.date = now().isoformat()
        self.initiationType = 'tender'
        self.buyer = Tag('buyer', tender).serialize()

        for _tag in tags:
            if _tag in ['award', 'contract']:
                items = tender.get(u'{}s'.format(_tag), '')
                if items:
                    setattr(self, '{}s'.format(_tag),
                            [Tag(_tag, item).serialize() for item in items])
                    self.tag.append(_tag)
            else:
                setattr(self, _tag, Tag(_tag, tender).serialize())
                self.tag.append(_tag)

    def serialize(self):
        return self.__dict__


class Package(object):

    def __init__(
        self,
        tags,
        tenders,
        publisher,
        license,
        publicationPolicy
    ):
        self.publishedDate = now().isoformat()
        self.uri = generate_uri()
        self.releases = [Release(tags, tender).serialize()
                         for tender in tenders]
        self.publisher = publisher
        self.license = license
        self.publicationPolicy = publicationPolicy

    def serialize(self):
        return self.__dict__


