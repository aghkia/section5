import simplejson as json
from tinydb.storages import MemoryStorage
from tinydb import TinyDB

#파일 DB 생성
db = TinyDB('C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section5\\databases\\database.db', default_table='users')

#메모리 DB 생성
# db = TinyDB(storages=MemoryStorage, default_table='users')

#테이블 선택
users = db.table('users')
todos = db.table('todos')

#테이블 데이터 삽입
# users.insert({'name':'kim', 'email':'test@google.com'})
# users.insert({'name':'homework', 'complete':'False'})

#테이블 데이터 전체 삽입1
with open('C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section5\\data\\users.json', 'r') as infile:
    r = json.loads(infile.read())
    for u in r:
        users.insert(u)

#테이블 데이터 전체 삽입2
with open('C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section5\\data\\todos.json', 'r') as infile:
    r = json.loads(infile.read())
    for t in r:
        todos.insert(t)

#전체 데이터 출력
print(users.all())
print(todos.all())

#테이블 목록 조회
print(db.tables())

#전체 데이터 삭제
# users.purge() #db.purge_table('users')
# todos.purge() #db.purge_table('todos')

#db.purge_tables() #전체 삭제

db.close()
