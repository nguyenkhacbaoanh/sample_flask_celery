from flask_restplus import Namespace, fields, Resource
from flask import request
import uuid
import json



api = Namespace('demo', description='demo flask')
para = api.model('para', {
    'queue': fields.String(),
    'num1': fields.Integer(),
    'num2': fields.Integer()
})
res = api.model('res', {
    'uuid': fields.String()
})

a = api.model('a', {
    'res': fields.Integer()
})
@api.route('/add')
@api.expect(para)
class Add(Resource):
    @api.marshal_with(res)
    def post(self):
        data = json.loads(request.data)
        print(data)
        if data["queue"] == "w1":
            from app.tasks.one.add_1 import add
        elif data["queue"] == "w2":
            from app.tasks.two.add_2 import add
        res = {
            "uuid":add.delay(data["num1"],data["num2"])
        }
        return res

@api.route('/mul')
@api.expect(para)
class Mul(Resource):
    @api.marshal_with(res)
    def post(self):
        data = json.loads(request.data)
        if data["queue"] == "w1":
            from app.tasks.one.mul_1 import mul
        elif data["queue"] == "w2":
            from app.tasks.two.mul_2 import mul
        res = {
            "uuid":mul.delay(data["num1"],data["num2"])
        }
        return res

@api.route('/uuid')
@api.expect(res)
class Uuid(Resource):
    @api.marshal_with(a)
    def post(self):
        data = json.loads(request.data)
        res_ = data['uuid']
        from celery.result import AsyncResult
        s = AsyncResult(res_)
        r = {
            "res": s.get()
        }
        return r