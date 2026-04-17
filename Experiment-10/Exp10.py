s = input("Enter the source string:")
t = input("Enter the target string: ")

def min_edit_distance(s,t):
    n = len(s)
    m = len(t)

    D = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
      D[i][0] = D[i-1][0] + 1

    for j in range(1,m+1):
      D[0][j] = D[0][j-1] + 1

    for i in range(1,n+1):
      for j in range(1,m+1):
          if(s[i-1]==t[j-1]):
              cost = 0
          else:
              cost = 1

          D[i][j] = min(
              D[i-1][j] + 1,
              D[i-1][j-1] + 1,
              D[i-1][j-1] + cost
          )
    return D[n][m]


distance = min_edit_distance(s,t)
print(distance)
