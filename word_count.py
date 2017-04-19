def words(wordstring):
    worddict = {}

    for i in wordstring.split():
        if i not in worddict:
            try:
                worddict[int(i)] = wordstring.count(i)
            except ValueError:
                worddict[i] = wordstring.count(i)

    return worddict

print(words('words  : chocolate!!!& iceream & 10 cookies'))