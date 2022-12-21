import add_color_tag
import py_json
import web_crawling
import my_db_connecter

import json

# firebase DB 연결 #
# firebase_connect.firebase_write('의류',web_crawling.run())
# firebase_connect.firebase_fix('의류',web_crawling.run())
# for i in web_crawling.run():
#     print(i)
#     print(json.dumps(i, indent="\t"))

#
# 데이터 불러오기
dic_list = web_crawling.run(4)
# dic_list = firebase_connect.firebase_read('의류')

# 색 추출
dic_list = add_color_tag.dic_list_tagging(dic_list)

# json 파일 저장 #
py_json.json_write_dict("save_db.json", dic_list)

# RDS DB 연결 #
# rds_connect.run(dic_list)


# save_db.json 읽기 #
# dic_list = py_json.json_read('D:\github\web-crawling\save_db.json')
# for dic in dic_list:
#     if 'color' in dic:
#         s = dic["color"]
#         print(s)
#         dic['color'] = s.upper()
#         if s == 'Bk':
#             dic['saturation'], dic['value'] = dic['value'], dic['saturation']

# for dic in dic_list:
#     print(json.dumps(dic, indent="\t"))

# DB 연결 #
my_db_connecter.write(dic_list)

print("\n\n프로그램 종료")
