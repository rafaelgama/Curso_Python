# instalando biblioteca externa
import emoji
print(emoji.emojize("Olá mundo :skull:"))
print(emoji.demojize('Olá mundo 👍'))
#From the list of unicodes, replace “+” with “000”. For example – “U+1F600” will become “U0001F600” and prefix the unicode with “\” and print it.
#https://home.unicode.org/
print(emoji.emojize('Olá mundo \U0001F606', use_aliases=True))