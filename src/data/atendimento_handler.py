from src.models.repository.atendimentos_repository import AtendimentosRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.errors_type.http_not_found import HttpNotFound

class AtendimentoHandler:
    def __init__(self) -> None:
        self.__atendimentos_repository = AtendimentosRepository()

    def find_by_data_consulta(self, data_consulta: str) -> HttpResponse:
        # Não precisa mais extrair a data da consulta da requisição HTTP
        # data_consulta = http_request.param["data_consulta"]
        
        # Busca os atendimentos pela data da consulta
        atendimentos = self.__atendimentos_repository.get_atendimento_by_data(data_consulta)
        
        # Se nenhum atendimento for encontrado, retorna uma resposta de erro HttpNotFound
        if not atendimentos:
            raise HttpNotFound("Nenhum atendimento encontrado para a data de consulta")
        
        # Retorna uma lista de atendimentos encontrados
        atendimentos_info = []
        for atendimento in atendimentos:
            atendimentos_info.append({
                "id": atendimento.ID,
                "Nome": atendimento.Nome,
                "Nascimento": atendimento.Nascimento,
                "CNS": atendimento.CNS,
                "CPF": atendimento.CPF,
                "UNIDADE": atendimento.UNIDADE,
                "data_atendimento": atendimento.data_atendimento,
                "condicao_saude": atendimento.condicao_saude
            })

        return HttpResponse(
            body={"atendimentos": atendimentos_info},
            status_code=200
        )

