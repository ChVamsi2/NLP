import re
s = input("Enter the string: ")
match = re.search(r's$',s)
if match:
    print("Parsing is successful and is plural word")
else:
    print("Parsing is not successful and is not plural word")
