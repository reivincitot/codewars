# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'
def solution(string):
    new_string = string.replace(string[0], string[-1])
    print(new_string)
    return new_string

solution("world")
solution("dos")