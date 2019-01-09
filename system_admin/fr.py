# ----------- Import Packages, and/or Modules: Classes, & Functions -----------
import os
import datetime
import subprocess
import re
import logging

# --------------------------- Function Definitions ---------------------------
# Count total lines in file
def file_line_count(p_file) -> "Return the total number of lines in file.":
    """Return the total number of lines in file."""
    with open(p_file,'r') as file:
        line_count = 0
        for line in file:
            line_count += 1
        return p_file, line_count

# ------------------------------- Main Function -------------------------------

## Main
def main():
    """
    All functions are called in main.
    inputs: none
    returns: none
    """
    # Input and output files
    INPUT_FILE = 'ar2d-2018.txt'
    OUTPUT_FILE = 'out_ar2d-2018.txt'
    SCRUBBED_FILE = 'ar2d-2018.txt'
    # bkup_yyyy-mm-dd_ar2d-2018.txt
    BACKUP_INPUT_FILE = 'BKUP_' +datetime.datetime.today().strftime('%Y-%m-%d') + '_' + INPUT_FILE

    # Create and configure logger
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_DIR = 'system_admin'
    LOG_FILE = "long_lines_txt.log"
    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format=LOG_FORMAT, filemode='w')
    logger = logging.getLogger(__name__)

    if os.path.exists(LOG_DIR) and os.path.isdir(LOG_DIR) and os.path.isfile(LOG_FILE):
        print(f"Log was written to {LOG_FILE}")

    # data = []
    # with open('/tmp/test.txt','r') as f:
    #     data=''.join(f.readlines())
    #
    # m=re.search(r'^(&.*!)\s*?\n',data,re.S | re.M) #find line that starts with '&' and ends with '!'
    # if m: print m.group(1)

    # ## This block find last word where we can pull from line
    # # split at 'unknown number of spaces as separator'
    # line_list = line.split()
    # #print(line_list)
    # end_indx = 0 # Initialize
    # if line.find('SANCDVT') != -1:
    #     end_indx = line_list.index('SANCDVT') + 1
    #     print(f"{''.join(map(str, line_list[:end_indx]))}")

    # 1. Find line with error "SANCDVT"
    # 2. Split line at column 286
    # 3. Pad rest of line with +195 to total 481 chars
    # Check if input file has 'SANCDVT' ERROR. If not, exit
    ERROR_COUNT = 0
    ERROR_FLAG = False                                                      
    with open(INPUT_FILE) as infile_ck:
        for line in infile_ck:
            if line.find('SANCDVT') != -1:
                ERROR_COUNT += 1
                ERROR_FLAG = True
    infile_ck.close()

    if ERROR_FLAG:
        SCRUB_FILE_FLAG = True
        logger.warning("%s file has errors and needs to be scrubbed.", infile_ck.name)
        # Backup input file if it has errors: cp ar2d-2018.txt bkup-yyyymmdd_ar2d-2018.txt
        # cp INPUT_FILE BKUP-yyyymmdd_INPUT_FILE
        cmd = 'copy "%s" "%s"' % (INPUT_FILE, BACKUP_INPUT_FILE)
        status = subprocess.call(cmd, shell=True)
    else:
        SCRUB_FILE_FLAG = False
        logger.info("%s file has no errors!", infile_ck.name)

    if SCRUB_FILE_FLAG:
        print(f"\nNumber of lines in {file_line_count(INPUT_FILE)}")
        logger.info("Number of lines in %s", file_line_count(INPUT_FILE))

        with open(OUTPUT_FILE, "w") as outfile:
            with open(INPUT_FILE, "r") as infile:
                for line in infile.readlines():
                    end_indx = 0
                    if line.find('SANCDVT') != -1:
                        if not line:
                            break
                        else:
                            #print(f"Found SANCDVT, writing padded line to outfile. {line.find('SANCDVT')}")
                            end_indx = line.find('SANCDVT') + 7
                            outfile.write('{:480}'.format(line[:end_indx].strip()) + '\n')
                            logger.warning("Error from PL/SQL package SANCDVT found!")
                    else:
                        if not line:
                            break
                        else:
                            #print(f"SANCDVT not found, writing existing line to outfile.")
                            outfile.write('{:480}'.format(line.strip()) + '\n')
        if infile.closed and outfile.closed:
            print(f"\nIO Files: {infile.name} and {outfile.name} are closed.")
        else:
            infile.close()
            outfile.close()

        print(f"\nNumber of lines in {file_line_count(OUTPUT_FILE)}")
        logger.info("Number of lines in %s", file_line_count(OUTPUT_FILE))
        # Rename OUTPUT_FILE to SCRUBBED_FILE <==> INPUT_FILE
        os.remove(INPUT_FILE)
        os.rename(OUTPUT_FILE, SCRUBBED_FILE)

# ------------------------ Main Application Entry Point -----------------------
if __name__ == '__main__':
    main()
