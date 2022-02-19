# :syringe: COVID-19 in Espírito Santo

An analysis on the covid cases in the state of Espírito Santo in Brazil. A mini project to learn varios technologies and practices. The project consists of the following tasks:

- **Webscraping**: obtaining data from the [state covid panel](https://coronavirus.es.gov.br/painel-covid-19-es).
- **Date cleanup**: treating data and cleaning up noise. 
- **Loading data**: storing data in an PostgreSQL database.
- **BI Visualization**: dashboards to better analyse data patterns and information. 
- **Scheduler**: fetch data daily and treats information to be added to database.
- **Deploy**: add project to a heroku server


## :hammer: Requirements

In order to run this project, you need to download packages in the requirements.txt file. It also uses functions from my scraper utils package, you can download it from [this repository](https://github.com/beamaia/scraper_utils). 

## :bar-chart: Data 

COVID-19 cases in the state of Espírito Santo ,updated regularly at 17:00 (GMT -3:00). The data dictionary can be found in this [link](https://bi.s3.es.gov.br/imunizacao/Dicion%C3%A1rio%20de%20Dados.pdf). There are over 3 mi cases, starting from 2020. There are 45 attributes (columns) in the csv file, some of which were added later on. 

Headers:
    - DataNotificacao;
    - DataCadastro;
    - DataDiagnostico;
    - DataColeta_RT_PCR;
    - DataColetaTesteRapido;
    - DataColetaSorologia;
    - DataColetaSorologiaIGG;
    - DataEncerramento;
    - DataObito;
    - Classificacao;
    - Evolucao;
    - CriterioConfirmacao;
    - StatusNotificacao;
    - Municipio;
    - Bairro;
    - FaixaEtaria;
    - IdadeNaDataNotificacao;
    - Sexo;
    - RacaCor;
    - Escolaridade;
    - Gestante;
    - Febre;
    - DificuldadeRespiratoria;
    - Tosse;Coriza;
    - DorGarganta;
    - Diarreia;
    - Cefaleia;
    - ComorbidadePulmao;
    - ComorbidadeCardio;
    - ComorbidadeRenal;
    - ComorbidadeDiabetes;
    - ComorbidadeTabagismo;
    - ComorbidadeObesidade;
    - FicouInternado;
    - ViagemBrasil;
    - ViagemInternacional;
    - ProfissionalSaude;
    - PossuiDeficiencia;
    - MoradorDeRua;
    - ResultadoRT_PCR;
    - ResultadoTesteRapido;
    - ResultadoSorologia;
    - ResultadoSorologia_IGG;
    - TipoTesteRapido
