import firebase_connect
import web_crawling

# dic = [{'name': '레이어드 크루 넥 반팔 티셔츠_일반 기장 [화이트]', 'price': 16900, 'detail_tag': 'SHORT_SLEEVE', 'picture_URL': '//image.msscdn.net/images/goods_img/20210825/2086653/2086653_1_125.jpg', 'site_URL': 'www.musinsa.com/app/goods/2086653', 'site_name': 'musinsa', 'major_tag': 'TOP', 'views': 0}, {'name': '레이어드 크루 넥 반팔 티셔츠_긴 기장 [화이트]', 'price': 1690015190, 'detail_tag': 'SHORT_SLEEVE', 'picture_URL': '//image.msscdn.net/images/goods_img/20200402/1382658/1382658_7_125.jpg', 'site_URL': 'www.musinsa.com/app/goods/1382658', 'site_name': 'musinsa', 'major_tag': 'TOP', 'views': 0}]
# firebase_connect.firebase_write('의류',dic)
firebase_connect.firebase_write('의류',web_crawling.run())

