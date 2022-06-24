from flask_restx import Namespace, fields


class RestorantDto:
    api = Namespace('admin', description="Restourant user related operations")

    restorant = api.model("Restorant object", [{
        "name": fields.String,
        "id": fields.Integer
    }])