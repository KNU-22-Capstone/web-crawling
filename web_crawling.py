import json

import urllib.request
from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

tag = {'TOP':['SHORT_SLEEVE','SHIRTS','LONG_SLEEVE','HOODIE'],
       'BOTTOM':['SHORTS','JEANS','SLACKS','COTTON_PANTS'],
       'OUTER':['COAT','JACKET','CARDIGAN'],
       'SHOES':['SNEAKERS','DRESS_SHOES'],
       'HAT':['HAT']}

dic_list = []
page_size = 0

def run():  # 전체 실행
    global dic_list, page_size
    dic_list = []
    page_size = 1

    musinsa()
    lookpin()
    hiver()
    _29cm()

    print(f'의류 딕셔너리 수 : {len(dic_list)}')
    return dic_list

def web_crawling(url):
    try:
        print(url)
        time.sleep(3)     # 크롤링 차단 방지

        req = urllib.request.Request(url =url, headers=header)
        url_open = urllib.request.urlopen(req)
        return BeautifulSoup(url_open, "html.parser")

    except:
        print("url 접속 실패")

def musinsa():  # 무신사 크롤링
    try:
        global page_size
        numberring = {'SHORT_SLEEVE': '001001', 'SHIRTS': '001002', 'LONG_SLEEVE': '001010', 'HOODIE': '001004',
                      'SHORTS': '003009', 'JEANS': '003002', 'SLACKS': '003008', 'COTTON_PANTS': '003007',
                      'COAT': '002008', 'JACKET': '002017', 'CARDIGAN': '002020',
                      'SNEAKERS': '018', 'DRESS_SHOES': '005014', 'HAT': '007'}

        for i in tag.keys():
            for j in tag[i]:
                for n in range(1, page_size+1):
                    time.sleep(0.2)
                    print(f'musinsa : {i} > {j} > {n} 페이지')
                    url = f'https://www.musinsa.com/categories/item/{numberring[j]}?d_cat_cd={numberring[j]}&brand=&list_kind=small&sort=pop_category&sub_sort=&page={n}&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
                    print(url)
                    req = urllib.request.Request(url=url, headers=header)
                    url_open = urllib.request.urlopen(req)
                    bs_obj = BeautifulSoup(url_open, "html.parser")

                    li_box = bs_obj.find("div", {"class", "list-box box"})
                    article_info = li_box.findAll("div", {"class", "article_info"})  # 상품 정보
                    lazyload = li_box.findAll("img", {"class", "lazyload lazy"})  # 이미지

                    for ai in range(len(article_info)):
                        a_tag = article_info[ai].find("p", {"class", "list_info"}).find("a")  # 제목 주소

                        p_tag = article_info[ai].find("p", {"class", "price"}).text  # 가격
                        price = p_tag.split('\n')[2]
                        for c in [' ', '원', '\n', ',']:
                            price = price.replace(c, "")

                        picture = lazyload[ai]['data-original']     # 이미지
                        extension = picture[-4:]
                        picture = picture[:-7] + '500' + extension  # 이미지 확대

                        dic_list.append({'name': a_tag['title'],
                                         'price': int(price),
                                         'major_tag': i,
                                         'detail_tag': j,
                                         'picture_URL': picture,
                                         'site_URL': 'https://'+a_tag['href'][2:],
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
    try:
        global page_size
        tail = {
            'SHORT_SLEEVE': '%EC%83%81%EC%9D%98%20%EB%B0%98%ED%8C%94%ED%8B%B0&category=%EB%B0%98%ED%8C%94%ED%8B%B0&main=%EC%83%81%EC%9D%98',
            'SHIRTS': '%EC%83%81%EC%9D%98%20%EC%85%94%EC%B8%A0%2F%EB%82%A8%EB%B0%A9&category=%EC%85%94%EC%B8%A0%2F%EB%82%A8%EB%B0%A9&main=%EC%83%81%EC%9D%98',
            'LONG_SLEEVE': '%EC%83%81%EC%9D%98%20%EA%B8%B4%ED%8C%94%ED%8B%B0&category=%EA%B8%B4%ED%8C%94%ED%8B%B0&main=%EC%83%81%EC%9D%98',
            'HOODIE': '%EC%83%81%EC%9D%98%20%ED%9B%84%EB%93%9C%ED%8B%B0%2F%EC%95%84%EB%85%B8%EB%9D%BD&category=%ED%9B%84%EB%93%9C%ED%8B%B0%2F%EC%95%84%EB%85%B8%EB%9D%BD&main=%EC%83%81%EC%9D%98',
            'SHORTS': '%ED%95%98%EC%9D%98%20%EB%B0%98%EB%B0%94%EC%A7%80&category=%EB%B0%98%EB%B0%94%EC%A7%80&main=%ED%95%98%EC%9D%98',
            'JEANS': '%ED%95%98%EC%9D%98%20%EC%B2%AD%EB%B0%94%EC%A7%80&category=%EC%B2%AD%EB%B0%94%EC%A7%80&main=%ED%95%98%EC%9D%98',
            'SLACKS': '%ED%95%98%EC%9D%98%20%EC%8A%AC%EB%9E%99%EC%8A%A4&category=%EC%8A%AC%EB%9E%99%EC%8A%A4&main=%ED%95%98%EC%9D%98',
            'COTTON_PANTS': '%ED%95%98%EC%9D%98%20%EB%A9%B4%EB%B0%94%EC%A7%80&category=%EB%A9%B4%EB%B0%94%EC%A7%80&main=%ED%95%98%EC%9D%98',
            'COAT': '%EC%95%84%EC%9A%B0%ED%84%B0%20%EC%BD%94%ED%8A%B8&category=%EC%BD%94%ED%8A%B8&main=%EC%95%84%EC%9A%B0%ED%84%B0',
            'JACKET': '%EC%95%84%EC%9A%B0%ED%84%B0%20%EC%9E%90%EC%BC%93&category=%EC%9E%90%EC%BC%93&main=%EC%95%84%EC%9A%B0%ED%84%B0',
            'CARDIGAN': '%EC%95%84%EC%9A%B0%ED%84%B0%20%EA%B0%80%EB%94%94%EA%B1%B4&category=%EA%B0%80%EB%94%94%EA%B1%B4&main=%EC%95%84%EC%9A%B0%ED%84%B0',
            'SNEAKERS': '%EC%8B%A0%EB%B0%9C%20%EC%8A%A4%EB%8B%88%EC%BB%A4%EC%A6%88&category=%EC%8A%A4%EB%8B%88%EC%BB%A4%EC%A6%88&main=%EC%8B%A0%EB%B0%9C',
            'DRESS_SHOES': '%EC%8B%A0%EB%B0%9C%20%EA%B5%AC%EB%91%90&category=%EA%B5%AC%EB%91%90&main=%EC%8B%A0%EB%B0%9C',
            'HAT': '%EC%95%A1%EC%84%B8%EC%84%9C%EB%A6%AC%20%EB%AA%A8%EC%9E%90&category=%EB%AA%A8%EC%9E%90&main=%EC%95%A1%EC%84%B8%EC%84%9C%EB%A6%AC'}

        options = webdriver.ChromeOptions()  # 옵션 생성
        options.add_argument("headless")  # 창 숨기는 옵션 추가

        # 드라이버 실행
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # 윈도우 크기 설정 : headless는 충분한 해상도가 나오지 않아서 따로 지정해줘야 element.click() 사용 가능
        driver.set_window_size(1440, 900)

        # url 접속
        driver.get(url=f'https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%83%81%EC%9D%98%20%EB%B0%98%ED%8C%94%ED%8B%B0&category=%EB%B0%98%ED%8C%94%ED%8B%B0&main=%EC%83%81%EC%9D%98')
        # 페이지 로딩 대기
        driver.implicitly_wait(3)

        # 룩핀 모달창 끄기
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div/div/div[3]/button').click()

        for i in tag.keys():
            for j in tag[i]:
                for n in range(1, page_size + 1):
                    print(f'lookpin : {i} > {j} > {n} 페이지')
                    time.sleep(0.2)

                    # url 접속
                    url = f'https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D={n}&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D={tail[j]}'
                    print(url)
                    driver.get(url=url)

                    bs_obj = BeautifulSoup(driver.page_source, "html.parser")
                    section = bs_obj.find("section", {"class", "SearchShare_products__2wIGC"})              # 전체 상품 그리드 section
                    section_list = section.findAll("section", {"class", "ProductCardShare_card__FAfuv"})    # 개별 상품 section 리스트
                    for sl in section_list:
                        picture = sl.find("img")["data-src"][:-3]+'1000'

                        name = sl.find("li", {"class", "ProductCardShare_product-name__35udD"}).text
                        price = int(sl.find("div", {"class", "bold ProductCardShare_price__WGlSK"}).text.replace(',','').replace('원',''))

                        site_URL = 'https://www.lookpin.co.kr' + sl.find("a")['href']

                        dic_list.append({'name': name,
                                         'price': int(price),
                                         'major_tag': i,
                                         'detail_tag': j,
                                         'picture_URL': picture,
                                         'site_URL': site_URL,
                                         'site_name': 'lookpin',
                                         'views': 0})
        # 드라이버 종료
        driver.quit()
    except:
        print("룩핀 크롤링 실패")
# 룩핀 주소
# 반팔티
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%83%81%EC%9D%98%20%EB%B0%98%ED%8C%94%ED%8B%B0&category=%EB%B0%98%ED%8C%94%ED%8B%B0&main=%EC%83%81%EC%9D%98
# 셔츠
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&parms%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%83%81%EC%9D%98%20%EC%85%94%EC%B8%A0%2F%EB%82%A8%EB%B0%A9&category=%EC%85%94%EC%B8%A0%2F%EB%82%A8%EB%B0%A9&main=%EC%83%81%EC%9D%98
# 긴팔티
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%83%81%EC%9D%98%20%EA%B8%B4%ED%8C%94%ED%8B%B0&category=%EA%B8%B4%ED%8C%94%ED%8B%B0&main=%EC%83%81%EC%9D%98
# 후드티
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%83%81%EC%9D%98%20%ED%9B%84%EB%93%9C%ED%8B%B0%2F%EC%95%84%EB%85%B8%EB%9D%BD&category=%ED%9B%84%EB%93%9C%ED%8B%B0%2F%EC%95%84%EB%85%B8%EB%9D%BD&main=%EC%83%81%EC%9D%98

# 반바지
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%ED%95%98%EC%9D%98%20%EB%B0%98%EB%B0%94%EC%A7%80&category=%EB%B0%98%EB%B0%94%EC%A7%80&main=%ED%95%98%EC%9D%98
# 청바지
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%ED%95%98%EC%9D%98%20%EC%B2%AD%EB%B0%94%EC%A7%80&category=%EC%B2%AD%EB%B0%94%EC%A7%80&main=%ED%95%98%EC%9D%98
# 슬렉스
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%ED%95%98%EC%9D%98%20%EC%8A%AC%EB%9E%99%EC%8A%A4&category=%EC%8A%AC%EB%9E%99%EC%8A%A4&main=%ED%95%98%EC%9D%98
# 면바지
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%ED%95%98%EC%9D%98%20%EB%A9%B4%EB%B0%94%EC%A7%80&category=%EB%A9%B4%EB%B0%94%EC%A7%80&main=%ED%95%98%EC%9D%98

# 코트
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%95%84%EC%9A%B0%ED%84%B0%20%EC%BD%94%ED%8A%B8&category=%EC%BD%94%ED%8A%B8&main=%EC%95%84%EC%9A%B0%ED%84%B0
# 자켓
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%95%84%EC%9A%B0%ED%84%B0%20%EC%9E%90%EC%BC%93&category=%EC%9E%90%EC%BC%93&main=%EC%95%84%EC%9A%B0%ED%84%B0
# 가디건
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%95%84%EC%9A%B0%ED%84%B0%20%EA%B0%80%EB%94%94%EA%B1%B4&category=%EA%B0%80%EB%94%94%EA%B1%B4&main=%EC%95%84%EC%9A%B0%ED%84%B0

# 스니커즈
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%8B%A0%EB%B0%9C%20%EC%8A%A4%EB%8B%88%EC%BB%A4%EC%A6%88&category=%EC%8A%A4%EB%8B%88%EC%BB%A4%EC%A6%88&main=%EC%8B%A0%EB%B0%9C
# 구두
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%8B%A0%EB%B0%9C%20%EA%B5%AC%EB%91%90&category=%EA%B5%AC%EB%91%90&main=%EC%8B%A0%EB%B0%9C

# 모자
# https://www.lookpin.co.kr/search/category?params%5Border%5D=trending&params%5Bpage%5D%5Bnumber%5D=1&params%5Bpage%5D%5Bsize%5D=100&params%5BgenderId%5D=men&params%5BonlyLikeStores%5D=false&params%5Bname%5D=%EC%95%A1%EC%84%B8%EC%84%9C%EB%A6%AC%20%EB%AA%A8%EC%9E%90&category=%EB%AA%A8%EC%9E%90&main=%EC%95%A1%EC%84%B8%EC%84%9C%EB%A6%AC

def hiver():    # 하이버 크롤링
    try:
        global page_size
        numberring = {'SHORT_SLEEVE': '425', 'SHIRTS': '431', 'LONG_SLEEVE': '426', 'HOODIE': '428',
                      'SHORTS': '442', 'JEANS': '441', 'SLACKS': '439', 'COTTON_PANTS': '003007',
                      'COAT': '418', 'JACKET': '420', 'CARDIGAN': '421',
                      'SNEAKERS': '447', 'DRESS_SHOES': '448', 'HAT': '607'}

        options = webdriver.ChromeOptions()  # 옵션 생성
        options.add_argument("headless")  # 창 숨기는 옵션 추가

        # 드라이버 실행
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # 윈도우 크기 설정 : headless는 충분한 해상도가 나오지 않아서 따로 지정해줘야 element.click() 사용 가능
        driver.set_window_size(1440, 900)


        for i in tag.keys():
            for j in tag[i]:
                print(f'hiver : {i} > {j}')

                print(f'https://www.hiver.co.kr/categories/{numberring[j]}/shopping')
                # url 접속
                driver.get(
                    url=f'https://www.hiver.co.kr/categories/{numberring[j]}/shopping')
                time.sleep(1.5)
                driver.refresh()
                time.sleep(1.5)

                bs_obj = BeautifulSoup(driver.page_source, "html.parser")
                container = bs_obj.find("div", {"class", "frame-container"})   # 전체 상품 그리드 div
                frame = container.find("div", {"class", "frame"})
                li_list = frame.findAll("li")     # 개별 상품 li 리스트

                for li in li_list:
                    picture = li.find("span")["style"][23:-3]

                    name = li.find("span", {"class", "product-name"}).text
                    price = int(li.find("strong", {"class", "current-price"}).text.replace(',','').replace('원',''))

                    site_URL = 'https://www.hiver.co.kr' + li.find("a")["href"]

                    dic_list.append({'name': name,
                                     'price': int(price),
                                     'major_tag': i,
                                     'detail_tag': j,
                                     'picture_URL': picture,
                                     'site_URL': site_URL,
                                     'site_name': 'hiver',
                                     'views': 0})
        # 드라이버 종료
        driver.quit()
    except:
        print("하이버 크롤링 실패")

# 하이버 주소
# 반팔티
# https://www.hiver.co.kr/categories/425/shopping
# 셔츠
# https://www.hiver.co.kr/categories/431/shopping
# 긴팔티
# https://www.hiver.co.kr/categories/426/shopping
# 후드티
# https://www.hiver.co.kr/categories/428/shopping

# 반바지
# https://www.hiver.co.kr/categories/442/shopping
# 청바지
# https://www.hiver.co.kr/categories/441/shopping
# 슬렉스
# https://www.hiver.co.kr/categories/439/shopping
# 면바지
# https://www.hiver.co.kr/categories/440/shopping

# 코트
# https://www.hiver.co.kr/categories/418/shopping
# 자켓
# https://www.hiver.co.kr/categories/420/shopping
# 가디건
# https://www.hiver.co.kr/categories/421/shopping

# 스니커즈
# https://www.hiver.co.kr/categories/447/shopping
# 구두
# https://www.hiver.co.kr/categories/448/shopping

# 모자
# https://www.hiver.co.kr/categories/607/shopping



def _29cm():    # 29cm 크롤링
    try:
        global page_size
        tail = {
            'SHORT_SLEEVE': '272100100&category_medium_code=272103100&category_small_code=272103101&sort=latest',
            'SHIRTS': '272100100&category_medium_code=272103100&category_small_code=272103106&sort=latest',
            'LONG_SLEEVE': '272100100&category_medium_code=272103100&category_small_code=272103102&sort=latest',
            'HOODIE': '272100100&category_medium_code=272103100&category_small_code=272103108&sort=latest',
            'SHORTS': '272100100&category_medium_code=272104100&category_small_code=272104108&sort=latest',
            'JEANS': '272100100&category_medium_code=272104100&category_small_code=272104104&sort=latest',
            'SLACKS': '272100100&category_medium_code=272104100&category_small_code=272104106&sort=latest',
            'COTTON_PANTS': '272100100&category_medium_code=272104100&category_small_code=272104105&sort=latest',
            'COAT': '272100100&category_medium_code=272102100&category_small_code=272102101&sort=latest',
            'JACKET': '272100100&category_medium_code=272102100&category_small_code=272102111&sort=latest',
            'CARDIGAN': '272100100&category_medium_code=272102100&category_small_code=272102108&sort=latest',
            'SNEAKERS': '274100100&category_medium_code=274101100',
            'DRESS_SHOES': '274100100&category_medium_code=274103100',
            'HAT': '275100100&category_medium_code=275101100'}

        options = webdriver.ChromeOptions()  # 옵션 생성
        options.add_argument("headless")  # 창 숨기는 옵션 추가

        # 드라이버 실행
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # 윈도우 크기 설정 : headless는 충분한 해상도가 나오지 않아서 따로 지정해줘야 element.click() 사용 가능
        driver.set_window_size(1440, 900)

        for i in tag.keys():
            for j in tag[i]:
                for n in range(1, page_size + 1):
                    print(f'29cm : {i} > {j} > {n} 페이지')

                    print(f'https://www.29cm.co.kr/shop/category/list?category_large_code={tail[j]}&page={n}&count=100')
                    # url 접속
                    driver.get(
                        url=f'https://www.29cm.co.kr/shop/category/list?category_large_code={tail[j]}&page={n}&count=100')
                    time.sleep(1.5)
                    driver.refresh()
                    time.sleep(1.5)

                    bs_obj = BeautifulSoup(driver.page_source, "html.parser")
                    div_product_content = bs_obj.find("div", {"class", "product_content ng-star-inserted"})
                    a_list = div_product_content.findAll("a", {"class", "prd_b_area"})

                    for a in a_list:
                        name = a.find("div", {"class", "name"}).text.replace("\n","").strip()

                        price = a.find("div", {"class", "price"})
                        span_num_list = price.findAll("span", {"class", "num"})
                        price = int(span_num_list[-1].text.replace(",",""))

                        site_URL = a['href']
                        picture = "https:"+a.find('img')['src']

                        dic_list.append({'name': name,
                                         'price': price,
                                         'major_tag': i,
                                         'detail_tag': j,
                                         'picture_URL': picture,
                                         'site_URL': site_URL,
                                         'site_name': '29cm',
                                         'views': 0})
    except:
        print("29cm 크롤링 실패")

# 29cm 주소
# 반팔티
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272103100&category_small_code=272103101&sort=latest&page=1&count=100
# 셔츠
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272103100&category_small_code=272103106&sort=latest&page=1&count=100
# 긴팔티
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272103100&category_small_code=272103102&sort=latest&page=1&count=100
# 후드티
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272103100&category_small_code=272103108&sort=latest&page=1&count=100

# 반바지
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272104100&category_small_code=272104108&sort=latest&page=1&count=100
# 청바지
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272104100&category_small_code=272104104&sort=latest&page=1&count=100
# 슬렉스
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272104100&category_small_code=272104106&sort=latest&page=1&count=100
# 면바지
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272104100&category_small_code=272104105&sort=latest&page=1&count=100

# 코트
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272102100&category_small_code=272102101&sort=latest&page=1&count=100
# 자켓
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272102100&category_small_code=272102111&sort=latest&page=1&count=100
# 가디건
# https://www.29cm.co.kr/shop/category/list?category_large_code=272100100&category_medium_code=272102100&category_small_code=272102108&sort=latest&page=1&count=100

# 스니커즈
# https://www.29cm.co.kr/shop/category/list?category_large_code=274100100&category_medium_code=274101100&page=1&count=100
# 구두
# https://www.29cm.co.kr/shop/category/list?category_large_code=274100100&category_medium_code=274103100&page=1&count=100

# 모자
# https://www.29cm.co.kr/shop/category/list?category_large_code=275100100&category_medium_code=275101100&page=1&count=100


if __name__ == '__main__':
    print("web_crawling 모듈입니다.")
    for i in run():
        print(json.dumps(i,indent="\t"))

