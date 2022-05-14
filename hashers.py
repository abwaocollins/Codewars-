def generate_hashtag(s):
    #your code here
    if s == "":
        return False
    else:
        
        res  =[]
        res.append("#")
        for x in s.split():
            res.append(x.capitalize())

        res = "".join(res)

        if len(res) >140:
            return False
        else:
            return res


c = ""

print(generate_hashtag(c))