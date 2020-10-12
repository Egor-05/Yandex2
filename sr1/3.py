def rabbits_hole(*args, eliminate_direction='', start_point=(0, 0)):
    if len(args) == 0:
        raise EmptyInstructionError('No instructions')
    a = ['west', 'east', 'north', 'south']
    if eliminate_direction not in a and \
       eliminate_direction != '':
        raise TypeError('Not available value')
    if eliminate_direction != '':
        a1 = a.index(eliminate_direction)
        del a[a1]
        a.insert(a1, '')
    s = [start_point[0], start_point[1]]
    for i in args:
        if i[0] == a[0]:
            s[0] -= i[1]
        elif i[0] == a[1]:
            s[0] += i[1]
        elif i[0] == a[2]:
            s[1] += i[1]
        elif i[0] == a[3]:
            s[1] -= i[1]
    if s == [start_point[0], start_point[1]]:
        raise WrongPathError('This is a wrong place')
    return (s[0], s[1])


class EmptyInstructionError (Exception):
    pass


class TypeError(Exception):
    pass


class WrongPathError(Exception):
    pass


args = [('west', 3), ('east', 3)]


print(rabbits_hole(*args))