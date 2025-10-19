from etl import pipeline_calcular_kpi_de_vendas_consolidado
#import logging
from loguru import logger


#logs usando loguru ao inves de logging
logger.add("logs/pipeline.log")
logger.info("Iniciando pipeline de ETL")
logger.debug("Pipeline de ETL iniciada")
logger.warning("Pipeline de ETL iniciada")
logger.error("Pipeline de ETL iniciada")
logger.critical("Pipeline de ETL iniciada")

#pipeline de ETL
pasta: str = 'data'
formato_de_saida: list = ["csv", "parquet"]
pipeline_calcular_kpi_de_vendas_consolidado(pasta, formato_de_saida)
