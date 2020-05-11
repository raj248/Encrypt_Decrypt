import EncoderUI 

def main():
	print('------Enter filenames without it\'s file extensions------')
	print('\n------Type q to quit program, and help for any help-----\n')
	q = input("(E)ncrypt, (D)ecrypt, (H)elp, (Q)uit: ")
	if q=='e' or q=="Q":
		EncoderUI.StartEncode()
	elif q=='d' or q=='D':
		EncoderUI.StartDecode()
	elif q=='q' or q=='Q':
		quit()
	elif q=='h' or q=='H':
		try:
			with open('readme.txt','r') as f:
				print(f.read())
		except:
			print('\nSorry you don\'t have the readme file for help support\n')
	else:
		print('Invalid Choice')
	main()



main()
