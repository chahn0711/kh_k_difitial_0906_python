# 내장함수 : 파이썬이 기본적으로 제공, import가 필요 없음
# 외장함수 : 파이썬이 기본적으로 제공, import가 필요함.

# 큰값 작은값 찾기
print(max(1,2,3,4,45,56,7,777,88,99,100))
print(min(1,2,3,4,45,56,7,777,88,99,100))

# 총 합 구하기
print(sum([1,2,3,4,45,56,7,777,88,99,100]))  # 리스트에 대한 총 합
print(sum((1,2,3,4,45,56,7,777,88,99,100)))  # 튜플에 대한 총 합
num = list(map(int, input("정수값 입력 : ").split()))
print(f"입력 받은 수의 총 합 : {sum(num)}")
print(f"입력 받은 수의 평균 : {sum(num)/len(num)}")

# 몫과 나머지 구하기
print(f"몫과 나머지 : {divmod(10, 4)}")  # 튜플의 동작 원리

# 여러개의 값을 한번에 입력 받아 리스트로 만들기
# 최대값, 최소값, 합계, 평균
# 합계에 몫과 나머지 : 5(나누는 수)
n = list(map(int, input("정수를 입력 하세요 : ").split()))
print(f"최대값 : {max(n)}")
print(f"최소값 : {min(n)}")
print(f"합계 : {sum(n)}")
print(f"평균 : {sum(n) / len(n)}")
print(f"몫과 나머지 : {divmod(sum(n),5)}") # 몫과 나머지 출력하는 함수

# 정렬
my_list = [1,2,3,4,45,56,7,777,88,99,100]
# 내림 차순
print(sorted(my_list, reverse=True))