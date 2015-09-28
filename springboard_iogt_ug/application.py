from ConfigParser import ConfigParser

from pyramid.config import Configurator

import pkg_resources


def main(global_config, **settings):

    cp = ConfigParser()
    cp.readfp(pkg_resources.resource_stream('springboard', 'defaults.ini'))
    defaults = dict(cp.items('springboard:pyramid'))
    filters = [
        'recent_pages = springboard_iogt.filters:recent_pages',
        'category_dict = springboard_iogt.filters:category_dict',
        'content_section = springboard_iogt.filters:content_section'
    ]
    defaults['jinja2.filters'] += '\n%s' % '\n'.join(filters)
    defaults.update(settings)

    config = Configurator(settings=defaults)

    config.include('springboard_iogt.config')
    config.configure_celery(global_config['__file__'])
    config.override_asset(
        to_override='springboard_iogt:templates/',
        override_with='springboard_iogt_ug:templates/')
    config.add_static_view(
        'static', 'springboard_iogt_ug:static', cache_max_age=3600)
    config.add_translation_dirs('springboard_iogt_ug:locale/')

    return config.make_wsgi_app()
