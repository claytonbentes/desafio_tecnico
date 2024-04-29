import pandas as pd

dataframe = pd.read_csv('atendimentos.csv', index_col=0)

class Atendimentos:
    def __init__(self, id, nome, nascimento, cns, cpf, unidade, data_atendimento, condicao_saude):
        self.ID = id
        self.Nome = nome
        self.Nascimento = nascimento
        self.CNS = cns
        self.CPF = cpf
        self.UNIDADE = unidade
        self.data_atendimento = data_atendimento
        self.condicao_saude = condicao_saude


    def __repr__(self):
        return f"Atendimento(ID={self.ID}, Nome={self.Nome}, Nascimento={self.Nascimento}, CNS={self.CNS}, CPF={self.CPF}, UNIDADE={self.UNIDADE}, data_atendimento={self.data_atendimento}, condicao_saude={self.condicao_saude})"