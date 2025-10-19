import logging
from functools import wraps
import time
import os
from loguru import logger


# Configuração básica do logger (pode ajustar o formato e o nível conforme necessário)
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(message)s'
# )
# logging.basicConfig(
#     filename='logs/pipeline.log',
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(message)s'
# )
# logger = logging.getLogger(__name__)

# Garante que a pasta de logs existe
os.makedirs("logs", exist_ok=True)

# Remove os handlers padrão
logger.remove()

# Adiciona handler que grava no arquivo
logger.add(
    "logs/pipeline.log",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    rotation="10 MB",
    enqueue=True
)

# Adiciona handler que mostra no terminal (apenas para tempo de execução)
logger.add(
    lambda msg: print(msg, end=""),
    level="INFO",
    format="{time:HH:mm:ss} | {level} | {message}",
    filter=lambda record: "executada em" in record["message"]
)


def log_decorator(func):
    """Decorator para logar chamadas de funções, resultados e exceções."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função original
    return wrapper




# Decorador de medida de tempo
def time_measure_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Função '{func.__name__}' executada em {end_time - start_time:.4f} segundos")
        return result
    return wrapper
