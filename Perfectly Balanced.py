#Given a string containing only the characters x and y,
#  find whether there are the same number of xs and ys.
def balanced(str):
    xcount = 0
    ycount = 0
    for char in str:
        if char == "x":
            xcount += 1
        elif char == "y":
            ycount += 1
    if xcount == ycount:
        return True
    else:
        return False





print(balanced("xxxyyy"))
print(balanced("yyyxxx"))
print(balanced("xxxyyyy"))
print(balanced("yyxyxxyxxyyyyxxxyxyx"))
print(balanced("xyxxxxyyyxyxxyxxyy"))
print(balanced(""))
print(balanced("x"))