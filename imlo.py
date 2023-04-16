from transliterate import to_cyrillic,to_latin


def translit(msg):
    matn=msg
    if(matn.isascii()):
        return (to_cyrillic(matn))
    else: return (to_latin(matn))
