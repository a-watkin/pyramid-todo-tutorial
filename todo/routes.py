# Must literally be called 'includeme'
def includeme(config):
    """Include these routes within the application."""
    config.add_route('hello', '/')