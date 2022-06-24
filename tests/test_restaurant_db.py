from app import db
from app.models.dataset import Restorant
from app.models.schemas import RestorantSchema

from tests.utils.base import BaseTestCase

class TestDatasetModel(BaseTestCase):
    def test_create_restaurant(self):
        d = Restorant(id=1, name='test1', menuId="1")
        db.session.add(d)
        db.session.commit()
        self.assertTrue(d.id > 0)

    def test_update_restorant(self):
        d = Restorant(id=2, name='test2', menuId="2")
        db.session.add(d)
        db.session.commit()
        d.name = 'test4'
        db.session.commit()
        self.assertTrue(d.name == 'test4')

    def test_delete_restorant(self):
        d = Restorant(id=3, name='test3', menuId="3")
        db.session.add(d)
        db.session.commit()
        db.session.delete(d)
        db.session.commit()
        res =  Restorant.query.get(d.id)
        self.assertTrue(res is None)

    def test_restoran_schema(self):
        # d = Dataset(user_id=1)
        d = Restorant(id=5, name='test5')
        d_dump = RestorantSchema().dump(d)
        self.assertTrue(d_dump['name'] == 'test5')