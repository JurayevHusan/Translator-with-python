from googletrans import Translator

tr= Translator()
text = input("Enter Your Text : ")
lg = input("Enter Your Language : ")
a = tr.translate(text , dest=lg)
print(lg,"the language : ",a.text)