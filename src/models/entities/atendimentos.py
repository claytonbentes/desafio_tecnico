from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

class Atendimentos(Base):
    __tablename__ = "atendimentos"
    ID = Column(Integer,primary_key=True)
    Nome = Column(String)
    Nascimento = Column(String)
    CNS = Column(Integer)
    CPF = Column(String)
    UNIDADE = Column(String)
    data_atendimento = Column(String)
    condicao_saude = Column(String)


    def __repr__(self):
        return f"Atendimento(ID={self.ID}, Nome={self.Nome}, Nascimento={self.Nascimento}, CNS={self.CNS}, CPF={self.CPF}, UNIDADE={self.UNIDADE}, data_atendimento={self.data_atendimento}, condicao_saude={self.condicao_saude})"