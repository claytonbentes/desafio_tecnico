# API Atendimentos

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

Esta API faz pesquisas por filtros de data_atendimento, condicao_saude e unidade, a partir de uma base de dados atendimentos.csv

## Rodando a API

Com o Docker instalado no computador e rodando, o que você precisará é apenas pegar o arquivo docker-compose.yml, que está na raiz do projeto, abrir o terminal, caminhar até onde o arquivo docker-compose.yml está, após isso digitar o comando: 

```bash
docker-compose up
```

## API Endpoints
A API fornece os seguintes endpoints:

```markdown
GET http://localhost:8001/api/v1/atendimentos - Mostra todos os atendimentos.
```

você pode passar os filtros na URL, como por exemplo: 

```markdown
http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01
http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01&condicao_saude=hipertensao
```

Além disso, foi adicionado o Swagger no projeto para documentação interativa da API, está disponível em:

```markdown
http://localhost:8001/swagger
```

## Contato

[![](https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/claytonbentes/)
[![](https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white)](mailto:claytonjhony.bentes@gmail.com)
