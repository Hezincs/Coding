A = input()
B = input()
print(A + " " + B)
#end

A= input()
B= input()
print(int(A)-int(B))
#end

word = input()
repeat = 50/len(word)
result =""
for i in range(int(repeat)):
  result += word
print(result)
#end

A = input()
if int(A) > 50:
  print("yes dream big")
else:
    print("on the small side")
    #end

num1= int(input())
operator= input()
num2 = int(input())
result= ""

if operator == "*":
  result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "+":
      result = num1 + num2
elif operator == "-":
        result= num1 - num2
print(result)
#end
