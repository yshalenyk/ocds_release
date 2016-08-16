import voluptuous


class RemoveSchema(voluptuous.Schema):

    def __init__(self, *args, **kwargs):
        super(RemoveSchema, self).__init__(*args, **kwargs)
        self.extra = int(voluptuous.REMOVE_EXTRA)

def value(val):
    try:
        parsed = int(val)
    except ValueError:
        parsed = float(val)
    return parsed

identifier_schema = RemoveSchema(
    {
        'scheme': unicode,
        'id': unicode,
        'legalName': unicode,
        'uri': unicode
    }
)


document_schema = RemoveSchema(
    {
        'id': unicode,
        'documentType': unicode,
        'title': unicode,
        'description': unicode,
        'url': unicode,
        'datePublished': unicode,
        'dateModified': unicode,
        'format': unicode,
        'language': unicode,
    },
)


classification_schema = RemoveSchema(
    {
        'scheme': unicode,
        'id': unicode,
        'description': unicode,
        'uri': unicode
    }
)
period_schema = RemoveSchema(
    {
        'startDate': unicode,
        'endDate': unicode
    }
)


value_schema = RemoveSchema(
    {
        'amount': value,
        'currency': unicode
    }
)


unit_schema = RemoveSchema(
    {
        'name': unicode,
        'value': value_schema
    }
)


address_schema = RemoveSchema({
    'streetAddress': unicode,
    'locality': unicode,
    'postalCode': unicode,
    'countryName': unicode
})


contact_point_schema = RemoveSchema(
    {
        'name': unicode,
        'email': unicode,
        'telephone': unicode,
        'faxNumber': unicode,
        'url': unicode
    }
)


organization_schema = RemoveSchema(
    {
        'identifier': identifier_schema,
        'additionalIdentifiers': identifier_schema,
        'name': unicode,
        'address': address_schema,
        'contractPoint': contact_point_schema
    }
)


items_schema = RemoveSchema(
    {
        'id': unicode,
        'description': unicode,
        'classification': classification_schema,
        'additionalClassifications': [classification_schema],
        'quantity': int,
        'unit': unit_schema 
    }
)


award = RemoveSchema(
    {
        'id': unicode,
        'title': unicode,
        'description': unicode,
        'status': unicode,
        'date': unicode,
        'value': value_schema,
        'suppliers': [ organization_schema ],
        'items': [ items_schema ],
        'contractPeriod': period_schema,
        'documents':[document_schema]
    }
)

contract = RemoveSchema(
    {
        'id': unicode,
        'awardID': unicode,
        'title': unicode,
        'description': unicode,
        'status': unicode,
        'period': period_schema,
        'value': value_schema,
        'items': [ items_schema ],
        'dateSigned': unicode,
        'documents':[document_schema]
    }
)


tender = RemoveSchema(
    {
        'id': unicode,
        'title': unicode,
        'description': unicode,
        'status': unicode,
        'items': [items_schema],
        'minValue': value_schema,
        'value': value_schema,
        'procurementMethod': unicode,
        'procurementMethodRationale': unicode,
        'awardCriteria': unicode,
        'awardCriteriaDetails': unicode,
        'submissionMethod': [ unicode ],
        'submissionMethodDetails': unicode,
        'tenderPeriod': period_schema,
        'enquiryPeriod': period_schema,
        'hasEnquiries': unicode,
        'eligibilityCriteria': unicode,
        'awardPeriod': period_schema,
        'numberOfTenderers': int,
        'tenderers': [organization_schema],
        'procuringEntity': organization_schema,
        'documents': [document_schema],
    }
)



