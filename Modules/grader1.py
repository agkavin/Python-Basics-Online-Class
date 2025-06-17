score = int(input("Enter Science score: "))

if score >= 90:
    grade = 'A'
elif score >= 75:
    grade = 'B'
elif score >= 60:
    grade = 'C'
else:
    grade = 'D'

print("Science Grade:", grade)
