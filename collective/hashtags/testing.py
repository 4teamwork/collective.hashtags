from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.testing import login
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import TEST_USER_NAME
from zope.configuration import xmlconfig


class HashTagsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML

        import collective.hashtags
        xmlconfig.file('configure.zcml',
                       collective.hashtags,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        login(portal, TEST_USER_NAME)
        # Install into Plone site using portal_setup
        applyProfile(portal, 'collective.hashtags:default')


HASH_TAGS_FIXTURE = HashTagsLayer()
HASH_TAGS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(HASH_TAGS_FIXTURE,), name="collective.hashtags:integration")
HASH_TAGS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(HASH_TAGS_FIXTURE,), name="collective.hashtags:functional")
