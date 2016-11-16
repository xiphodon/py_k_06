import pymongo

# 使用mongo数据库持久化数据

# 文件路径
path = "./words.txt"

# 获得数据库连接（本地地址，端口号）
client = pymongo.MongoClient("localhost", 27017)
# 连接数据库（若不存在则创建）
first_db = client["first_db"]
# 连接数据库中的表（若不存在则创建）
tab_01 = first_db["tab_01"]


def saveDataToDB(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            data = {
                "index": index,
                "line": line,
                "line_len": len(line.split())
            }
            tab_01.insert_one(data)


def readDataFromDB():
    for item in tab_01.find():
        print(item)

    for item in tab_01.find({"line_len":0}):
        print(item["index"])

    # $lt,$gt,$lte,$gte,$nt 分别为 <,>,<=,>=,!=
    # 长度大于30的行
    for item in tab_01.find({"line_len":{"$gt":30}}):
        print(item["line"])

if __name__ == "__main__":
    # saveDataToDB(path)
    readDataFromDB()
