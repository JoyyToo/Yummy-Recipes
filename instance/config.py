# /instance/config.py

import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


class StagingConfig(Config):
    """Configurations for Staging."""
    DEVELOPMENT = True
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
