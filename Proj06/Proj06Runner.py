def run(str, sep):
   # """Returns a substring of any given string based upon a given range of characters before and after the substring"""

    r = ['Elena Stefanova', str, sep]
    b = 0
    i = str.find(sep, 0)

    while (i > -1):
       r.append(str[b:i])
       b = i+1
       i = str.find(sep, b)

    r.append(str[b:])

    return r
