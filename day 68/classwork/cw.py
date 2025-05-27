def split_by_dollar(text):
    return text.split("$")

sentence = "this$is$my$code$$please$check$it"
result = split_by_dollar(sentence)
print(result)
