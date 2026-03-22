punctuations = "`~!@#$%^&*()_+-={}[]:;''?/>.<,\|"
res = ""

s = input("Enter the string: ")
for i in s:
  if i not in punctuations:
      res+=i
print("\n")
print(res)
print(res.split())
