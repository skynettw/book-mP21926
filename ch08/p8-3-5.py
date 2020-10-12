from pymongo import MongoClient
conn = MongoClient()
db = conn.news
collection = db.nkust
find_cmd = {"title":{'$regex' : "高科大"}}
rows = collection.find(find_cmd)
if rows.count() > 0:
    for row in rows:
        print(row['date'], end=":")
        print(row['title'])
else:
    print("找不到標題中含有「高科大」的新聞")
    