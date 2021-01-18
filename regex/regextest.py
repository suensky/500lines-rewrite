import re

def pretty_print(x):
    print("span: " + str(x.span()) + " word: " + x.group())

#Check if the string contains "a" followed by exactly two "l" characters:
def testGroup():
    txt = "Theall rain in Spain falls mainly in theall plain!"
    x = re.search("al{2}", txt)
    print(x.span())
    print(x.string)
    print(x.group())

def testStringStart():
    text = "The rain in Spain starts"
    x = re.search(r"\ATh", text)
    print(x)

    x = re.search(r"\Arain", text)
    print(x)

def testStringEnd():
    text = "first second last"
    x = re.search(r"ast\Z", text)
    print(x)

    x = re.search(r"second\Z", text)
    print(x)

def testStartWithWord():
    text = "The aina rain in Spain starts ainb"
    x = re.search(r"\bain", text)
    print(x)

    x = re.search(r"ain\b", text)
    print(x)

def testNotStartWithWord():
    text = "The aina rain in Spain starts ainb"
    x = re.search(r"\Bain", text)
    pretty_print(x)

    x = re.search(r"ain\B", text)
    pretty_print(x)
# testGroup()
# testStringStart()
# testStringEnd()

testStartWithWord()
testNotStartWithWord()


