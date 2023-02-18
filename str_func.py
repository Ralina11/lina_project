def upper_first(text):
    '''делает заглавными первые буквы каждого слова в строке, поступившей на вход функции.'''
    out_text = ""
    out_text += text[0].upper()
    for i in range(1,len(text)):
        if text[i-1] == " ":
            out_text += text[i].upper()
        else:
            out_text += text[i]
    return out_text
