from urllib import urlencode
from pyramid import testing

from springboard.tests import SpringboardTestCase
from springboard_iogt_ug.application import main
from springboard_iogt.views import PERSONA_COOKIE_NAME


class TestUGIoGTViews(SpringboardTestCase):

    def setUp(self):
        self.workspace = self.mk_workspace()
        self.config = testing.setUp(settings={
            'unicore.repos_dir': self.working_dir,
            'unicore.content_repo_urls': self.workspace.working_dir,
            'iogt.content_section_url_overrides':
                '\nffl = http://za.ffl.qa-hub.unicore.io/'
                '\nebola = http://za.ebola.qa-hub.unicore.io/'
        })

    def tearDown(self):
        testing.tearDown()

    def test_select_persona(self):
        app = self.mk_app(self.workspace, main=main)
        next_url = 'http://localhost/page/1234/'
        querystring = urlencode({'next': next_url})

        response = app.get('/persona/youth_boy/?%s' % querystring)
        self.assertEqual(response.status_int, 302)
        self.assertEqual(response.location, next_url)
        cookie = response.headers.get('Set-Cookie', '')
        self.assertIn('%s=YOUTH_BOY;' % PERSONA_COOKIE_NAME, cookie)

        response = app.get('/persona/youth_girl/?%s' % querystring)
        self.assertEqual(response.status_int, 302)
        self.assertEqual(response.location, next_url)
        cookie = response.headers.get('Set-Cookie', '')
        self.assertIn('%s=YOUTH_GIRL;' % PERSONA_COOKIE_NAME, cookie)

        response = app.get('/persona/father/?%s' % querystring)
        self.assertEqual(response.status_int, 302)
        self.assertEqual(response.location, next_url)
        cookie = response.headers.get('Set-Cookie', '')
        self.assertIn('%s=FATHER;' % PERSONA_COOKIE_NAME, cookie)

        response = app.get('/persona/mother/?%s' % querystring)
        self.assertEqual(response.status_int, 302)
        self.assertEqual(response.location, next_url)
        cookie = response.headers.get('Set-Cookie', '')
        self.assertIn('%s=MOTHER;' % PERSONA_COOKIE_NAME, cookie)

        response = app.get('/persona/not-a-persona/', expect_errors=True)
        self.assertEqual(response.status_int, 404)
