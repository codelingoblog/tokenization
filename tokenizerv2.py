import re
regex = "[a-zA-Z]+"
sentence = """At the age of one year old, Harry had somehow survived a curse from the greatest Dark sorcerer of all time, Lord Voldemort, whose name most witches and wizards still feared to speak."""
tokenized_words = re.findall(regex,sentence)
print tokenized_words