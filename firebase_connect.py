import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import time

# 서비스 계정의 비공개 키 파일이름
# cred = credentials.Certificate("./keys/codiwiki-tonton-firebase-key.json")
# firebase_admin.initialize_app(cred, {'projectId':'codiwiki-tonton'})
cred = credentials.Certificate("./keys/tttest-95867-firebase-key.json")
firebase_admin.initialize_app(cred, {'projectId':'tttest-95867'})
# cred = credentials.Certificate("./keys/test1124-a9535-firebase-key.json")
# firebase_admin.initialize_app(cred, {'projectId':'test1124-a9535'})

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
        dic_list = [doc.to_dict() for doc in users_ref.stream()]
        print("DB에서 읽은 자료수 :", len(dic_list))
        for i in range(3):
            print(" . ", end="")
            time.sleep(1)
        return dic_list

        # docs = users_ref.stream()
        # for doc in docs:
        #     print(u'{} => {}'.format(doc.id, doc.to_dict()))
    except:
        print("firebase 데이터 읽기 실패")
        print("collections_name :", collection_name)

def firebase_fix(collection_name, new_dic_list):
    try:
        fix_count = 0
        write_count = 0
        docs = db.collection(u'{}'.format(collection_name)).stream()

        line = 0

        for doc in docs:
            name = doc.to_dict()['name']
            for new_dic in new_dic_list:
                new = new_dic
                if name == new['name']:
                    print(f'[{line}]\tfix - {doc.id} : {name}')
                    line += 1
                    db.collection(u'{}'.format(collection_name)).document(doc.id).update(new)
                    fix_count += 1
                    break

        print('DB에서 수정한 의류 딕셔너리 수 :', fix_count)
        print('DB에 추가한 의류 딕셔너리 수 :', write_count)
    except:
        print("firebase 데이터 수정 실패")
        print("collections_name :", collection_name)


if __name__ == '__main__':
    print("codiwiki-tonton : firebase 접속 모듈입니다.")