import color_extraction
import image_open
import remove_background
import ton_tag

import pymysql

def run(dic_list):

    try:
        conn, cursor = connect_DB()

        count = 1
        success = 0
        fail = 0

        for dic in dic_list:
            count, flag = insert(cursor, dic, count)
            if flag:
               success += 1
            else:
               fail += 1

        print(f"\n성공 : {success}개 , 실패 : {fail}개")

        conn.commit()
        conn.close()

    except:
        print("rds_connect run() : Fail")

def insert(cursor, dic, count):
    try:
        cursor.execute(
            "INSERT INTO clothes (detail_tag, major_tag, name, picture_url,price, site_name, site_url, sold, views, color, saturation, value) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
            (dic["detail_tag"], dic["major_tag"], dic["name"], dic["picture_URL"],
             dic["price"], dic["site_name"], dic["site_URL"], False, 0, dic['color'], dic['saturation'], dic['value']))

        print(f"[{count}]  " + "삽입 성공 :", dic["name"])
        return count + 1, True
    except:
        return count + 1, False
def connect_DB():
    host = "210.125.212.192"
    user = "admin"
    password = "1234"
    dbname = "tonton"
    port = 8888
    try:
        conn = pymysql.Connect(host=host, user=user, passwd=password, db=dbname,
                               port=port, use_unicode=True, charset='utf8')

        cursor = conn.cursor()
        return conn, cursor
    except:
        print("DB에 연결되지 않았습니다.")
        return -1

if  __name__ == "__main__":
    dic_list = [{'detail_tag': "HAT",
                 'major_tag': "HAT",
                 'name': "COLORED LOGO BEANIE_BK(21FWCP03)...",
                 'picture_URL': "//image.msscdn.net/images/goods_img/20200914/1602010/1602010_1_500.jpg",
                 'price': 29000,
                 'site_URL': "https://www.musinsa.com/app/goods/1602010",
                 'site_name': "musinsa",
                 'views': 0,
                 'color':'R',
                 'saturation':1,
                 'value':1},
                {'detail_tag': "SHORTS",
                 'major_tag': "BOTTOM",
                 'name': "CORDURA® Check Short Slate",
                 'picture_URL': "https://img.29cm.co.kr/next-product/2022/04/13/77aed525dd934b19abd5cad71fbb27e5_20220413163055.jpg?width=500",
                 'price': 65400,
                 'site_URL': "https://www.29cm.co.kr/product/1505778",
                 'site_name': "29cm",
                 'views': 0,
                 'color':'BC',
                 'saturation':1,
                 'value':1},
                {'detail_tag': "SNEAKERS",
                 'major_tag': "SHOES",
                 'name': "아미 트레이너 KR - 화이트:그레이 / 384686-01...",
                 'picture_URL': "https://image.msscdn.net/images/goods_img/20210805/2050302/2050302_3_500.jpg",
                 'price': 84900,
                 'site_URL': "https://www.musinsa.com/app/goods/2050302",
                 'site_name': "musinsa",
                 'views': 0,
                 'color':'PA',
                 'saturation':1,
                 'value':1}]
    run(dic_list)

    # 테이블 정보 가져오기
    # query = "SELECT * FROM clothes"
    # cursor.execute(query)
    # result = cursor.fetchall()
    # print(result)