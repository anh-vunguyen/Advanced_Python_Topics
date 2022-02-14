def checkMagazine(magazine, note):
    possible = True
    dict_words = {}
    for word in magazine:
        if dict_words.get(word) == None:
            dict_words[word] = 1
        else:
            dict_words[word] += 1
    print(dict_words)
    for word in note:
        if dict_words.get(word) < 1:
            possible = False
            break
        dict_words[word] -= 1
    print(dict_words)
    if possible:
        print('Yes')
    else:
        print('No')

magazine = 'apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg'
note = 'elo lxkvg bg mwz clm w'

magazine = magazine.rstrip().split()
note = note.rstrip().split()
checkMagazine(magazine, note)
