#!/usr/bin/env LearnPythonNotes
# -----------------------------------------------------------------------------
import os
import csv
import json
from pprint import pprint
# import logging
# import math
# import random
# from datetime import datetime
# from datetime import date
# from datetime import time as tiempo
# import time as t
# import intertools

# --------------------------- Function Definitions ----------------------------
def get_files(folder):
    """List all files in root current working directory."""
    for item in os.listdir(folder):
        full_item = os.path.join(folder, item)

        if os.path.isfile(full_item):
            yield full_item
        elif os.path.isdir(full_item):
            yield from get_files(full_item)

# ------------------------------- Main Function -------------------------------
def main():
    """Main program function calls."""
    print("\n--------------- Program Started! ---------------\n")
    # List Files on file system, from current working directory including
    # subdirectories
    folder = os.getcwd()  # Get current working directory
    yield_gen = get_files(folder) # Create a list of files
    print(type(yield_gen))

    #TODO: Can we use a List Comprehension here?
    for i in yield_gen:
        print(i)

# ------------------------ Main Application Entry Point -----------------------
if __name__ == "__main__":
    main()

# This section will be removed once the functions are created
    # TODO: Put file io sections into their own funciton
    #       - Text file io function
    #       - Binary file io funciton
    #       - CSV file io funciton
    #       - JSON file io function
    # ---------------------------- Text File IO -------------------------------
    print(f"\n---------- Text IO ----------")
    # Text Files:
    # - Plain Text
    # - XML
    # - JSON
    # - Source Code

    ## List to write out to myfile.
    txt_to_myfile = ["Plain Text", "XML", "JSON", "Source Code"]

    ## See help on opening files
    # help(open)
    """With the "With" statement, you get better syntax and exceptions handling.

    "The with statement simplifies exception handling by encapsulating common
    preparation and cleanup tasks."

    In addition, it will automatically close the file. The with statement provides
    a way for ensuring that a clean-up is always used.:"""
    try:
        ## Open a text file for writting, appending, or read-only
        # Specify full path instead of relative path.
        TXT_FILE = 'txt_file_io.txt'
        DATA_DIR = '\\data'
        FULL_PATH_CUR_DIR = os.getcwd()  # Returns current working directory
        os.chdir(FULL_PATH_CUR_DIR + DATA_DIR) # cd /change/to/data/dir
        FULL_PATH_DATA_DIR = os.getcwd()  # Returns full path to data directory

        if os.path.isdir(FULL_PATH_DATA_DIR):  # Return True if directory exists
            # Appends full path to file
            TXT_FILE = os.path.join(FULL_PATH_DATA_DIR, TXT_FILE)

        ## Open file mode:
        #  'w' open for writing, truncating the file first
        #  '+' open a disk file for updating (reading and writing)
        #  'a' open for writing, appending to the end of the file if it exists
        #  'r' read only
        with open(TXT_FILE, mode="r+", encoding="utf-8") as myfile:
            # Verify file exists prior to reading/writting
            if os.path.isfile(TXT_FILE):  # Return True if file exists
                print(f"\nFile ==> {myfile.name} was created!")

            ## Append Mode only - cannot read file.
            # with open(cur_dir + txt_file, mode="a", encoding="utf-8") as myfile:
            # with open(cur_dir + txt_file, mode="a+", encoding="utf-8") as myfile:
            # File Info
            print("Name of the file:", myfile.name.split('\\')[-1])
            print("Mode of the file:", myfile.mode)
            print("Mode of the file:", myfile.encoding)
            print("Tell the byte at which the file cursor is:", myfile.tell())
            # Write to file
            for line in txt_to_myfile:
                myfile.write(line + "\n")
                ## Another way to write list items to file
                # print(line, file=myfile)
                # print(10 * "=", file=myfile)
            # Read file
            print("Tell the byte at which the file cursor is:", myfile.tell())
            myfile.seek(0)
            print("Tell the byte at which the file cursor is:", myfile.tell())

            # Test file existence try block
            if os.path.exists(myfile.name):
                print(f"The file {myfile.name} exists!")
                # myfile.close() # Uncomment to test IO exceptions
                # os.remove(myfile.name) # Uncomment to test IO exceptions
            else:
                print(f"The text file does not exist!")

            print(myfile.read())  # Causes an error if file opened for append only, except with "a+"
            print("Tell the byte at which the file cursor is:", myfile.tell())
            # myfile.close() # Uncomment to test IO exceptions
            #print("File closed?", myfile.closed)
    except (FileNotFoundError, IOError) as e:
        print(f"{myfile.name} not found or not readable!\n{e}")
    except Exception as e2:
        print(f"{myfile.name} was closed or deleted!\n{e2}")
        # Write error to file_io_err.log

    finally:  # The finally always gets executed.
        # Close file
        # myfile.close()

        print("File closed?", myfile.closed)
    # ---------------------------- Binary File IO -------------------------------
    print(f"---------- Binary IO ----------")
    # Binary Files:
    # - Compiled code
    # - App data
    # - Media files
    #   ~ images
    #   ~ audio
    #   ~ video

    BIN_FILE = 'bin_file_io.txt'
    DATA_DIR = '\\data'
    # From current working directory change to data dir
    os.chdir('..' + DATA_DIR)
    binary_file = open(BIN_FILE, "wb+")
    # File Info
    print("Name of the file: ", binary_file.name)
    print("Closed or not : ", binary_file.closed)
    print("Opening mode : ", binary_file.mode)
    # print("Softspace flag : ", binary_file.softspace)

    for i in range(5, 0, -1):
        # Write to binary file
        text = "\n" + str(i) + ". " + "Hello 123"
        encoded = text.encode("utf-8")
        binary_file.write(encoded)

    # Read file
    binary_file.seek(0)
    binary_data = binary_file.read()
    print("binary:", binary_data)
    text = binary_data.decode("utf-8")
    print("Decoded data:", text)
    # print("Softspace flag : ", binary_file.softspace)

    # Close opend file
    binary_file.close()

