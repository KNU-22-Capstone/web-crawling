import urllib.request
from bs4 import BeautifulSoup

file = open("musinsa 데닝펜츠 100페이지.txt", "w")

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
url = "https://www.musinsa.com/categories/item/003002?d_cat_cd=003002&brand=&list_kind=small&sort=pop_category&sub_sort=&page=1&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure="
for i in range(2,102):
    # time.sleep(2)
    req = urllib.request.Request(url =url, headers=header)
    url_open = urllib.request.urlopen(req)
    bs_obj = BeautifulSoup(url_open, "html.parser")

    li_box = bs_obj.find("div", {"class", "list-box box"})
    article_info = li_box.findAll("div", {"class", "article_info"})

    def get_goods_info(ai):
        a_tag = ai.find("p", {"class", "list_info"}).find("a")
        title = a_tag['title']
        link = a_tag['href'][2:]
        p_tag = ai.find("p", {"class", "price"}).text.replace(" ", "").split("\n")[2]
        return {"title": title, "link": link, "price": p_tag}

    slid = "\n================================================\n " + (str(i-1)) + " 페이지 끝\n================================================\n"
    for ai in article_info:
        text = str(get_goods_info(ai))
        print(text)
        file.write(text + " ")
    print(slid)
    file.write(slid)

    start_idx = 119
    end_idx = start_idx + len(str(i-1))
    url = url[:start_idx] + str(i) + url[end_idx:]
    print("\n"+url+"\n")

file.close()

print("잘 완료 됨")

# 결과 #

# ================================================
#  1 페이지 끝
# ================================================
#
#
# ================================================
#  2 페이지 끝
# ================================================
#
# 생략
#
# ================================================
#  99 페이지 끝
# ================================================
#
#
# ================================================
#  100 페이지 끝
# ================================================
#
# 잘 완료 됨