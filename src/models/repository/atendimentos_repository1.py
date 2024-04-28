from src.models.settings.connection import db_connection_handler
from src.models.entities.atendimentos import Atendimentos
from typing import List
from datetime import datetime



class AtendimentosRepository:
    def get_atendimento_by_data(self, data_atendimento: datetime) -> List[Atendimentos]:
        with db_connection_handler as database:
                atend = (database.session
                         .query(Atendimentos)
                         .filter(Atendimentos.data_atendimento==data_atendimento)
                         .all())
                
                if not atend:
                    return None

                return atend
        