"""
BSON /ˈbiːsən/ is a computer data interchange format used mainly as a data storage
and network transfer format in the MongoDB database. It is a binary form for
representing simple data structures, associative arrays (called objects or
documents in MongoDB), and various data types of specific interest to MongoDB.
The name "BSON" is based on the term JSON and stands for "Binary JSON".

Compared to JSON, BSON is designed to be efficient both in storage space and
scan-speed. Large elements in a BSON document are prefixed with a length field
to facilitate scanning. In some cases, BSON will use more space than JSON due
to the length prefixes and explicit array indices.
"""

# ----------- Import Packages, and/or Modules: Classes, & Functions -----------
#from pymongo import MongoClient
import pymongo
from config_settings import db_config as db_conn
import datetime, pytz

# --------------------------- Function Definitions ----------------------------

def time_stamp():
    """Returns timestamp in ISO-8601 form '2016-11-16T14:31:18.130822-08:00'
    Requires import datetime, pytz"""
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
    #return utc_now.isoformat()
    return pst_now.isoformat()

# ------------------------- MongoDB Connection Str ----------------------------
# conn_str = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn_str)

# Create database 'the_small_bookstore' in MongoDB
# db = client.the_small_bookstore

client = pymongo.MongoClient(db_conn.DATABASE_CONFIG['MONGO_URI'])
dbname = db_conn.DATABASE_CONFIG['MONGO_DB1']
db = client[dbname]

# db.<collection-name>.count()
print(f"db.books.count: {db.books.count()}")

if db.books.count() >= 0:
    # Drop 'books' collection
    db.books.drop()
    print(f"Books collection has been dropped! {db.books.count()}")

# Create or insert dict. into collection only if the dict. doesn't already exist!
# Adds dictionaries/documents in 'books' collection
if db.books.count() == 0:
    print("Inserting data")
    # insert some data...
    r = db.books.insert_one({'title': 'Harry Potter', 'isbn': '73738584947384'})
    print(r, type(r))
    r = db.books.insert_one({'title': 'The forth book', 'isbn': '181819884728473'})

    print(r.inserted_id)
    db.books.insert_one({'title': 'Playboy', 'Issue': 'December 2018'})
else:
    print("Books already inserted, skipping")

# Drop 'magazines' collection
db.magazines.drop()

# Create or insert dict. into collection only if the dict. doesn't already exist!
# Adds dictionaries/documents in 'magazines' collection
if db.magazines.count() < 3:
    print("Inserting data")
    mag = db.magazines.insert_one({'title': 'Time', 'Issue': '11/26/2018'})
    print(mag, type(mag))
    mag = db.magazines.insert_one({'title': 'Playboy', 'Issue': 'December 2018'})
    print(mag, type(mag))
    mag = db.magazines.insert_one({'title': 'Soccer America', 'Issue': 'November 2018'})
    print(mag, type(mag))
else:
    print("Magazines already on shelf.")

# book = db.books.find_one({'isbn': '73738584947384'})
# print(book, type(book))
# book['favorited_by'] = []
# book['favorited_by'].append(100)
# db.books.update({'_id': book.get('_id')}, book)
# book = db.books.find_one({'isbn': '73738584947384'})
# print(book)

db.books.update({'isbn': '181819884728473'}, {'$addToSet': {'favorited_by': 120}})
book = db.books.find_one({'isbn': '181819884728473'})
print(book)

# Delete magazine from books shelf, be very cautious, use if condition or you
# may delete all documents in the collection.
# Retrieve a magazine
magazine = db.books.find_one({'title': 'Playboy', 'Issue': 'December 2018'})
print(f"To be deleted: {magazine} size of object: {len(magazine)}")
if magazine != None:
    print(f"Deleting from book collection {magazine}!")
    db.books.remove(magazine)

magazine = db.books.find_one({'title': 'Time', 'Issue': '11/26/2018'})
print(f"To be deleted: {magazine}")
if magazine != None:
    print(f"Deleting from book collection {magazine}!")
    db.books.remove(magazine)

# Retrieve a magazine
magazine = db.magazines.find_one({'title': 'Playboy', 'Issue': 'December 2018'})
print(magazine)

# Python dictionary
my_dictionary = {
    "key 1": "Value 1",
    "key 2": "Value 2",
    "decimal": 100,
    "boolean": False,
    "list": [1, 2, 3],
    "dict": {
        "child key 1": "value 1",
        "child key 2": "value 2"
    }
}

# Python dictionary
Movies = {"title": "Minority Report",
			"director": "Steven Spielberg",
			"composer": "John Williams",
			"actors": ["Tom Curise", "Colin Farrell", "Samantha Morton", "Max von Sydow"],
			"is_awesome": True, "budget": 102000000, "cinematographer": "Janusz Kami\\u044ski"}

# Create or insert dict. into collection only if the dict. doesn't already exist!
if (db.dictionary_collection_doc.count() < 1 and
        db.dictionary_collection_movie.count() < 1):
    # Create 'dictionary_collection_doc' collection and insert dictionary/doc
    doc = db.dictionary_collection_doc.insert_one(my_dictionary)

    doc = db.dictionary_collection_doc.find_one({'dict': '*'})
    print(f"Global Search: {doc}")
    doc = db.dictionary_collection_doc.find_one({'key 1': 'Value 1'})
    print(f"Specific string search: {doc}")

    # Create 'dictionary_collection_movie' collection and insert dictionary/doc
    movie_doc = db.dictionary_collection_movie.insert_one(Movies)
else:
    print("Records already in 'business' database.")
    #doc = db_business.dictionary_collection_doc.find_one({'dict': '*'})
    doc_query = {"dict": {"$regex": "^.*.$"}} # Search in sub-dict (not working)
    #doc_query = {"key 1": {"$regex": "^V.*1$" }}
    doc_cursor = db.dictionary_collection_doc.find(doc_query)
    print(f"Global Search: {type(doc_cursor)}")
    for doc in doc_cursor:
        print(f"Global Search: {doc}")

    doc = db.dictionary_collection_doc.find_one({'key 1': 'Value 1'})
    print(f"Specific string search: {type(doc)}")

# Drop 'library_members' database by dropping all of it's collections
# db.dictionary_collection_doc.drop()
# db.dictionary_collection_movie.drop()

dictList = [ {'FirstName': 'Michael', 'LastName': 'Kirk', 'SSID': '224567', "Date Added": time_stamp()},
{'FirstName': 'Linda', 'LastName': 'Matthew', 'SSID': '123456', "Date Added": time_stamp()},
{'FirstName': 'Sandra', 'LastName': 'Parkin', 'SSID': '123456', "Date Added": time_stamp()},
{'FirstName': 'Bob', 'LastName': 'Henry', 'SSID': '666666', "Date Added": time_stamp()},
{'FirstName': 'Silvia', 'LastName': 'Perkin', 'SSID': '676767', "Date Added": time_stamp()}]

# Create a second database 'library_members'
dbname = db_conn.DATABASE_CONFIG['MONGO_DB2']
db = client[dbname]

if db.members.count() >= 0:
    # Drop 'members' collection
    db.members.drop()
    print(f"Members collection has been dropped! {db.members.count()}")

# Use for loop to read and insert from a dictionary
for member in dictList:
    r = db.members.insert_one(member)


# -------------------------------- End of File --------------------------------