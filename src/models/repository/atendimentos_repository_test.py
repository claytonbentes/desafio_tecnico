from src.models.settings.connection import db_connection_handler
from .atendimentos_repository import AtendimentosRepository
from datetime import datetime
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Nao necessario")
def test_get_atendimento_by_data():

    atend_data_str = "2023-12-152222"
    try:
        atend_data = datetime.strptime(atend_data_str, "%Y-%m-%d")
    except Exception:
        return 'Data nao pode ser convertida'
    
    atends_repository = AtendimentosRepository()
    response = atends_repository.get_atendimento_by_data(atend_data)

