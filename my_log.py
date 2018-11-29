import os
import logging
import math

dir(logging) # See what logging module provides
# Create and configure logger
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DIR = '/opt/'
LOG_FILE = "/opt/Lumberjack.log"
# If "level" is set to error, you will only see "error" and "critical" log messages. 
# W/o filemode, defautl is to append to log
logging.basicConfig(filename = LOG_FILE, level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')
#logging.basicConfig(filename = LOG_FILE, level = logging.DEBUG, filemode = 'w')

#if not os.path.exists('/opt/') or not os.path.isfile('/opt/teto.log'):
#    msg = '%s log file does not exist', log_file
#    logger = logging.getlogger(__name__).error(msg)
#else:
#    logger = logging.getlogger(__name__).info('%s log file exists!')

logger = logging.getLogger(__name__)

if os.path.exists(LOG_DIR) and os.path.isdir(LOG_DIR) and os.path.isfile(LOG_FILE):
    print(f"Log was written to {LOG_FILE}")

# Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to devide by zero?")
logger.critical("The entire internet is down!!!")

# Test
def quadratric_formula(a, b, c):
	"""Return the solution to the equation ax^2 + bx c = 0."""
	logger.info("quadratric_formula({0}, {1}, {2})".format(a, b, c))
	
	# Compute the discriminant
	logger.debug("# Compute the discriminant")
	disc = b**2 - 4*a*c
	
	# Compute the two roots
	logger.debug("# Compute the tow roots")
	root1 = (-b + math.sqrt(disc)) / (2*a)
	root2 = (-b - math.sqrt(disc)) / (2*a)
	
	# Return the roots
	logger.debug("# Return the roots")
	return (root1, root2)

roots = quadratric_formula(1, 0, -4)
print(roots)