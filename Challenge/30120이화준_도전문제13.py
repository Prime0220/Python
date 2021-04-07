# ### [도전문제 13] ###
# 다음과 같이 출력되도록 중첩된 반복문을 사용해 작성하세요

# A
# AA
# AAA
# AAAA
# AAAAA
# AAAAAA


for a in range(7) :
    for b in range(1, a+1) :
        print('A', end='')
    print()
