from .core import Alchemical as BaseAlchemical


class Alchemical(BaseAlchemical):
    """Create an Alchamical instance for a Flask application.

    :param app: the Flask application instance. If the application instance
                isn't provided here, the :func:`Alchemical.init_app` method
                must be called later to complete the initialization of the
                extension.
    """
    def __init__(self, app=None):
        super().__init__()
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Complete initialization of the Alchemical instance.

        :param app: the Flask application instace.
        """
        self.initialize(app.config['ALCHEMICAL_DATABASE_URI'],
                        binds=app.config.get('ALCHEMICAL_BINDS'))
