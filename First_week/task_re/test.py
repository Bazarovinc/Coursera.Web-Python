import re
from regexp import calculate


def findall(regexp):
    text = """
    x-=-101c-=+101x-=y+101y+=10a=b+100c-=-101b+=b+100a=+1c-=101y+=+10-expected1
    """

    return re.findall(regexp, text)


result = calculate({'a': 10, 'b': 20, 'c': 30}, findall)
correct = {"a": -98, "b": 196, "c": -686}
if result == correct:
    print("Correct")
else:
    print("Incorrect: %s != %s" % (result, correct))
