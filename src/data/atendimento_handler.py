from src.models.repository.atendimentos_repository import AtendimentosRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.errors_type.http_not_found import HttpNotFound

class AtendimentoHandler:
    def __init__(self) -> None:
        self.__atendimentos_repository = AtendimentosRepository()

    def filtro_atendimento(self, data_atendimento: str, unidade:str, condicao:str) -> HttpResponse:

        try:
            # Busca os atendimentos pela data da consulta/unidade/condicao de saude
            atendimentos = self.__atendimentos_repository.get_atendimento_by_filter(data_atendimento, unidade, condicao)
        except:
            return HttpResponse(
            body={"error": "Dados passados sao invalidos"},
            status_code=400
            )
        # Se nenhum atendimento for encontrado, retorna uma resposta de erro HttpNotFound
        if atendimentos.empty:
            return HttpResponse(
                body={"error": "Dado nao existente"},
                status_code=404
            )

        atendimentos_info=atendimentos.to_dict(orient="records")
        
        return HttpResponse(    
            body={"atendimentos": atendimentos_info},
            status_code=200
        )

