# Analise Educação no BR - Projeto final NTBD

Esse repositório é referente a fase final do projeto da matéria de Novas Tecnologias de Banco de Dados da UFSCar Campus Sorocaba.

O objetivo do projeto é criar um DataWarehouse para realizar a análise entre a relação entre os recursos presentes em escolas e o desempenho dos alunos no ENEM.

Para a criação do DataWarehouse, houve uma modelagem inicial, estudo da base de dados juntamente com o mapeamento dos dados. Após essa primeira fase de planejamento, a fase de implementação buscou realizar o ETL e o tratamento dos dados.

## Modelagem do DW
O diagrama da modelagem está disponível [aqui](https://drive.google.com/file/d/1v3JhTrsaudnxh600vjUrhRTPMmGeZ0u6/view?usp=sharing)

## Fontes de dados
### Resultados do ENEM
A base de microdados do ENEM apresenta informações de dados básicos, dados da escola, dados de prova, redação, e do questionário socioeconômico de todos os participantes do ENEM. A base é disponibilizada publicamente pelo INEP, com os dados separados por ano. 
É disponibilizado um arquivo csv com os dados, além de anexos com informações adicionais. No anexo do ano de 2022, pode ser encontrado o dicionário de dados do csv, detalhando o esquema do arquivo csv.

Acessível em:  [Enem — Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira | Inep (www.gov.br)](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)

### Censo escolar - Microdados
A base de microdados do censo escolar apresenta dados de localização, infraestrutura e matrículas de escolas.
A base é disponibilizada publicamente pelo INEP, com os dados separados por ano. 
É disponibilizado um arquivo csv com os dados, além de anexos com informações adicionais. No anexo do ano de 2022, pode ser encontrado o dicionário de dados do csv, detalhando o esquema do arquivo csv, além de pontuando quais colunas estão disponíveis na base de dados de cada ano.

 Acessível em: [Censo Escolar — Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira | Inep (www.gov.br)](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar)

 ### Mapeamento dos dados
 A partir das duas bases de dados utilizadas, foi criado um novo dicionário como mapeamento, mostrando a origem dos dados e qual será sua representação dentro do DataWarehouse

 Acessível em: [Planilha de mapeamento dos dados](https://docs.google.com/spreadsheets/d/1C6DYyT1f2gPf8APttbNckL7-wUL60_EB0ew3pkrP3Vo/edit?usp=sharing)


## Autores
Jean Wylmer Flores Mendoza

Pedro Henrique Mendes