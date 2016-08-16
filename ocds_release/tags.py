import collections
import itertools
from schemas import (
    tender,
    contract,
    award,
    organization_schema
)


class DictUpdateHook(object):

    def _init_hook(self,  **kwargs):
        raise NotImplementedError


class HookedDict(collections.MutableMapping, DictUpdateHook):

    def __init__(self, **kwargs):
        self.store = dict()
        self._init_hook(**kwargs)

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def serialize(self):
        return self.schema(self.store)


class Tender(HookedDict):

    @classmethod
    def tag(cls):
        return "tender"

    def _init_hook(self,  **kwargs):
        self.schema = tender
        self.store.update(kwargs)
        bids = kwargs.get('bids', '')
        self.store['tenderers'] = self._find_tenderers(bids)
        if bids:
            del self.store['bids']

        for k, v in kwargs.iteritems():
            if k == 'submissionMethod':
                self.store['submissionMethod'] = [kwargs['submissionMethod']]
            elif k == 'minimalStep':
                self.store['minValue'] = self.store['minimalStep']
                del self.store['minimalStep']
            else:
                self.store[k] = v
        if 'numberOfBids' in self.store:
            del self.store['numberOfBids']
        self.store['numberOfTenderers'] = len(self.store['tenderers'])

    def _find_tenderers(self, bids):
        if bids:
            return list(itertools.chain.from_iterable(
                map(lambda x: x.get('tenderers', ''), bids)))
        return []


class Award(HookedDict):

    @classmethod
    def tag(cls):
        return "award"

    def _init_hook(self, **kwargs):
        self.schema = award
        self.store.update(kwargs)


class Contract(HookedDict):

    @classmethod
    def tag(cls):
        return "contract"

    def _init_hook(self, **kwargs):
        self.schema = contract
        self.store.update(kwargs)


class Buyer(HookedDict):

    @classmethod
    def tag(cls):
        return "buyer"

    def _init_hook(self, **kwargs):
        self.schema = organization_schema
        self.store.update(kwargs.get('procuringEntity'))


def Tag(tag, values):
    for cls in HookedDict.__subclasses__():
        if cls.tag() == tag:
            return cls(**values)



