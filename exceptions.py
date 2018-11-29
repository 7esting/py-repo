#!/usr/bin/env PyRefCodeNotes
"""
Python Exception Object:
    - Provides a description of the error
    - Provides a traceback and line number(s) where error occurred

Exception Clauses
-----------------

try:
    # Runs first
    < code >
except:
    # Runs if exception occurs in try block
    < code >
else:
    # Runs if try block *succeeds*
    < code >
finally:
    # Runs *always*
    < code >
"""
# -------------------------- Python3 - Exceptions -----------------------------
import os
import logging
import time

print(f"\nSource Root directory: {os.getcwd()}\n")
# Create logger
LOG_FILE = "logs/file_io_err.log"
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time requred."""
    start_time = time.time()
    try:
        f = open(path, mode='rb') # Default is to open txt file in read mode
        # Close file before read to show how multiple exceptions can be addressed
        #f.close()
        data = f.read()
        return data
    except FileNotFoundError as err1:
        logger.error(err1)
        raise # Also display error to user
    except ValueError as err2:
        logger.critical(err2)
        pass # Skip past 'finally' block from this point & continue w/ program
    else:
        f.close() # Only executes if try block succeeds
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required to read {file} =  {time}".format(file=path, time=dt))

print(f"\nSource Root directory: {os.getcwd()}\n")
#
data = read_file_timed("C://Users//hmaldonado//Desktop//dress_boots_jeans_4.jpg")
