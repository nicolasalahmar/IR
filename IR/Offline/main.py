from Helper.ORM import fetch_records
from Pipeline.index.index import create_index
from datetime import datetime


start = datetime.now()
records = fetch_records('dataset1.db', 100)
index = create_index(records)
end = datetime.now()

print(index)
print(end-start)
