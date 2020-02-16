# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def minEditDistance(str1, str2, m, n):
    if m == len(str1):
        return 0
    
    if n == len(str2):
        return 0
    
    if str1[m] == str2[n]:
        return minEditDistance(str1, str2, m+1, n+1)
    else:
        return 1 + min(minEditDistance(str1, str2, m, n+1), minEditDistance(str1, str2, m+1, n), minEditDistance(str1, str2, m+1, n+1))

str1 = "sunday"
str2 = "saturday"        
print(minEditDistance(str1, str2, 0, 0))        
