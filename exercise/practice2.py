python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "java"))
index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)
print(python.count("n"))


python = "Python is Amazing"
print("나는 올해 %d살" % 20)
print("나는  %s를 좋아한다" % "파이썬")
print("Apple은 %c로 시작" % "A")

print("나는  %s를 좋아한다" % 20)
print("나는  %s색과 %s를 좋아한다" % ("파란", "빨간"))

print("나는  {}를 좋아한다" .format(20))
print("나는  {}색과 {}를 좋아한다" .format("파란", "빨간"))
print("나는  {1}색과 {0}를 좋아한다" .format("파란", "빨간"))

print("나는 {age}살이고 {color}를 좋아해요" .format(age=20, color="빨간"))

age=20
color = "빨간색"
print(f"나는 {age}살이고 {color}을 좋아해요")