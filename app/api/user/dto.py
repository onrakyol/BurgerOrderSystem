from flask_restx import Namespace, fields

class UserDto:

    api = Namespace("user", description="User related operations")

    user = api.model("User object", {
        "email":fields.String,
        "name":fields.String,
        "username":fields.String,
        "joined_date":fields.DateTime,
        "roleId":fields.Integer
    })

    data_resp = api.model("User data response",{
        "status":fields.Boolean,
        "message":fields.String,
        "user":fields.Nested(user)
    })
