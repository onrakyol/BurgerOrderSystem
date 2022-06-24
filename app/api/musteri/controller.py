from flask import request
from flask_restx import Resource
import jwt
from flask_jwt_extended import jwt_required
from app.models.user import User
from app.utils import err_resp

from .dto import MusteriDto
from .clientService import ClientService

api = MusteriDto.api
restorantBundle = MusteriDto.restorant


# As a client I want to
# Get all restorants input - output

@api.route("/Restaurants")
class Client(Resource):
    @api.doc("get all restaurants", response={
        200: ("Success"),
        400: "Service not available",
    })
    @jwt_required()
    def get(self):        
        try:
            return ClientService.get_all_restorants()                            
        except Exception as e:
            print("Error User:", e)

 # Get menu of selected restorant
 
@api.route("/Menu/<int:restorantId>")
class Client(Resource):
    @api.doc("Get menu of selected restaurants", response={
        200: ("Success"),
        400: "Service not available",
    })    
    @jwt_required()
    def get(self, restorantId):
        if User.roleId == 1:
            return err_resp("You are not authorized", 401)
        else:
            try:
                return ClientService.get_restorant_menu(restorantId)
            except Exception as e:
                print("Error User:", e)

# Create order
@api.route("/createOrder")
class Client(Resource):
    @api.doc("get all restorants", response={
        200: ("Success"),
        400: "Service not available",
    })
    @jwt_required()
    def post(self):
        order = request.get_json()
        return ClientService.create_order(order)


# Watch order details
@api.route("/watchOrders")
class Client(Resource):
    @api.doc("get all restorants", response={
        200: ("Success"),
        400: "Service not available",
    })
    
    def post(self):
        order = request.get_json()
        return ClientService.create_order(order)
# Monitoring list of the orders

@api.route("/getAllOrder/<int:userid>")
class Client(Resource):
    @api.doc("get all previous orders of user", response={
        200: ("Success"),
        400: "Service not available",
    })    
    def get(self, userid):
        print("userid", userid)
        try:
            return ClientService.monitor_all_order_of_client(userid)
        except Exception as e:
            print("Error User:", e)

# Cancel the order
@api.route("/cancelOrder/<int:orderid>")
class Client(Resource):
    @api.doc("cancel selected order", response={
        200: ("Success"),
        400: "Service not available",
    })
    def get(self, orderid):
        try:
            return ClientService.cancel_order(orderid)
        except Exception as e:
            print("Error User:", e)