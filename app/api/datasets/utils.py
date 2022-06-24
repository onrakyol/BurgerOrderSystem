def load_data(dataset_db_obj):
    from app.models.schemas import DatasetSchema
    dataset_schema = DatasetSchema()
    data = dataset_schema.dump(dataset_db_obj)
    return data