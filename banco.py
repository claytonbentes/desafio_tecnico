import sqlite3
import pandas as pd
from datetime import datetime

# Definindo a função padronizar_data
def padronizar_data(data):
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
            try:
                # Tenta converter para o formato com microssegundos
                data_formatada = datetime.strptime(data, '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d')
                return data_formatada
            except ValueError:
                # Se não conseguir converter, retorna a data original
                return data
            
data = pd.read_csv('atendimentos.csv', index_col=0)
df = pd.DataFrame(data)


data_atendimento = df['data_atendimento']

# Aplicar a função padronizar_data em toda a coluna 'data'
data_atendimento = data_atendimento.apply(padronizar_data)

#df['data_atendimento_formatada'] = data_atendimento

# Criar uma conexão com o banco de dados SQLite
#conn = sqlite3.connect('atendimentos.db')

# Inserir o DataFrame no banco de dados SQLite
#df.to_sql('atendimentos', conn, if_exists='replace', index=False)

# Fechar a conexão
#conn.close()

