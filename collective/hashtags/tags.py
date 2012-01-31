from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from zope.interface import implements


class ITagsPortlet(IPortletDataProvider):
    """A portlet that displays all hashtags of the context.
    """


class Assignment(base.Assignment):
    """Portlet assignment.
    This is what is actually managed through the portlets UI and associated
    with columns.
    """
    implements(ITagsPortlet)

    def __init__(self):
        pass

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return "Tags Portlet"


class Renderer(base.Renderer):
    """Portlet renderer.
    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('tags.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        self.navroot_url = portal_state.navigation_root_url()

    @property
    def available(self):
        return len(self.tags()) > 0

    @memoize
    def tags(self):
        """Get a list of cs tags containing search url and tag name.
        """
        portal_url = getToolByName(self.context, 'portal_url').portal_url()
        search_url = '%s/search?Subject=' % portal_url
        return [{'url': search_url + tag,
                 'name': tag} for tag in self.context.Subject()]