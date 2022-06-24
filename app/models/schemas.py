from app import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "name", "username", "joined_date", "roleId")


class RestorantSchema(ma.Schema):
    class Meta:
        fields = ("id", "name");