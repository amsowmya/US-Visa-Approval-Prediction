import sys
from us_visa.logger import logging
from us_visa.exception import USvisaException

logging.info("test file")

try:
    1/"10"
    
except Exception as e:
    logging.error(e)
    raise USvisaException(e, sys)
