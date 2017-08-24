'''
Latin Square challenge for /r/DailyProgrammer
8/21/17 by /u/Rainewood
'''

#Data to analayze
n = int(input("Please enter n, where n is the sidelength of a square array: "))
numsString = input("Please enter the numbers in the array: ").split()
numsToCheck = list(map(int, numsString))

#LatinSquare check function
def latinSquare(n, numsToCheck):
    #Number of elements check
    if n**2 != len(numsToCheck):
        return False
    #Elements fit request check
    for num in numsToCheck:
        if num < 1 or num > n:
            return False
    #Row/Col grab and calculation
    for i in range (n):
        row = set(numsToCheck[i * n + j] for j in range(n))
        if len(row) != n:
            return False

        col = set(numsToCheck[j * n + i] for j in range(n))
        if len(col) != n:
            return False
    return True

#Output
print(latinSquare(n, numsToCheck))
