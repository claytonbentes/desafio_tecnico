from datetime import datetime
from typing import List
from functools import reduce
from src.models.entities.atendimentos import Atendimentos, dataframe

class AtendimentosRepository:
    def padronizar_data(self, data: str) -> datetime:
        if data:
            try:
                # Tenta converter a data para o formato 'YYYY-mm-dd'
                data_formatada = datetime.strptime(data, '%Y-%m-%d').strftime('%Y-%m-%d')
                return data_formatada
            except ValueError:
                try:
                    # Tenta converter para outro formato (caso necessário)
                    data_formatada = datetime.strptime(data, '%d %B, %Y').strftime('%Y-%m-%d')
                    return data_formatada
                except ValueError:
                        # Tenta converter para o formato com microssegundos
                    data_formatada = datetime.strptime(data, '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d')
                    return data_formatada
        else:
            return False
            
    def get_atendimento_by_filter(self, data_atendimento: str, unidade:str, condicao:str) -> List[Atendimentos]:
        df = dataframe
        
        df['data_atendimento_formato'] = df['data_atendimento'].apply(lambda x: self.padronizar_data(x))
        
        data_formatada = self.padronizar_data(data_atendimento)
        
        
        
        condicoes = []

        # Adiciona os filtros opcionais à lista de condições
        if data_formatada:
            condicoes.append(df['data_atendimento_formato'] == data_formatada)
        if unidade:
            condicoes.append(df['UNIDADE'] == unidade)
        if condicao:
            condicoes.append(df['condicao_saude'] == condicao)


        # Aplica os filtros em conjunto usando o operador &
        if condicoes:
            df_filtrado = df[reduce(lambda x, y: x & y, condicoes)]
        else:
            df_filtrado = df.copy()
        
        df_filtrado = df_filtrado.drop(columns='data_atendimento_formato')
        
        return df_filtrado