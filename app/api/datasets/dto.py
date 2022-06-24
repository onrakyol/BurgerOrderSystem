from flask_restx import Namespace,fields

class DatasetDto:
    api = Namespace('datasets', description='Datasets related operations')
    dataset = api.model('dataset', {
        'id':fields.Integer,
        'name':fields.String,
        'filepath':fields.String,
        'filename':fields.String,
        'userid':fields.Integer,
    })


    data_resp = api.model('data_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'dataset':fields.Nested(dataset)
    })

    data_list_resp = api.model('data_list_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'datasets':fields.List(fields.Nested(dataset))})