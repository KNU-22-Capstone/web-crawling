import json

import color_extraction
import image_open
import remove_background
import ton_tag


def dic_list_tagging(dic_list):
    count = 0
    result_dic_list = []
    for dic in dic_list:

        for i in range(10):
            image = image_open.img_url_open(dic['picture_URL'])
            image = remove_background.image_remove(image)
            if type(image) != type(-1):
                break
        if type(image) == type(-1):
            continue
        color_hsv = color_extraction.extract(image)
        dic['color'], dic['saturation'], dic['value'] = ton_tag.tagging(color_hsv)

        print(f'count : {count}')
        print(dic['picture_URL'])
        print(dic['color'], dic['saturation'], dic['value'])

        count += 1
        result_dic_list.append(dic)
    return dic_list


if __name__ == "__main__":
    dic_list = [
        {
            "name": "Laulhere Authentique Wool Beret (12 colors)",
            "price": 76950,
            "major_tag": "HAT",
            "detail_tag": "HAT",
            "picture_URL": "https://img.29cm.co.kr/next-product/2020/10/22/60fc0728d7eb4e55b05ee99a0e35de97_20201022092914.jpg?width=500",
            "site_URL": "https://www.29cm.co.kr/product/488907",
            "site_name": "29cm",
            "sold": False,
            "views": 0
        },
        {
            "name": "Times Cap Green",
            "price": 27300,
            "major_tag": "HAT",
            "detail_tag": "HAT",
            "picture_URL": "https://img.29cm.co.kr/next-product/2022/08/18/82a1aa8a5144459ab6cc7392ddb85fce_20220818154202.jpg?width=500",
            "site_URL": "https://www.29cm.co.kr/product/1669580",
            "site_name": "29cm",
            "sold": False,
            "views": 0
        },
        {
            "name": "FLOWERING BUCKET BLACK",
            "price": 108000,
            "major_tag": "HAT",
            "detail_tag": "HAT",
            "picture_URL": "https://img.29cm.co.kr/next-product/2022/09/21/2de90ec79209466a9c568257ab355dc1_20220921141925.jpeg?width=500",
            "site_URL": "https://www.29cm.co.kr/product/1733266",
            "site_name": "29cm",
            "sold": False,
            "views": 0
        }]
    dic_list = dic_list_tagging(dic_list)

    for dic in dic_list:
        print(json.dumps(dic, indent="\t"))
