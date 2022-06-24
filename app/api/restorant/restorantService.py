from flask import current_app
from app.models.dataset import Restorant
from app.models.dataset import MenuContent
from app.models.dataset import Order
from app.utils import err_resp, internal_err_resp, message
from app.utils import generate_unique_id
from app import db


class RestorantService:
    @staticmethod
    def monitor_all_orders(restorant_id):
        if not (orders := Order.query.filter_by(restorantId=restorant_id, status="NEW")):
            return err_resp("No restorant defined", 404)

        try:
            response = []
            for order in orders:
                order_info = {"id": order.id, "orderid": order.orderid, "restorantId": order.restorantId,
                              "status": order.status}
                response.append(order_info)
            resp = message(True, response)
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    # Get detail of selected order
    @staticmethod
    def get_detail_of_order(selected_order_id):
        if not (order := Order.query.filter_by(id=selected_order_id).first()):
            return err_resp("No order found", 404)
        try:
            restorant = Restorant.query.filter_by(id=order.restorantId).first();
            selected_content = MenuContent.query.filter_by(restorantId=order.restorantId, id=order.orderid).first()
            response = {"Status": order.status, "Restorant": restorant.name,
                        "Menu": selected_content.name, "Price": selected_content.price,
                        "Description": selected_content.description}
            resp = message(True, response)
            return resp, 200
        except Exception as e:
            print("Error Restorant:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    # Cancel the order
    @staticmethod
    def cancel_order(selected_order_id):
        try:
            Order.query.filter_by(id=selected_order_id, status="NEW").update({"status": "CANCEL"})
            db.session.commit()
            return message(True, "Dataset updated successfully")
        except Exception as e:
            print("Error Restorant:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    # Update the status of the order
    @staticmethod
    def update_status(status, selected_order_id):
        try:
            Order.query.filter_by(id=selected_order_id).update({"status": status})
            db.session.commit()
            return message(True, "Dataset updated successfully")
        except Exception as e:
            print("Error Restorant:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    # Get the content of the menu
    @staticmethod
    def get_content_of_menu(restorant_id):
        if not (contents := MenuContent.query.filter_by(restorantId=restorant_id)):
            return err_resp("No restorant defined", 404)
        try:
            response = []
            for content in contents:
                content_info = {"id": content.id, "Hamburger": content.name, "Fiyat": content.price, "Açıklama": content.description}
                response.append(content_info)
            resp = message(True, response)
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    # Get the details of selected dish
    @staticmethod
    def get_detail_of_content(content_id):
        if not (content := MenuContent.query.filter_by(id=content_id).first()):
            return err_resp("No content defined", 404)
        try:
            restorant = Restorant.query.filter_by(id=content.restorantId).first();
            response = {"Name": content.name, "Restorant": restorant.name, "Price": content.price,
                        "Description": content.description}
            resp = message(True, response)
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    # Update the content of the menu
    @staticmethod
    def update_content(content_id, content):
        try:
            MenuContent.query.filter_by(id=content_id).update({"name":content.get('name'), "price": content.get('price'),
                                                               "description": content.get('description')})
            db.session.commit()
            return message(True, "Dataset updated successfully")
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()
    # Add new element to the menu
    @staticmethod
    def add_menu_content(restorant_id, content):
        try:
            uniqueid = generate_unique_id()
            new_content = MenuContent(id=uniqueid,
                                      name=content.get('name'),
                                      restorantId=restorant_id,
                                      price=content.get('price'),
                                      description=content.get('description')
                                      )
            db.session.add(new_content)
            db.session.commit()
            return message(True, "Content insertion successfully")
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()
    # Update the details of the selected dish

    # Delete any element of the menu
    @staticmethod
    def delete_menu_content(content_id):
        try:
            cont_to_update = MenuContent.query.filter_by(id=content_id).first()
            MenuContent.query.filter_by(id=content_id).update({"restorantId": cont_to_update.restorantId*-1})
            db.session.commit()
            return message(True, "Dataset updated successfully")
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()
