source = input("Enter the string1: ")
target = input("Enter the string2: ")

n = len(source)
m = len(target)


D = [[0] * (m + 1) for _ in range(n + 1)]


for i in range(n + 1):
    D[i][0] = i   

for j in range(m + 1):
    D[0][j] = j  
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if source[i - 1] == target[j - 1]:
            cost = 0
        else:
            cost = 1

        D[i][j] = min(
            D[i - 1][j] + 1,      
            D[i][j - 1] + 1,      
            D[i - 1][j - 1] + cost  
        )

print("Source string:", source)
print("Target string:", target)
print("Minimum number of Operations required:", D[n][m])
