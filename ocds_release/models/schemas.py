import voluptuous


class BaseOCDSSchema(voluptuous.Schema):

    def __init__(self, *args, **kwargs):
        super(BaseOCDSSchema, self).__init__(*args, **kwargs)
        self.extra = int(voluptuous.REMOVE_EXTRA)


def value(val):
    try:
        parsed = int(val)
    except ValueError:
        parsed = float(val)
    return parsed


def tender_status(status):
    if status not in ['complete', 'unsuccessful', 'cancelled']:
        return 'active'
    return status


identifier_schema = BaseOCDSSchema(
    {
        'scheme': unicode,
        'id': unicode,
        'legalName': unicode,
        'uri': unicode
    }
)


document_schema = BaseOCDSSchema(
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


classification_schema = BaseOCDSSchema(
    {
        'scheme': unicode,
        'id': unicode,
        'description': unicode,
        'uri': unicode
    }
)
period_schema = BaseOCDSSchema(
    {
        'startDate': unicode,
        'endDate': unicode
    }
)


value_schema = BaseOCDSSchema(
    {
        'amount': value,
        'currency': unicode
    }
)


unit_schema = BaseOCDSSchema(
    {
        'name': unicode,
        'value': value_schema
    }
)


address_schema = BaseOCDSSchema({
    'streetAddress': unicode,
    'locality': unicode,
    'postalCode': unicode,
    'countryName': unicode
})


contact_point_schema = BaseOCDSSchema(
    {
        'name': unicode,
        'email': unicode,
        'telephone': unicode,
        'faxNumber': unicode,
        'url': unicode
    }
)


organization_schema = BaseOCDSSchema(
    {
        'identifier': identifier_schema,
        'additionalIdentifiers': identifier_schema,
        'name': unicode,
        'address': address_schema,
        'contactPoint': contact_point_schema
    }
)


items_schema = BaseOCDSSchema(
    {
        'id': unicode,
        'description': unicode,
        'classification': classification_schema,
        'additionalClassifications': [classification_schema],
        'quantity': int,
        'unit': unit_schema
    }
)


award = BaseOCDSSchema(
    {
        'id': unicode,
        'title': unicode,
        'description': unicode,
        'status': unicode,
        'date': unicode,
        'value': value_schema,
        'suppliers': [organization_schema],
        'items': [items_schema],
        'contractPeriod': period_schema,
        'documents': [document_schema]
    }
)

contract = BaseOCDSSchema(
    {
        'id': unicode,
        'awardID': unicode,
        'title': unicode,
        'description': unicode,
        'status': unicode,
        'period': period_schema,
        'value': value_schema,
        'items': [items_schema],
        'dateSigned': unicode,
        'documents': [document_schema]
    }
)


tender = BaseOCDSSchema(
    {
        'id': unicode,
        'title': unicode,
        'description': unicode,
        'status': tender_status,
        'items': [items_schema],
        'minValue': value_schema,
        'value': value_schema,
        'procurementMethod': unicode,
        'procurementMethodRationale': unicode,
        'awardCriteria': unicode,
        'awardCriteriaDetails': unicode,
        'submissionMethod': [unicode],
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
