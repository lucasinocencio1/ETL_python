import pandas as pd
import os
import glob
from pathlib import Path


# uma funcao de extract que le e consolida os json
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    """
    Função que extrai os dados de um arquivo json e consolida em um DataFrame
    Args: 
        pasta: str
        pasta onde esta os arquivos json
    Returns:
        df_total: pd.DataFrame
        DataFrame com os dados consolidados
    """
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True) #sem index e concatena os dataframes
    return df_total

# uma funcao que extrai os dados do DataFrame e calcula o KPI de total de vendas

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Função que cria métricas de negocio
    """
    df["Total"] = df["Quantidade"] * df["Venda"]
    df["juros"] = df["Quantidade"] * df["Venda"] * 0.05 #juros de 5%
    return df

# def carregar_dados(df: pd.DataFrame, format_saida: list):
#     """
#     parametro que vai ser ou "csv" ou "parquet" ou "os dois"
#     """
#     for formato in format_saida:
#         if formato == 'csv':
#             df.to_csv("dados.csv", index=False)
#         if formato == 'parquet':
#             df.to_parquet("dados.parquet", index=False)


def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    Função que carrega os dados em csv ou parquet e cria pastas output/csv e output/parquet
    """
    output_dir =  Path("output")
    (output_dir / "csv").mkdir(parents=True, exist_ok=True)
    (output_dir / "parquet").mkdir(parents=True, exist_ok=True)
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv(output_dir / "csv" / "dados.csv", index=False)
            print(f"Dados carregados em csv com sucesso")
        elif formato == 'parquet':
            df.to_parquet(output_dir / "parquet" / "dados.parquet", index=False)
            print(f"Dados carregados em parquet com sucesso")


def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    """
    Pipeline principal que executa todo o processo ETL
    """
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)
print("Pipeline executado com sucesso") #prova terminal
