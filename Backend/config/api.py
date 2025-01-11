from flask import Flask
from flask_smorest import Api

def configure_api_settings(app: Flask) -> Api:
    app.config.update(
        PROPAGATE_EXCEPTIONS=True,
        API_TITLE='Bird API',
        API_VERSION='v1',
        OPENAPI_VERSION='3.0.3',
        OPENAPI_URL_PREFIX='/',
        OPENAPI_SWAGGER_UI_PATH='/swagger-ui',
        OPENAPI_SWAGGER_UI_URL='https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    )
    return Api(app)