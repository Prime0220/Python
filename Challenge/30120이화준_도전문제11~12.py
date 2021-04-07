############################ [ 도전문제 11 ] ################################
#
#   - 다음과 같이 출력되도록 중첩된 반복문을 사용해 작성하세요.
#
#   KAAAAAK
#   KAAAAAK
#   KAAAAAK
#   KAAAAAK
#   KAAAAAK

for for_i in range(5) :

    print("K", end='')
    
    for for_j in range(7):
        
        if for_j == 6 :
            print("K")
        else :
            print("A", end='')

print('--'*45)

############################ [ 도전문제 11 ] ################################
#
#   - 다음과 같이 출력되도록 중첩된 반복문을 사용해 작성하세요.
#
#   KKKKKKK
#   AAAAAAA
#   KKKKKKK
#   AAAAAAA
#   KKKKKKK



for for_a in range(5) :

    if for_a % 2 == 0 :
        for for_b in range(7) :
            
            print('K', end='')
        print()
            
    else :
        for for_c in range(7) :
            
            print('A', end='')
        print()

print('--'*45)

