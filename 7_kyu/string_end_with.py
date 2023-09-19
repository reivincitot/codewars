# DESCRIPTION:
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
def solution(text, ending):
    # your code here...
    if len(ending)< 2:
        return False
    elif len(ending)>2:
        return False
    elif text[-2:]==ending:
        return True
    
solution( "samurai", "ai"    )
solution( "ninja",   "ja"    )
solution( "sensei",  "i"     )
solution( "abc",     "abc"   )
solution( "abcabc",  "bc"    )
solution( "fails",   "ails"  )