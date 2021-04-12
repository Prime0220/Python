#   - 2차원 리스트의 요소에 접근하려면 다음과 같이 가로와 세로 인덱스를 적어준다.
#       - 리스트 이름 [세로인덱스][가로인덱스]

list2d = [[10, 20], [30, 40], [50, 60]]
print(list2d[0][0])
print(list2d[1][1])
print(list2d[2][1])
list2d[1][0] = 88
print(list2d)

print("\n", '--' * 45, "\n")

# ### 불규칙한 모양의 2차원 리스트와 동적 추가 ####
#
#   - 가로 세로 인덱스의 크기가 일정하지 않은 리스트도 만드 수 있다.
#   - 아래는 불규칙한 모양의 2차원 리스트의 예이다.

# 인덱스의 크기가 일정하지 않은 2차원 리스트 예

jaggedList = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]
print(jaggedList)

# append 메소드와 extend 메소드를 이용한 리스트 동적 추가

jaggedList[0].append(1111)
print(jaggedList)

print("\n", '--' * 45, "\n")

jaggedList[0].append(2222)
print(jaggedList)

print("\n",'--' * 18,"extend 메소드 사용",'--' * 18,"\n")

jaggedList[2].extend([3333, 4444])
print(jaggedList)

print("\n", '--' * 45, "\n")

# ### 도전문제 ###
#
#   -  5명의 이름, 전화번호, 나이를 입력 받아서 2차원 리스트에 저장하는 프로그램을 작성하시오.
#   - 단 5명의 이름, 전화번호, 나이는 반복문을 활용해서 입력 받으시오.
#
'''
people = [[],[],[],[],[]]

for i in range(5) :
    name, phoneNum, age = input("공백란을 기준으로 이름, 전화번호, 나이를 입력해주세요. : ").split(' ')
    people[i].extend([name, phoneNum, age])
print(people)

print("\n", '--' * 45, "\n")
'''
# #### 불규칙한 모양의 2차원 리스트 자료를 모두 출력하기 ####
#
#   - 리스트의 크기를 알려주는 len함수를 사용하면 리스트의 크기가 불규칙해도 반복문을 사용할 수 있다.
#

jaggedList_ = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]
for i in range(len(jaggedList_)) :
    for j in range(len(jaggedList_[i])) :
        print(jaggedList_[i] [j], end = ' ')
print()



                     
