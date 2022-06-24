from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
import jwt

from .dto import RestorantDto
from .restorantService import RestorantService

api = RestorantDto.api


# As a restorant I want to
# Get all orders
@api.route("/getAllOrder/<int:restorant_id>")
class Client(Resource):
    @api.doc("get all previous orders of user", response={
        200: ("Success"),
        400: "Service not available",
    })
    @jwt_required()
    def get(self, restorant_id):
        try:
            return RestorantService.monitor_all_orders(restorant_id)
        except Exception as e:
            print("Error User:", e)

# Get detail of selected order
@api.route("/getOrderDetail/<int:order_id>")
class Client(Resource):
    @jwt_required()
    def get(self, order_id):
        try:
            return RestorantService.get_detail_of_order(order_id)
        except Exception as e:
            print("Error User:", e)

# Cancel the order
@api.route("/cancelOrder/<int:order_id>")
class Client(Resource):
    @jwt_required()
    def get(self, order_id):
        try:
            return RestorantService.cancel_order(order_id)
        except Exception as e:
            print("Error User:", e)


# Update the status of the order
@api.route("/updateContent/<int:selected_order_id>")
class Client(Resource):
    @jwt_required()
    def post(self, selected_order_id):
        try:
            statusObj = request.get_json()
            return RestorantService.update_status(statusObj.get('status'), selected_order_id)
        except Exception as e:
            print("Error User:", e)


# Get the content of the menu
@api.route("/getMenu/<int:restorant_id>")
class Client(Resource):
    @jwt_required()
    def get(self, restorant_id):
        try:
            return RestorantService.get_content_of_menu(restorant_id)
        except Exception as e:
            print("Error User:", e)


# Get the details of selected dish
@api.route("/getSelectedContent/<int:content_id>")
class Client(Resource):
    @jwt_required()
    def get(self, content_id):
        try:
            return RestorantService.get_detail_of_content(content_id)
        except Exception as e:
            print("Error User:", e)


# Update the content of the menu
@api.route("/updateSelectedContent/<int:content_id>")
class Client(Resource):
    @jwt_required()
    def post(self, content_id):
        try:
            content = request.get_json()
            return RestorantService.update_content(content_id, content)
        except Exception as e:
            print("Error User:", e)


# Add new element to the menu
@api.route("/addContent/<int:restorant_id>")
class Client(Resource):
    @jwt_required()
    def post(self, restorant_id):
        try:
            content = request.get_json()
            return RestorantService.add_menu_content(restorant_id, content)
        except Exception as e:
            print("Error User:", e)


# Delete any element of the menu
@api.route("/deleteContent/<int:content_id>")
class Client(Resource):
    @jwt_required()
    def post(self, content_id):
        try:
            # RESTORANT Validation
            return RestorantService.delete_menu_content(content_id)
        except Exception as e:
            print("Error User:", e)
