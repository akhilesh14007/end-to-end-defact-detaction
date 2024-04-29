from Defact_detaction.logger import logging
from Defact_detaction.exception import AppException
import sys

try:
    a=3/"s"
except Exception as e:
    raise AppException(e,sys)