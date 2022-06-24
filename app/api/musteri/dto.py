from flask_restx import Namespace, fields


class MusteriDto:
    api = Namespace('client', description="Client related operations")

    restorant = api.model("Restorant object", [{
        "name": fields.String,
        "id": fields.Integer
    }])
