import sqlite3
import simplejson as json
import datetime

#DB 생성
conn = sqlite3.connect('C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section5\\databases\\sqlite1.db')
#conn = sqlite3.connect('C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section5\\databases\\sqlite1.db', isolation_level=None) #AutoCommit

#DB 생성(메모리 DB)
#conn = sqlite3.connect(":memory:")

#날짜 생성
now = datetime.datetime.now()
print('now', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime', nowDatetime)

#sqlite3 버전확인
print('sqlite3.version', sqlite3.version)
print('sqlite3.sqlite_version', sqlite3.sqlite_version)

#Cursor 연결
c = conn.cursor()
print(type(c))

#테이블 생성(SQLite3 Datatype: TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute('CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, username text, email text, phone text, website text, regdate text)')

#데이터 삽입
#c.execute("INSERT INTO users VALUES(1, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co.kr', ?)", (nowDatetime,))

userList = (
    (2, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co.kr', nowDatetime),
    (3, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co.kr', nowDatetime),
    (4, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co.kr', nowDatetime)
)

#c.executemany('INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)', userList)

with open('C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section5\\data\\users.json', 'r') as infile:
    r = json.load(infile)
    userData = []
    for user in r:
        t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime)
        #print('t', t)
        userData.append(t)
    #print('userData',userData)
    #print('userData', tuple(userData))
    c.executemany('INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)', userData)

#print('users db delete', conn.execute('delete from users').rowcount, 'rows') #데이터베이스 삭제
conn.commit()

conn.close()
