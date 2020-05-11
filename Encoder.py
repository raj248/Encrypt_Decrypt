import EncoderUI 

def main():
	print('------Enter filenames without it\'s file extensions------')
	print('\n------Type q to quit program, and help for any help-----\n')
	q = input("Encrypt/Decrypt (e/d) : ")
	if q=='e':
		EncoderUI.StartEncode()
	elif q=='d':
		EncoderUI.StartDecode()
'''	if q=='h'or'help':
		# print readme.txt
		try:
			with open('readme.txt','r') as f:
				print(f.read())
		except:
			print('\nSorry you don\'t have the readme file for help support\n')
	elif q=='q':
		quit()
'''	else:
		('Invalid Choice')
	main()



main()
