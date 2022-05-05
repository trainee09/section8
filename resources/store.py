from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        
        if store:
            return store.json()

        return {'message':"Store not found."}, 404
    
    def post(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return {'message':"Store already exists."}
        
        store = StoreModel(name)

        store.save_to_db()
        return store.json()

    def delete (self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()
            return {'message':"Store has been deleted."}

        return {'message':"Store does not exist."}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}