#8.10
A = {a:a**2 for a in range(10)}
print(A)

#8.11
A_set = {num for num in range(10) if num%2==1}
print(A_set)

#8.13
key=('optimist', 'pessimist', 'troll')
value=('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
B = dict(zip(key,value))
print(B)

#8.14

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']
C = dict(zip(titles, plots))
print(C)

#9.1
def good():
    """
    :param n: name
    :return: list name
    """
    return ['Harry', 'Ron', 'Hermione']

A = good()
print(A)
