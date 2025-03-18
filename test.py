import emoji 

def text_to_emoji(text):
  return emoji.emojize(text,language='alias')

text = 'i love :pizza: and :sad:'
convert = text_to_emoji(text)
print(convert)