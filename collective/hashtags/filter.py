import re
from zope.interface import implements
from plone.outputfilters.interfaces import IFilter
from Products.CMFCore.utils import getToolByName


class HashTagsToLinks(object):
    implements(IFilter)
    order = 1000

    def __init__(self, context, request):
        self.context = context

    def is_enabled(self):
        return True

    pattern = re.compile(r'\B#(\w{1,})', re.UNICODE)

    def __call__(self, data):
        portal_url = getToolByName(self.context, 'portal_url').portal_url()
        search_url = '%s/search?Subject=' % portal_url
        return self.pattern.sub(
            '<a href="%s\g<1>">#\g<1></a>' % search_url,
            data.decode('utf8')).encode('utf8')
