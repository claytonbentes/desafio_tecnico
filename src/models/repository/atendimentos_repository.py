from datetime import datetime
from typing import List
import pandas as pd
from sqlalchemy import or_, func, cast, Date
from src.models.settings.connection import db_connection_handler
from src.models.entities.atendimentos import Atendimentos
import pdb

class AtendimentosRepository:
    def padronizar_data(self, data: str) -> datetime:
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
            
    def get_atendimento_by_data(self, data_atendimento: str) -> List[Atendimentos]:
        # Padronizar a data usando a função padronizar_data
        data_padronizada = self.padronizar_data(data_atendimento)
        
        # Verificar se a data foi padronizada corretamente
        if data_padronizada is None:
            # Lidar com o erro de data inválida
            # Por exemplo, lançar uma exceção ou retornar uma lista vazia
            raise ValueError("Data inválida. Certifique-se de que a data está no formato 'YYYY-mm-dd'.")

        data = pd.read_csv('atendimentos.csv', index_col=0)
        df = pd.DataFrame(data)

        data_atendimento = df['data_atendimento']

        df['data_atendimento'] = data_atendimento.apply(lambda x: self.padronizar_data(x))

        # Aplicar a função padronizar_data em toda a coluna 'data'
        #data_atendimento = data_atendimento.apply(padronizar_data)
        df_filtrado = df.loc[df['data_atendimento'] == str(data_padronizada)]
        
        print(df_filtrado)
        
        return df_filtrado

        # with db_connection_handler as database:
        #     atend = (database.session
        #     .query(Atendimentos)
        #     .filter(or_(
        #         cast(Atendimentos.data_atendimento, Date) == data_padronizada,  # Para datas no formato 'YYYY-mm-dd'
        #      func.strftime('%Y-%m-%d', Atendimentos.data_atendimento) == data_padronizada,  # Outro formato se necessário
        #      func.strftime('%d %B, %Y', Atendimentos.data_atendimento) == data_padronizada  # Outro formato se necessário
        #     ))
        #     .all())
        #     print(atend)
        #     return atend
