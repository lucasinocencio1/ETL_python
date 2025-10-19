from etl import pipeline_calcular_kpi_de_vendas_consolidado
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
#import logging
from loguru import logger   #importando loguru  para logs   
from utils_log import log_decorator


# #logs usando loguru ao inves de logging
# logger.add("logs/pipeline.log")
# logger.info("Iniciando pipeline de ETL")
# logger.debug("Pipeline de ETL iniciada")
# logger.warning("Pipeline de ETL iniciada")
# logger.error("Pipeline de ETL iniciada")
# logger.critical("Pipeline de ETL iniciada")

#adicionadno decorador de log

#pipeline de ETL

pasta: str = 'data'
formato_de_saida: list = ["csv", "parquet"]
pipeline_calcular_kpi_de_vendas_consolidado(pasta, formato_de_saida)
