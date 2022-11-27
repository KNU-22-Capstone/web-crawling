import firebase_connect
import web_crawling
import rds_connect
import py_json

# firebase DB 연결 #
# firebase_connect.firebase_write('의류',web_crawling.run())
# firebase_connect.firebase_fix('의류',web_crawling.run())
# for i in web_crawling.run():
#     print(i)
#     print(json.dumps(i, indent="\t"))


# 데이터 불러오기
# dic_list = web_crawling.run()
dic_list = firebase_connect.firebase_read('의류')

# json 파일 저장 #
py_json.json_write_dict("save_db.json", dic_list)

# RDS DB 연결 #
rds_connect.run(dic_list)


