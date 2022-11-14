letter = '''Dear <|NAME|>,
\tI am happy to tell about your selection
\tYour are selected in softwaring field
\tYour are great day ahead
\n\tThank and Regard
Date: <|DATE|>'''
name = input("Enter your name\n")
date = input("Enter today date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)