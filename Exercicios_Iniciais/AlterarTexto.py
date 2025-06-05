def Remove(text, subtext):
    text = text.replace(subtext, " ")
    return text

text = input("Enter the first text: ")
subtext = input("Enter the subtext to be removed: ")
new = Remove(text, subtext)
print(new)