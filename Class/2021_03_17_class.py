#append메소드를 사용하여 리스트에 요소 추가

a = [1, 2, 3, 4, 5]
print(a)
a.append([6, 7, 8])
print(a)
print(a[5])
print(a[5][2])
print(type(a))
print('--'*45)

#extend 메소드를 사용하여 리스트에 여러값을 추가

b = [1, 2, 3, 4, 5]
print(b)
b.extend([6, 7, 8])
print(b)

print('--'*45)

#insert 메소드를 사용하여 특정 위치에 요소 추가

c = [1, 3, 5, 7]
print(c)
c.insert(1, 2)
print(c)
c.insert(4, 6)
print(c)
c.insert(7, 8)
print(c)

print('--'*45)

d1 = [1, 2, 7, 8]
d2 = [1, 2, 7, 8]

d1.insert(2, [3, 4, 5, 6])
print(d1)

d2[2 : 2] = [3, 4, 5, 6]
print(d2)

print('--'*45)

########### 도전문제 ############
# -다음과 같은 리스트가 있다고 하자. [1, 3, 5, 7, 10]
# 1. 리스트의 마지막에 11을 추가하세요.
# 2. 리스트의 5와 7 사이에 6을 추가하세요오옹.
# 3. 리스트의 7과 10 사이에 8, 9를 추가하세요.(단, 명령어 1개로 처리하세요.)

e = [1, 3, 5, 7, 10]

e.insert(3, 6)
e[5:5] = (8, 9)
e.append(11)

print(e)

print('--'*45)

#리스트의 마지막 요소나 특정 인덱스 위치의 값을 삭제하는 메소드 [ pop ]

f = [1, 2, 3, 4, 5]
f.pop()
print(f)
f.pop()
print(f)

print('--'*45)

g = [1, 2, 3, 4, 5]
g.pop(2)
print(g)
del g[1]
print(g)

print('--'*45)

#리스트의 지정된 값을 찾아 삭제하는 메소드 [ remove ]

h = [1, 3, 5, 7, 9]
h.remove(5)
print(h)

print('--'*45)

i = [1, 3, 5, 7, 9, 11]
for i1 in range(2) :
    data = int(input("리스트에서 삭제할 값을 입력하세요 : "))
    if data in i :
        i.remove(data)
        print(i)
    else :
        print('리스트에 존재하지 않는 값입니다.')
        print(i)

print('--'*45)

# 리스트의 정보 조회 및 정렬하기
#
# - 리스트에서 특정 값의 위치 인덱스를 구하기기기기기긱

j = [10, 20, 30 ,40, 50]
print(j.index(40)) # 40이 위치한 인덱스값 3이 출력
#print(j.index(25)) # 25라는 값이 없어 value error가 발생.

print('--'*45)
