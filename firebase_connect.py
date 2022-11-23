import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 서비스 계정의 비공개 키 파일이름
# cred = credentials.Certificate("codiwiki-tonton-firebase-key.json")
# firebase_admin.initialize_app(cred, {'projectId':'codiwiki-tonton'})
# cred = credentials.Certificate("tttest-95867-firebase-key.json")
# firebase_admin.initialize_app(cred, {'projectId':'tttest-95867'})
cred = credentials.Certificate("test1124-a9535-firebase-key.json")
firebase_admin.initialize_app(cred, {'projectId':'test1124-a9535'})

db = firestore.client()

def firebase_write(collection_name, new_dic_list): # 데이터 쓰기
    try:
        dic_name_list = [i['name'] for i in firebase_read(collection_name)]

        write_count = 0

        for dic in new_dic_list:
            if dic['name'] not in dic_name_list:
                db.collection(u'{}'.format(collection_name)).document().set(dic)
                write_count += 1

        print('DB에 추가한 의류 딕셔너리 수 :', write_count)
    except:
        print("firebase 데이터 쓰기 실패")
        print("collections_name :", collection_name)

def firebase_read(collection_name): # 데이터 읽기
    try:
        users_ref = db.collection(u'{}'.format(collection_name))
        return [doc.to_dict() for doc in users_ref.stream()]

        # docs = users_ref.stream()
        # for doc in docs:
        #     print(u'{} => {}'.format(doc.id, doc.to_dict()))
    except:
        print("firebase 데이터 읽기 실패")
        print("collections_name :", collection_name)

def firbase_fix(collection_name, new_dic_list):
    try:
        fix_count = 0
        users_ref = db.collection(u'{}'.format(collection_name))
        docs = users_ref.stream()
        for doc in docs:
            name = doc.to_dict()['name']
            print(f'{name} 수정중...')
            for new_dic in new_dic_list:
                if name in new_dic['name']:
                    print('수정!!')
                    db.collection(u'{}'.format(collection_name)).document(doc.id).update(new_dic)
                    fix_count += 1
                    break

        print('DB에서 수정한 의류 딕셔너리 수 :', fix_count)
    except:
        print("firebase 데이터 수정 실패")
        print("collections_name :", collection_name)



