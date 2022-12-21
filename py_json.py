import json

def json_read(src):
    try:
        with open(src,'r', encoding='utf-8') as f:
            json_data = json.load(f)
            return json_data
    except:
        print("파일 읽기 실패")
        print("주소 :", src)

def json_write_dict(src, dic):
    try:
        with open(src,'w', encoding='utf-8') as f:
            json.dump(dic, f, indent="\t")
            print("파일 쓰기 성공")
            return True
    except:
        print("파일 쓰기 실패")
        print("주소 :", src)
        print("dic :", dic)

if __name__ == '__main__':
    print("python에서 json 파일 읽기")