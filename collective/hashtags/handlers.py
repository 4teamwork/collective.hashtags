import re
from plone.app.textfield.interfaces import IRichText
from plone.dexterity.utils import iterSchemata
from zope import schema


def add_hashtags(obj, event):
    """Adds hashtags to subject field.
    """
    pattern = re.compile(r'\B#\w{1,}(?!")\b', re.UNICODE)
    fields = {}
    for schemata in iterSchemata(obj):
        for name, field in schema.getFields(schemata).items():
            if IRichText.providedBy(field) and field.get(obj):
                for tag in pattern.findall(field.get(obj).raw):
                    fields[tag[1:]] = ''
    fields = fields.keys()
    obj.subject = fields
    obj.reindexObject()
