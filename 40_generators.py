def all_variants(text):
    i = 0
    l = 1
    word = text[i:i+l]
    while l <= len(text):
        yield word
        i += 1
        if i + l > len(text):
            i = 0
            l += 1
        word = text[i:i+l]


a = all_variants("abc")
for i in a:
    print(i)
