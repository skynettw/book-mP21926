from pymongo import MongoClient
conn = MongoClient()
db = conn.news
collection = db.nkust
find_cmd = {'date':{'$in':['2020-02-04', '2020-02-19']}}
rows = collection.find(find_cmd)
if rows.count() > 0:
    for row in rows:
        print(row['title'])
else:
    print("找不到當天的新聞")
    