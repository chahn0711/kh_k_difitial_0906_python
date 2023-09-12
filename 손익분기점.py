# 고정비용 : 1000
# 가변비용 : 70
# 판매비용 : 170
fix, var, sell = map(int, input().split())
if sell <= var: print(-1)
else: print(fix // (sell - var) + 1)