from flask import Flask

from rest_flask.core.api import api as api_blueprint
from rest_flask.core.main import main as main_blueprint
from rest_flask.extensions import init_extensions


class RestFlask(Flask):
    def __init__(self, import_name, static_path=None, static_url_path=None, static_folder='static',
                 template_folder='templates', instance_path=None, instance_relative_config=False):
        super(RestFlask, self).__init__(import_name, static_path, static_url_path, static_folder, template_folder,
                                        instance_path, instance_relative_config)

        self.register_blueprint(main_blueprint)
        self.register_blueprint(api_blueprint)

    def init_extensions(self):
        init_extensions(self)

        # init default admin
        import rest_flask.core.accounts.admin
        import rest_flask.core.api.admin

    def register_core_blueprint(self, api=None, api_url_prefix='/api',
                                main=None, main_url_prefix='/main'):
        from rest_flask.core.api import api as api_blueprint
        from rest_flask.core.main import main as main_blueprint

        api_blueprint = api or api_blueprint
        main_blueprint = main or main_blueprint

        self.register_blueprint(api_blueprint, url_prefix=api_url_prefix)
        self.register_blueprint(main_blueprint, url_prefix=main_url_prefix)
