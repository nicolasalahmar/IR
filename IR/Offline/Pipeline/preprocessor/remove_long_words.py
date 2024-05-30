def remove_long_words(tokens):
    filtered_tokens = [token for token in tokens if len(token) <= 40]
    return filtered_tokens

# sentence = "This is a sentence with some urla0geunitedkingdom4pd2nfayaax1hwbqxsig1205kc45pexp1164206223 that should be removed"
# print(remove_long_words(sentence))
