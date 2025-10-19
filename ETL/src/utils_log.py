import logging
from functools import wraps

# Configuração básica do logger (pode ajustar o formato e o nível conforme necessário)
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(message)s'
# )
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

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
