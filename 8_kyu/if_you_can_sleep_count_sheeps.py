# If you can't sleep, just count sheep!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    if n <= 0:
        return ""
    else:
        count = ""
        for i in range(1, n + 1):
            count += f"{i} sheep..."
        return count.rstrip()

        
count_sheep(1)