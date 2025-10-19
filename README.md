# ETL Project

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para consolidar e processar dados de vendas KPIs.

## Estrutura do Projeto

```
ETL/
├── src/
│   ├── pipeline.py
│   ├── etl/
│   │   ├── pipeline_calcular_kpi_de_vendas_consolidado.py
│   │   └── …
│   └── requirements.txt
└── README.md
```

## Configuração do Ambiente

1. Crie o ambiente virtual:
   ```bash
   python -m venv .venv
   ```

2. Ative o ambiente:
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

Rode o pipeline principal:

```bash
python src/pipeline.py
```

Ao final, o terminal exibirá:

```
Pipeline executado com sucesso
```

## Tecnologias

- Python 3.12+
- Loguru (para logs)
- Pandas
- tzdata