#     # ---------------------------- CSV File IO -------------------------------
#     print(f"---------- CSV File IO ----------")
#     mycsv_file = os.getcwd() + "\\data\\Google Stock Market Data - google_stock_data.csv"
#     # # File object "csv_read_file"
#     # # Reading a CSV file without CSV module
#     # csv_read_file = open(mycsv_file, 'r')
#     #
#     # # Basic read to validate file
#     # for line in csv_read_file:
#     #     print(line)
#     #
#     # # Builds a list with ea. line as an element
#     # lines = [line for line in open(mycsv_file)]
#     # print(f"{lines[1]}")
#     #
#     # # Strip leading and trailing spaces
#     # print(f"{lines[2].strip()}")
#     # # Strip leading and trailing spaces. Split ea. csv into an element in the list
#     # print(f"{lines[2].strip().split(',')}")
#     # # Build a list again
#     # dataset = [line.strip().split(',') for line in open(mycsv_file)]
#     # print(f"{line[-1]}")
#
#     # Now reading a CSV file using the CSV module
#     # Print dir(csv) to see what functions and classes the module contains.
#     # Let's use reader and writer functions
#     # Specify a newline keyword argument to account for newline, or/both carriage return
#     with open(mycsv_file, newline='') as csv_read_file:
#         reader = csv.reader(csv_read_file)
#
#         header = next(reader)  # The first line is the header
#         data = [row for row in reader]  # Read the remaining data into the list "data"
#
#         print(f"Header print:\n {header}")
#         print(f"Data print:\n {data[0]}")
#
#         # Read data and convert to appropriate data types (Does not work!!!)
#         # data = [] # Clear "data" list
#         # for row in reader:
#         #     # row = [Date, Open, High, Low, Close, Volume, Adj. Close]
#         #     date = datetime.strptime(row[0], '%m/%d/%Y')
#         #     open_price = float(row[1]) # 'open' is a builtin fuction
#         #     high = float(row[2])
#         #     low = float(row[3])
#         #     close = float(row[4])
#         #     volume = int(row[5])
#         #     adj_close = float(row[6])
#         #
#         #     # Converts data types
#         #     data.append([date, open_price, high, low, close, volume, adj_close])
#         #     print(f"Data print again:\n {data[0]}")
#
#     # Let's calc Stock Return = % change in price
#     # Common time frames:
#     #   >> Daily
#     #   >> Weekly
#     #   >> Monthly
#     #   >> Quarterly
#     #   >> Annual
#
#     # Compute Daily returns using the "closing price" on a given date
#     mycsv_returns = os.getcwd() + "\\data\\goog_returns.csv"
#     with open(mycsv_returns, 'w') as csv_out_file:
#         writer = csv.writer(csv_out_file)
#         writer.writerow(["Date", "Return"])
#
#         # Using "data" list from above
#         for i in range(len(data) - 1):
#             todays_row = data[i]
#             todays_date = todays_row[0]
#             todays_price = todays_row[-1]
#             yesterdays_row = data[i + 1]
#             yesterdays_price = yesterdays_row[-1]
#
#             daily_return = (float(todays_price) - float(yesterdays_price)) / float(yesterdays_price)
#             # formatted_date = todays_date.strftime('%m/%d/%Y')
#             writer.writerow([todays_date, daily_return])
#
#     print(f"\n---------- JSON IO ----------")
#
#     """
#     JSON Key Methods
#     ----------------
#     json.load(f):       Load JSON data from file (or file-like object)
#
#     json.loads(s):      Load JSON data from string
#
#     json.dump(j, f):    Write JSON object to file (or file-like object)
#
#     json.dump(j):       Output JSON object as string
#     """
#     json_file = open('data/movies.json', 'r', encoding='utf-8')
#     movie = json.load(json_file)
#     json_file.close()
#
#     pprint(f"Printing the JSON data: \n{movie}")
#     pprint(f"Printing dictionary key \'title\': {movie['title']}")
#
#     print(f"\nJSON file type: {type(movie)}")
#
#     # JSON formatted 'value'
#     value = """
#         {
#             "title" : "Tron: Legacy",
#             "composer" : "Daft Punk",
#             "actors" : null,
#             "won_oscar" : false
#         }
#         """
#
#     # Convert to a properly formatted Python dictionary
#     # Note: null => none and false => False
#     # Since all characters are ascii there is not need to worry about encoding
#     tron = json.loads(value)
#     pprint(f"Print json => LearnPythonNotes dict: \n{tron}")
#     pprint(f"Print dictionary key value: {tron['title']}")
#
#     # Convert movies.json file to a valid Python text string and store in a
#     # database for instance use json.dumps(pyDict)
#     # If there are ascii characters use json.dumps(pyDict, ensure_ascii=False)
#     pprint(json.dumps(movie))
#
#     # Convert a dictionary to a JSON formatted file
#     movie2 = {}
#     movie2['title'] = "Minority Report"
#     movie2['director'] = "Steven Spielberg"
#     movie2['composer'] = "John Williams"
#     movie2['actors'] = ["Tom Cruise", "Colin Farrell",
#                         "Samantha Morton", "Max von Sydow"]
#     movie2['is_awesome'] = True
#     movie2['budget'] = 102000000
#     movie2['cinematographer'] = "Janusz Kami\\u044ski"
#
#     # Write to file and preserver non-ascii characters
#     json_file2 = open('data/movie2.json', 'w', encoding='utf-8')
#     json.dump(movie2, json_file2, ensure_ascii=False)
#     json_file2.close()
#
#     with open('data/movie2.json', 'r', encoding='utf-8') as json_file2:
#         movie2_dict = json.load(json_file2)
#         json_file2.close()
#
#     pprint(f"Printing the JSON data: \n{movie2_dict}")