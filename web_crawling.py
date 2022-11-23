import json
import urllib.request
import time

from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

tag = {'TOP':['SHORT_SLEEVE','SHIRTS','LONG_SLEEVE','HOODIE'],
       'BOTTOM':['SHORTS','JEANS','SLACKS','COTTON_PANTS'],
       'OUTER':['COAT','JACKET','CARDIGAN'],
       'SHOES':['SNEAKERS','DRESS_SHOES'],
       'HAT':['HAT']}

dic_list = []

def run():  # 전체 실행
    global dic_list
    dic_list = []

    musinsa()
    lookpin()
    hiver()
    _29cm()

    return dic_list

def web_crawling(url):
    try:
        global dic_list
        time.sleep(0.5)     # 크롤링 차단 방지

        req = urllib.request.Request(url =url, headers=header)
        url_open = urllib.request.urlopen(req)
        return BeautifulSoup(url_open, "html.parser")

    except:
        print("url 접속 실패")

def musinsa():  # 무신사 크롤링
    numberring = {'SHORT_SLEEVE':'001001', 'SHIRTS':'001002', 'LONG_SLEEVE':'001010', 'HOODIE':'001004',
                  'SHORTS':'003009', 'JEANS':'003002', 'SLACKS':'003008', 'COTTON_PANTS':'003007',
                  'COAT':'002008', 'JACKET':'002017', 'CARDIGAN':'002020',
                  'SNEAKERS':'018', 'DRESS_SHOES':'005014', 'HAT':'007'}
    try:
        for i in tag.keys():
            for j in tag[i]:
                for n in range(1, 2):
                    print(f'musinsa {i} > {j} > {n} 페이지')
                    bs_obj = web_crawling(f'https://www.musinsa.com/categories/item/{numberring[j]}?d_cat_cd={numberring[j]}&brand=&list_kind=small&sort=pop_category&sub_sort=&page={n}&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=')

                    li_box = bs_obj.find("div", {"class", "list-box box"})

                    article_info = li_box.findAll("div", {"class", "article_info"})  # 상품 정보
                    lazyload = li_box.findAll("img", {"class", "lazyload lazy"})  # 이미지

                    for ai in range(len(article_info)):
                        a_tag = article_info[ai].find("p", {"class", "list_info"}).find("a")  # 제목 주소

                        p_tag = article_info[ai].find("p", {"class", "price"}).text  # 가격
                        p_tag = p_tag.split('\n')[2]
                        for c in [' ', '원', '\n', ',']:
                            p_tag = p_tag.replace(c, "")

                        picture = lazyload[ai]['data-original']     # 이미지
                        extension = picture[-4:]
                        picture = picture[:-7] + '500' + extension  # 이미지 확대

                        dic_list.append({'name': a_tag['title'],
                                         'price': int(p_tag),
                                         'major_tag': i,
                                         'detail_tag': j,
                                         'picture_URL': picture,
                                         'site_URL': a_tag['href'][2:],
                                         'site_name': 'musinsa',
                                         'views': 0})
    except:
        print("무신사 크롤링 실패")
# 무신사 주소
# 반팔티
# https://www.musinsa.com/categories/item/001001?d_cat_cd=001001&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=
# 셔츠
# https://www.musinsa.com/categories/item/001002?d_cat_cd=001002&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=
# 긴팔티
# https://www.musinsa.com/categories/item/001010?d_cat_cd=001010&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=
# 후드티
# https://www.musinsa.com/categories/item/001004?d_cat_cd=001004&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=

# 반바지
# https://www.musinsa.com/categories/item/003009?d_cat_cd=003009&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=
# 청바지
# https://www.musinsa.com/categories/item/003002?d_cat_cd=003002&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=
# 슬렉스
# https://www.musinsa.com/categories/item/003008?d_cat_cd=003008&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=
# 면바지
# https://www.musinsa.com/categories/item/003007?d_cat_cd=003007&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=

# 코트
# https://www.musinsa.com/categories/item/002008?d_cat_cd=002008&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=
# 자켓
# https://www.musinsa.com/categories/item/002017?d_cat_cd=002017&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=
# 가디건
# https://www.musinsa.com/categories/item/002020?d_cat_cd=002020&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=

# 스니커즈
# https://www.musinsa.com/categories/item/018?d_cat_cd=018&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=
# 구두
# https://www.musinsa.com/categories/item/005014?d_cat_cd=005014&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=

# 모자
# https://www.musinsa.com/categories/item/007?d_cat_cd=007&brand=&list_kind=small&sort=pop_category&sub_sort=&page=2&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=

def lookpin():  # 룩핀 크롤링
    pass


def hiver():    # 하이버 크롤링
    pass


def _29cm():    # 29cm 크롤링
    pass


if __name__ == '__main__':
    print("web_crawling 모듈입니다.")
    for i in run():
        print(json.dumps(i,indent="\t"))

