# 반복문 : 조건이 참인 동안 계속 수행되는 구문
# n = int(input("정수를 입력 하세요 : "))
# sum = 0
# while n:    # 파이썬 정수값이 0이 아니면 참으로 간주함
#     sum += n
#     n -= 1  # 파이썬은 증감 연산자가 없음
# print(sum)

# while True:
#     age = int(input("나이를 입력 하세요 : "))
#     if 0 < age < 200: break
#     print("나이 입력 범위가 벗어났습니다.")

# for 요소 in 시퀀스: 시퀀스의 각 요소를 순회하는데 사용 (자바의 향상된 for문과 동일)
# fruits = ["apple", "banana", "cherry", ["seoul", "korea"]]
# print(fruits[3][1][0])
# for e in fruits:
#     print(e[0])
#
# str1 = "서울시 강남구 역삼동 KH정보교육원"
# for e in str1:
#     print(e, end="/")

# for 변수 in range(시작값, 종료값, 증감값):
n = int(input("정수를 입력 하세요 : "))
sum = 0
for i in range(1, n+1): # 1부터 n+1 미만
    sum += i
print(sum)