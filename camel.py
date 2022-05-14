
def to_camel_case(text):
    import re

    t = re.split(r"[_-]",text)

    for i in range(1,len(t)):
        t[i] = t[i].capitalize()

    return ''.join(t)

print(to_camel_case('a_pippi-Was_evil'))

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

