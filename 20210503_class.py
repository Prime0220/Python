import sqlite3

lyrics  = '''너 없는 지금도 눈부신 하늘과
눈부시게 웃는 사람들
나의 헤어짐은 모르는 세상은
슬프도록 그대로인데
시간마저 데려가지 못하게
나만은 널 보내지 못했나봐
가시처럼 깊게 박힌 기억은
아파도 아픈줄 모르고
그대 기억이 지난 사랑이
내 안을 파고 드는 가시가 되어
제발 가라고 아주 가라고
애써도 나를 괴롭히는데
아픈만큼 너를 잊게 된다면
차라리 앓고 나면 그만인데
가시처럼 깊게 박힌 기억은
아파도 아픈줄 모르고
그대 기억이 지난 사랑이
내 안을 파고 드는 가시가 되어
제발 가라고 아주 가라고
애써도 나를 괴롭히는데
너무 사랑했던 나를
크게 두려웠던 나를
미치도록 너를 그리워했던
날 이제는 놓아줘
보이지 않아 내 안에 숨어
잊으려 하면 할수록 더 아파와
제발 가라고 아주 가라고
애써도 나를 괴롭히는데'''

con, cur = None, None
onechar, count = "", 0

con = sqlite3.connect("C:\\Users\\user\\Desktop\\snagilDB")

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS lyricsTB")
cur.execute("CREATE TABLE lyricsTB(onechar char(1), count INT)");
for ch in lyrics :
    if 'ㄱ' <= ch <= '힣' :
        cur.execute("SELECT * FROM lyricsTB WHERE onechar='" + ch + "'")
        row = cur.fetchone()
        if row == None :
            cur.execute("INSERT INTO lyricsTB VALUES ('" + ch + "'," + str(1) + ")")
        else :
            cnt = row[1]
            cur.execute("UPDATE lyricsTB SET count=" + str(cnt+1) + " WHERE  onechar= '" + ch + "'")
con.commit()

cur.execute("SELECT * FROM lyricsTB ORDER BY count DESC")
print("원문\n", lyrics)
print("--" * 10)
print("문자\t빈도수")
print("--" * 10)
while (True) :
    row = cur.fetchone()
    if row == None :
        break
    ch = row[0]
    cnt = row[1]
    print("%4s      %5d      " %(ch, cnt))
con.close()
