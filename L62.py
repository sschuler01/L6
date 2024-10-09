#the authors' names are: Serenity and Mac

def find_perf_num():
    n = int(input("What is the number?\n"))
    total = 0
    for x in range(1, n):
        if n % x == 0:
            total = total + x
    if total == n:
        return True
    else:
        return False
        
print(find_perf_num())
