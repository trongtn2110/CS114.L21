def _delete(_str):
    newstr= ""
    newstr1 =""
    nguyen_am = ('a', 'y' ,'e', 'i', 'o', 'u')
    for x in _str:
        if x in nguyen_am:
            newstr = _str.replace(x, '')
            _str = newstr
    for x in newstr:
        newstr1 = newstr1 + '.' + x
    return newstr1
_str = input()
_str = _str.lower()
print(_delete(_str))