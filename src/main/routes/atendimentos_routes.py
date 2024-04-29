from flask import Flask, request, jsonify
from flask_restx import  Resource, fields
from flask_restx import Api
from src.data.atendimento_handler import AtendimentoHandler
from flask_restx import Namespace, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Atendimento API',
    description='Api para pegar dados através de um CSV',
)
api = Namespace('Atendimento')

atendimento = api.model('Atendimento', {
    'data_atendimento': fields.String(required=True, description='Data de atendimento'),
    'unidade': fields.String(required=True, description='Unidade de atendimento'),
    'condicao_saude': fields.String(required=True, description='condição de saude de paciente'),
})

@api.route('/')
class AtendimentoResource(Resource):
    @api.doc('get_atendimento')
    @api.param('data_atendimento', 'Data de atendimento', required=False)
    @api.param('unidade', 'Unidade de atendimento', required=False)
    @api.param('condicao_saude', 'condição de saude de paciente', required=False)
    def get(self):
        '''Listar os atendimentos de acordo com os filtros passados'''
        data = request.args.get('data_atendimento') or False
        unidade = request.args.get('unidade') or False
        condicao = request.args.get('condicao_saude') or False

        atend_handler = AtendimentoHandler()
        http_response = atend_handler.filtro_atendimento(data, unidade, condicao)

        return (http_response.body), http_response.status_code