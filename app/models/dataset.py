from app import db

Column = db.Column
Model = db.Model
Integer = db.Integer
String = db.String
ForeignKey = db.ForeignKey


class Restorant(Model):
    __tablename__ = "restorants"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    menuId = Column(Integer)


class MenuContent(Model):
    __tablename__ = "menuContent"
    id = Column(Integer, primary_key=True)
    restorantId = Column(Integer)
    name = Column(String)
    price = Column(String)
    description = Column(String)


class Order(Model):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    restorantId = Column(Integer)
    orderid = Column(Integer)
    userid = Column(Integer)
    status = Column(db.String(10))