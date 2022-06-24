import imp
import unittest
import os
from flask import current_app
from app import create_app
from config import basedir


class TestDevelopmentConfig(unittest.TestCase):
    def test_app_is_development(self):
        app = create_app('development')

        self.assertFalse(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(current_app is None)
        self.assertFalse(app.config['SQLALCHEMY_DATABASE_URI'] ==
        "sqlite:///" + os.path.join(basedir, "data-dev.sqlite"))


class TestProductionConfig(unittest.TestCase):
    def test_app_is_production(self):
        app = create_app('production')

        self.assertTrue(app.config['DEBUG'] is False)