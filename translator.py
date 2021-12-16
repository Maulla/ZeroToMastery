# import pytranslate

# with open('test.txt', mode='r+') as translated_file:
# 	gs = goslate.Goslate()
# 	updated_text = gs.translate(translated_file, 'ja')
# 	updated_text
from translate import Translator

translator= Translator(to_lang="ja")

try:
	with open('test.txt', mode='r') as my_file:
		print(my_file.read())
except FileNotFoundError as e:
	print('Check your file path') 
