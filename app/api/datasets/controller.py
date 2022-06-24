from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from .dto import DatasetDto

api = DatasetDto.api
dataset=DatasetDto.dataset
data_resp=DatasetDto.data_resp
data_list_resp=DatasetDto.data_list_resp

@api.route('/<int:dataset_id>')
class Dataset(Resource):
    @api.doc('get specific dataset',responses={
        200:('Success',data_resp),
        400:'Invalid Dataset ID',
    })
    @jwt_required()
    def get(self,dataset_id):
        """ get specific dataset"""
        return
    
    @api.doc("Delete a specific dataset",responses={
        200:"Success"})
    @jwt_required()
    def delete(self,dataset_id):
        """ Delete a specific dataset"""
        return

    @api.doc("Update a specific dataset",responses={200:"Success"})
    @api.expect(dataset)
    @jwt_required()
    def put(self,dataset_id):
        """ Update a specific dataset"""
        data = request.get_json()
        return

@api.route("/user/<int:user_id>")
class DatasetList(Resource):
    @api.doc("Get all datasets of a specific user",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self,user_id):
        """
        Get all datasets of a specific user"""
        return


    @api.doc("Create a new dataset",responses={200:"Success",500:"Internal Server Error"})
    @api.expect(dataset)
    @jwt_required()
    def post(self,user_id):
        """
        Create a new dataset"""
        data = request.get_json()
        return