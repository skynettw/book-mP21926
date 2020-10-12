from pymongo import MongoClient
conn = MongoClient()
db = conn.news
collection = db.nkust
find_cmd = {'date':{'$gte':'2020-02-01'}}
rows = collection.find(find_cmd)
if rows.count() > 0:
    for row in rows:
        print(row['date'], end=":")
        print(row['title'])
else:
    print("找不到2020-02-01之後的新聞")
    