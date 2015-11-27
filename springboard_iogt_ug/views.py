from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from springboard.utils import ga_context
from springboard_iogt.views import IoGTViews, PERSONA_COOKIE_NAME, ONE_YEAR
from springboard_iogt.utils import (
    get_redirect_url)

PERSONAE = {'YOUTH_BOY', 'YOUTH_GIRL', 'FATHER', 'MOTHER'}


class UGIogtViews(IoGTViews):
    @ga_context(lambda context: {'dt': 'Selected Persona', })
    @view_config(route_name='select_persona')
    def select_persona(self):
        slug = self.request.matchdict['slug'].upper()
        if slug not in PERSONAE:
            raise HTTPNotFound

        # set cookie and redirect
        response = HTTPFound(location=get_redirect_url(self.request))
        response.set_cookie(PERSONA_COOKIE_NAME, value=slug, max_age=ONE_YEAR)

        # set persona dimension value on GA
        # NOTE: the persona dimension has to be configured with scope 'user'
        persona_dimension_id = self.settings.get('ga.persona_dimension_id')
        if persona_dimension_id:
            self.request.google_analytics[persona_dimension_id] = slug

        return response
