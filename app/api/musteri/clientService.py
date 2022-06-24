from flask import current_app
from app.models.dataset import Restorant
from app.models.dataset import MenuContent
from app.models.dataset import Order
from app.utils import err_resp, internal_err_resp, message
from app import db

class ClientService:
    @staticmethod
    def get_all_restorants():
        """
        Get all restorants
        """
        if not (restorants := Restorant.query.all()):
            return err_resp("No restorant defined", 404)
        try:
            response = []
            for restorant in restorants:
                restorant_info = {"id": restorant.id, "name": restorant.name}
                response.append(restorant_info)
            resp = message(True, response)
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_restorant_menu(id):
        """
        Get restaurant menu with id
        """
        if not (content := MenuContent.query.filter_by(restorantId=id)):
            return err_resp("No restorant defined", 404)

        try:
            response = []
            for element in content:
                resp_element = {"Hamburger": element.name, "Fiyat": element.price, "Açıklama": element.description}
                response.append(resp_element)
            resp = message(True, response)
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def create_order(order):
        """
        Create order
        """
        restorantId = order.get('restorantId')
        orderID = order.get('orderID')        
        userid = order.get('userid')        
        status = "NEW"
        try:
            new_order = Order(restorantId=restorantId, orderid=orderID, userid=userid, status=status)
            db.session.add(new_order)
            db.session.commit()
            resp = message('True', 'Kayıt başarılı')
            return resp, 200  # 200 dönüyor

        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def monitor_all_order_of_client(id):
        """
        Show all orders of client
        """
        if not (orders := Order.query.filter_by(userid=id)):
            return err_resp("No restorant defined", 404)

        try:
            response = []
            for order in orders:
                element = MenuContent.query.filter_by(restorantId= order.restorantId, id=order.orderid).first()
                restorant_info = {"id": order.orderid, "restorantId": order.restorantId, "status": order.status,
                                  "name": element.name, "description": element.description}
                response.append(restorant_info)
            resp = message(True, response)
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def cancel_order(order_id):
        """
        Cancel order
        """
        try:
            Order.query.filter_by(id=order_id, status="NEW").update({"status":"CANCEL"})
            db.session.commit()
            return message(True, "Dataset updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()