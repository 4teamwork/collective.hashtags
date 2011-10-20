import unittest2 as unittest
from collective.hashtags.testing import HASH_TAGS_INTEGRATION_TESTING
from collective.hashtags.filter import HashTagsToLinks


class TestSetup(unittest.TestCase):

    layer = HASH_TAGS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.filter = HashTagsToLinks(self.portal, self.portal.REQUEST)

    def test_transform_text(self):
        url = '%s/search?Subject=' % self.portal.absolute_url()
        # text ohne tags
        self.assertEqual(
            self.filter('text ohne tags...'),
            'text ohne tags...')
        #text mit 1 tag
        self.assertEqual(
            self.filter('text mit #tag'),
            'text mit <a href="%stag">#tag</a>' % url)
        #mehrere tags
        self.assertEqual(
            self.filter('mit #mehreren #tags nicht #nacheinander'),
            'mit <a href="%smehreren">#mehreren</a> <a href="%stags">#tags</a> nicht <a href="%snacheinander">#nacheinander</a>' % (url, url, url))
        #hash in einer url
        self.assertEqual(
            self.filter('<a href="www.url.com#tag">tag</a>'),
            '<a href="www.url.com#tag">tag</a>')
        #raute aber kein text
        self.assertEqual(
            self.filter('Lorem # ipsum'),
            'Lorem # ipsum')
        #mehrere '#' in einem wort
        self.assertEqual(
            self.filter('#Lorem#Ipsum'),
            '<a href="%sLorem">#Lorem</a>#Ipsum' % url)
        #hash mit Zahlen
        self.assertEqual(
            self.filter('#v1 and #v1b2'),
            '<a href="%sv1">#v1</a> and <a href="%sv1b2">#v1b2</a>' % (url, url))
        #hash mit underlines
        self.assertEqual(
            self.filter('This is a #hash_tag'),
            'This is a <a href="%shash_tag">#hash_tag</a>' % url)
        #hash with .
        self.assertEqual(
            self.filter('#hash.tag'),
            '<a href="%shash">#hash</a>.tag' % url)