if __name__ == '__main__':
    print("codiwiki-tonton : firebase 접속 모듈입니다.")

    # print("읽기 테스트")
    # for i in firebase_read("테스트"):
    #     print(json.dumps(i, indent="\t"))

    dic_list = [{'title': 'tapered raw denim (red selvage)', 'link': 'www.musinsa.com/app/goods/2128118', 'price': '71,400원'},
                {'title': 'Nonspan cropped denim pants_49W2...', 'link': 'www.musinsa.com/app/goods/2127952', 'price': '99,000원'},
                {'title': '밴딩 스트링 스탠다드핏 밑단절개 데님팬츠', 'link': 'www.musinsa.com/app/goods/2127854', 'price': '48,900원'},
                {'title': '밴딩 스트링 스탠다드핏 데님팬츠', 'link': 'www.musinsa.com/app/goods/2127836', 'price': '48,900원'},
                {'title': '빈티지 워시드 스텐다드 데님 팬츠 다크블루', 'link': 'www.musinsa.com/app/goods/2126628', 'price': '139,000원'},
                {'title': '빈티지 워시드 스텐다드 데님 팬츠 라이트 블루', 'link': 'www.musinsa.com/app/goods/2126624', 'price': '139,000원'},
                {'title': 'BELTED DENIM SKINNY JEANS-GREY', 'link': 'www.musinsa.com/app/goods/2125205', 'price': '85,000원'},
                {'title': 'BELTED DENIM SKINNY JEANS-CARBON...', 'link': 'www.musinsa.com/app/goods/2125202', 'price': '85,000원'},
                {'title': '여성 히든밴딩 인디고 보이핏 데님 팬츠-AERG2354B0...', 'link': 'www.musinsa.com/app/goods/2124499', 'price': '39,900원'},
                {'title': '슬림핏 스트링 워싱 밴딩 데님팬츠', 'link': 'www.musinsa.com/app/goods/2124381', 'price': '52,800원'},
                {'title': '슬림핏 워싱 데미지 스트링 데님팬츠', 'link': 'www.musinsa.com/app/goods/2124364', 'price': '52,800원'},
                {'title': '테이퍼드핏 워싱 디스트로이드 밑단컷팅 데님팬츠', 'link': 'www.musinsa.com/app/goods/2124302', 'price': '52,800원'},
                {'title': '밑단 절개 슬림 코튼 블랙진', 'link': 'www.musinsa.com/app/goods/2124254', 'price': '48,900원'},
                {'title': '빈티지워싱 데미지 밑단절개 데님팬츠', 'link': 'www.musinsa.com/app/goods/2124050', 'price': '49,800원'},
                {'title': '슬림 워싱 디스트로이드 데님팬츠', 'link': 'www.musinsa.com/app/goods/2123769', 'price': '52,800원'},
                {'title': '블랙워싱테이퍼드 BLACK WASHING TAPERED D...', 'link': 'www.musinsa.com/app/goods/2123611', 'price': '34,930원'},
                {'title': '베이직세미부츠컷 BASIC SEMI-BOOTS CUT DE...', 'link': 'www.musinsa.com/app/goods/2123592', 'price': '34,930원'},
                {'title': 'WIDE LONG STRAIGHT DENIM PANTS D...', 'link': 'www.musinsa.com/app/goods/2122972', 'price': '135,200원'},
                {'title': 'SEMI BOOTS CUT DENIM PANTS INDIG...', 'link': 'www.musinsa.com/app/goods/2122971', 'price': '127,200원'},
                {'title': 'Mother Fit Washing Denim', 'link': 'www.musinsa.com/app/goods/2122493', 'price': '64,800원'},
                {'title': 'Wide Fit Light Washing Denim', 'link': 'www.musinsa.com/app/goods/2122492', 'price': '89,000원'},
                {'title': '21FW 슬림핏 데님진 블랙 GMP00290 P000541...', 'link': 'www.musinsa.com/app/goods/2120664', 'price': '303,450원'},
                {'title': '21FW 로고 자수 스트레이트 데님진 589767 QOY7...', 'link': 'www.musinsa.com/app/goods/2120598', 'price': '418,950원'},
                {'title': '21FW 로고 자수 슬림핏 데님진 블랙 589763 QOY...', 'link': 'www.musinsa.com/app/goods/2120595', 'price': '418,950원'},
                {'title': '구제 테이퍼드핏 데님 팬츠[미디엄블루]', 'link': 'www.musinsa.com/app/goods/2120375', 'price': '39,000원'},
                {'title': '5P 슬림 스트레이트핏 블랙 데님', 'link': 'www.musinsa.com/app/goods/2120323', 'price': '198,000원'},
                {'title': '5P 라이트 블루 워싱 스트레이트핏 데님 (노스판)', 'link': 'www.musinsa.com/app/goods/2120114', 'price': '108,000원'},
                {'title': '[21FW] 크롭 킥 플레어 데님 팬츠', 'link': 'www.musinsa.com/app/goods/2119422', 'price': '85,440원'},
                {'title': 'Bootcut Fit Denim Jeans - Mid Bl...', 'link': 'www.musinsa.com/app/goods/2118534', 'price': '150,000원'},
                {'title': '사이드 트리밍 카고 데님 팬츠 KA [블루]', 'link': 'www.musinsa.com/app/goods/2118287', 'price': '53,400원'},
                {'title': '사이드 트리밍 카고 코듀로이 데님 팬츠 KA [러스트]', 'link': 'www.musinsa.com/app/goods/2118284', 'price': '89,000원'},
                {'title': 'SIDE POCKETS BIKER JEANS (BLACK)...', 'link': 'www.musinsa.com/app/goods/2117543', 'price': '50,000원'},
                {'title': '시그니처 데님 팬츠 (2컬러) Signature Denim...', 'link': 'www.musinsa.com/app/goods/2117152', 'price': '24,000원'},
                {'title': '[WIDE] Monday Jeans Blue', 'link': 'www.musinsa.com/app/goods/2117112', 'price': '42,000원'},
                {'title': '클릭 데님팬츠', 'link': 'www.musinsa.com/app/goods/2117099', 'price': '149,000원'},
                {'title': '에센셜 하프 데님팬츠', 'link': 'www.musinsa.com/app/goods/2117076', 'price': '98,000원'},
                {'title': '[STRAIGHT] Angel Jeans', 'link': 'www.musinsa.com/app/goods/2116815', 'price': '46,000원'},
                {'title': '와이드 테이퍼드 데님 팬츠 (블랙)_ PB3PA0101', 'link': 'www.musinsa.com/app/goods/2116020', 'price': '47,200원'},
                {'title': '배기 데님 팬츠 (블랙)_ PB3PA0303', 'link': 'www.musinsa.com/app/goods/2116019', 'price': '47,200원'},
                {'title': '사이드라인 브러쉬드 팬츠 데님 블랙', 'link': 'www.musinsa.com/app/goods/2115722', 'price': '37,800원'},
                {'title': '[21FW] STONE WASHING DENIM PANTS...', 'link': 'www.musinsa.com/app/goods/2114380', 'price': '83,400원'},
                {'title': '118 골지 데님 (CREAM)', 'link': 'www.musinsa.com/app/goods/2113858', 'price': '135,000원'},
                {'title': '롱부츠컷데님 LONG BOOTS-CUT DENIM', 'link': 'www.musinsa.com/app/goods/2112269', 'price': '24,950원'},
                {'title': '루즈스트레이트데님 LOOSE STRAIGHR DENIM', 'link': 'www.musinsa.com/app/goods/2112265', 'price': '24,950원'},
                {'title': 'SMILE LOGO DENIM PANTS ORANGE', 'link': 'www.musinsa.com/app/goods/2111262', 'price': '89,400원'},
                {'title': '에센셜 와이드 데님 팬츠', 'link': 'www.musinsa.com/app/goods/2111171', 'price': '98,000원'},
                {'title': '딥 블루 워싱 스판 데님 팬츠 [블루]', 'link': 'www.musinsa.com/app/goods/2110504', 'price': '79,000원'},
                {'title': '슬림핏 자수 데님 팬츠 [블루]', 'link': 'www.musinsa.com/app/goods/2110498', 'price': '79,000원'},
                {'title': '롤업 자수 블랙 데님 팬츠 [블랙]', 'link': 'www.musinsa.com/app/goods/2110486', 'price': '79,000원'},
                {'title': '[HAZZYS PHIZ][DEMIL컬렉션] 데밀오리지널 리...', 'link': 'www.musinsa.com/app/goods/2110278', 'price': '161,850원'},
                {'title': '슬림 스트레이트 베이직 데님_blue', 'link': 'www.musinsa.com/app/goods/2107613', 'price': '38,500원'},
                {'title': '슬림 부츠 스트레이트 크롭 데님_blue', 'link': 'www.musinsa.com/app/goods/2107504', 'price': '49,000원'},
                {'title': '[21FW] 노맨틱 백 로고 벨티드 데님 블루', 'link': 'www.musinsa.com/app/goods/2105862', 'price': '59,000원'},
                {'title': 'IN#0108 크리즈 라이트 블루 워싱 크롭 스트레이트', 'link': 'www.musinsa.com/app/goods/2104901', 'price': '54,600원'},
                {'title': '디스트로이드 부츠컷 데님 팬츠 KA [블랙]', 'link': 'www.musinsa.com/app/goods/2103791', 'price': '53,400원'},
                {'title': '크롭 테이퍼드 핏 데님 팬츠_CREAM', 'link': 'www.musinsa.com/app/goods/2103660', 'price': '52,430원'},
                {'title': 'STRAIGHT SLIM FIT DENIM PANTS DA...', 'link': 'www.musinsa.com/app/goods/2103385', 'price': '138,000원'},
                {'title': 'STRAIGHT SLIM FIT DENIM PANTS BL...', 'link': 'www.musinsa.com/app/goods/2103266', 'price': '138,000원'},
                {'title': 'CROP WIDE DENIM PANTS CREAM', 'link': 'www.musinsa.com/app/goods/2103230', 'price': '138,000원'},
                {'title': 'CROP WIDE DENIM PANTS DARK GREY', 'link': 'www.musinsa.com/app/goods/2103226', 'price': '138,000원'},
                {'title': 'INSIDE SLIT DENIM PANTS BLUE', 'link': 'www.musinsa.com/app/goods/2103223', 'price': '138,000원'},
                {'title': 'ONE TUCK BAGGY INDIGO DENIM PANT...', 'link': 'www.musinsa.com/app/goods/2103221', 'price': '138,000원'},
                {'title': 'VINTAGE WASHING TAPERED FIT DENI...', 'link': 'www.musinsa.com/app/goods/2103211', 'price': '138,000원'},
                {'title': '데님 블록 스플래터 릴렉스핏 진 (다크-라이트)', 'link': 'www.musinsa.com/app/goods/2101684', 'price': '289,000원'},
                {'title': '데님 블록 스플래터 릴렉스핏 진 (라이트-다크)', 'link': 'www.musinsa.com/app/goods/2101683', 'price': '289,000원'},
                {'title': '웨이스트 밴딩 라이트 데님 그래피티 아트 하프 팬츠', 'link': 'www.musinsa.com/app/goods/2101682', 'price': '119,000원'},
                {'title': 'Straight Denim', 'link': 'www.musinsa.com/app/goods/2101381', 'price': '108,000원'},
                {'title': 'Slit Denim', 'link': 'www.musinsa.com/app/goods/2101183', 'price': '117,000원'},
                {'title': 'SI JN 6023 Tapered Deep Blue Jea...', 'link': 'www.musinsa.com/app/goods/2100571', 'price': '107,000원'},
                {'title': '디스트레스드 스판 데님 [블루]', 'link': 'www.musinsa.com/app/goods/2100266', 'price': '114,000원'},
                {'title': '워싱 밴딩 데님 팬츠[뉴스탠다드]_M216MPT760M', 'link': 'www.musinsa.com/app/goods/2099594', 'price': '127,200원'},
                {'title': '워싱 밴딩 데님 팬츠[뉴스탠다드]_M216MPT761M', 'link': 'www.musinsa.com/app/goods/2099592', 'price': '127,200원'},
                {'title': '톤 배색 데님 팬츠[뉴스탠다드]_M216MPT758M', 'link': 'www.musinsa.com/app/goods/2099591', 'price': '107,400원'},
                {'title': '톤 배색 데님 팬츠[뉴스탠다드]_M216MPT759M', 'link': 'www.musinsa.com/app/goods/2099590', 'price': '107,400원'},
                {'title': '[21FW] 그레이 워싱 데님 팬츠_루즈테이퍼드핏 (421...', 'link': 'www.musinsa.com/app/goods/2098738', 'price': '24,950원'},
                {'title': 'Comfy Wide Jeans - MEDIUM BLUE', 'link': 'www.musinsa.com/app/goods/2098208', 'price': '59,400원'},
                {'title': '[21FW] 루즈 스트레이트 데님 팬츠', 'link': 'www.musinsa.com/app/goods/2098160', 'price': '80,640원'},
                {'title': '[BOY] Camping Jeans', 'link': 'www.musinsa.com/app/goods/2098143', 'price': '36,400원'},
                {'title': '[STRAIGHT] Resurrect Jeans', 'link': 'www.musinsa.com/app/goods/2097669', 'price': '82,000원'},
                {'title': '가먼트다잉데님(퍼플그레이)', 'link': 'www.musinsa.com/app/goods/2097644', 'price': '66,750원'},
                {'title': '가먼트다잉데님(브라운)', 'link': 'www.musinsa.com/app/goods/2097643', 'price': '66,750원'},
                {'title': '하트 디스트로이드 스트레이트 와이드 데님 진 청바지', 'link': 'www.musinsa.com/app/goods/2096656', 'price': '89,000원'},
                {'title': 'Windy semi boots denim_blue [21F...', 'link': 'www.musinsa.com/app/goods/2096434', 'price': '71,200원'},
                {'title': '워시드 슬림 데님 팬츠(Blue)', 'link': 'www.musinsa.com/app/goods/2096201', 'price': '69,420원'},
                {'title': '[unisex] C logo pants (khaki)', 'link': 'www.musinsa.com/app/goods/2096162', 'price': '60,000원'},
                {'title': '[unisex] C logo pants (ivory)', 'link': 'www.musinsa.com/app/goods/2096161', 'price': '60,000원'},
                {'title': '[unisex] bleach denim pants (bla...', 'link': 'www.musinsa.com/app/goods/2096157', 'price': '57,600원'},
                {'title': 'AMC 프리미엄 데님 팬츠 블루_Women', 'link': 'www.musinsa.com/app/goods/2094711', 'price': '53,400원'},
                {'title': 'AMC 프리미엄 데님 팬츠 블루_Men', 'link': 'www.musinsa.com/app/goods/2094691', 'price': '53,400원'},
                {'title': '페인팅 와이드 데님 팬츠', 'link': 'www.musinsa.com/app/goods/2094298', 'price': '71,500원'},
                {'title': '테스트11111111111', 'link': '@@@@@@@@', 'price': 777777},
                {'title': '테스트22222222222', 'link': '@@@@@@@@@', 'price': 2222}]

    # print("입력 테스트")
    # firebase_write("테스트3", dic_list)
    # print("종료")