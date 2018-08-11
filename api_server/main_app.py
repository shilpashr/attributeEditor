#!/usr/bin/env python3
import os
import connexion

from api_server import encoder

def create_app():
    """ Connexion application intialization """
    app = connexion.App(__name__, specification_dir='./config/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('api_config.yaml', arguments={'title': 'Attribute Editor'})

    return app.app


# This is required for running app on local development env
if __name__ == '__main__':
    app = create_app()
    app.run(port=3001)