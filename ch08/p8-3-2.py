from pymongo import MongoClient
conn = MongoClient()
db = conn.news
collection = db.nkust
rows = collection.find({'date':'2020-02-04'})
if rows.count() > 0:
    for row in rows:
        print(row['title'])
else:
    print("找不到當天的新聞")
    