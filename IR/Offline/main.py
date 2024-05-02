from Helper.ORM import fetch_records
from Pipeline.index.index import Index
from datetime import datetime

start = datetime.now()
records = fetch_records('dataset1.db', 10)
index = Index(records)
index.save()
end = datetime.now()

print(index.create_dataframe())
print(end - start)

# index = Index.load()
# print(index.create_dataframe())
