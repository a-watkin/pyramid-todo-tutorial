from pyramid.config import Configurator

def main(global_config, **settings):
    """Returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    # implicitly importing from routes.py?
    # you can do .routes because __init__ is in the same module.
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()