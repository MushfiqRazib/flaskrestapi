from flask import request
from flask import jsonify
from flask_restx import Resource
from ..util.dto import LogDto
from ..service.computation_service import ComputationContext, FibonacciStrategy
from ..service.logs_service import save_new_log, get_all_logs, get_a_log

api = LogDto.api
_logs = LogDto.logs


@api.route('/<int:number>')
@api.param('number', 'The fib number')
@api.response(200, 'Combinations of fib number is successfully generated.')
class FibonacciController(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument'}, 
			 params={ 'number': 'Specify the number associated with the fibonacci number' })

    def get(self, number):
        """Get fib number all possible combinations"""
        fb = FibonacciStrategy()
        combinations = fb.compute_algorithm(number)
        #context = ComputationContext(FibonacciStrategy)
        #combinations = context.do_computation(number)

        # saving log information to DB
        if combinations is not None:
            logdata = {
                'logger': "TAG:FIB LOGGING",
                'level': "INFO",
                'msg': "FIB REQUEST - GET /fib/" + str(number) + " FIB RESPONSE - successfull, Response Code: 200"
            }        
        else:
            logdata = {
                'logger': "TAG:FIB LOGGING",
                'level': "ERROR",
                'msg': "FIB REQUEST - GET /fib/" + str(number) + " FIB RESPONSE - failed, Response Code: 400"
            }
        
        #save_new_log(data=logdata)

        return jsonify(combinations)