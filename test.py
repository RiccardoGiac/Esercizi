def word_break(s:str, wordDict:list[str]) -> bool:

    sl: list[str] = list(s)
    l_compare: list[str] = []
    l_compare2: list[str] = []
    s_attuale: str = sl[0]
    for letter in sl:
        if s_attuale == wordDict[0]:
            l_compare.append(wordDict)
            l_compare2.append(wordDict.pop(0))
            s_attuale = sl[0]
        else:
            s_attuale += letter
                        
    if l_compare == l_compare2:
            return True
    else:
            return False

        
                

print(word_break("catsandog",["cats","dog","sand","and","cat"]))