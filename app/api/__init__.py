from flask_restx import Api
from flask import Blueprint

from .user.controller import api as user_ns
from .musteri.controller import api as muster_ns
from .restorant.controller import api as restorant_ns

api_bp = Blueprint("client", __name__)
apidef = Api(api_bp, version="1.0", title="BURGERZILLA", description="API")

apidef.add_namespace(muster_ns)
apidef.add_namespace(restorant_ns)
apidef.add_namespace(user_ns)