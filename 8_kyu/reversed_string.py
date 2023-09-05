# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'
def solution(string):
    reversed_string = "".join(reversed(string))
    return(reversed_string)


solution("world")
solution("dos")