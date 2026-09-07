name1=input("Enter your name:")
math_score1=input("Enter your math_score1:")
math_score1=int(math_score1)
fizik_score1=input("Enter your fizik_score1:")
fizik_score1=int(fizik_score1)
name2=input("Enter your name:")
math_score2=input("Enter your math_score2:")
math_score2=int(math_score2)
fizik_score2=input("Enter your fizik_score2:")
fizik_score2=int(fizik_score2)
avg1=(math_score1+fizik_score1)/2
avg2=(math_score2+fizik_score2)/2
if avg1>avg2:
    print(name1)
else:
    print(name2)