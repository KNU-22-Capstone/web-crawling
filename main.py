import json

import firebase_connect
import web_crawling

firebase_connect.firebase_write('의류',web_crawling.run())
# firebase_connect.firbase_fix('의류', web_crawling.run())

# for i in web_crawling.run():
#     print(i)
#     print(json.dumps(i, indent="\t"))
