import FileEncoder

def StartEncode(): 
	# encode a file/text_msg
	# file => EncodeFile(), text_msg => EncodeText()
	q = input('Encrypt (F)ile, (T)ext : ')
	if q=='f' or q=='F': 
		EncodeFile()
	elif q=='t'or q=='T': 
		EncodeText()
	else:
		print('Invalid Choice')

def EncodeFile():
	# param<filename,password,save_as_new_name>
	# open_file => read() => Decrypt() => save_as_new_name 
	filename = input('Filename : ') + '.txt'
	code = ''

	with open(filename,'r') as f:
		msg = f.read()
		pwd = input("password for encryption : ")
		code = FileEncoder.Encrypt(msg,FileEncoder.EncryptionKey(FileEncoder.KeyGen(pwd)))
	filename = input('Save as : ') + '.txt'
	SaveAs(code,filename)

def EncodeText():
	# param<text,password,append/create> 
	# append => filename, save_as(text,filename,open_type = 'a')
	# end append => append_more/home
	# create => filename, save_as(text,filename)
#	text = input('Message : ') + "\n"
	print('',end='\r')
	filename = input('Append messeges to : ') + '.txt'
	pwd = input('password for encryption : ')
	while True:
		text = input('Message : ') + "\n"
		q = input('(C)ontinue, (H)ome : ')
		if q=='h' or q =='H':
			code = FileEncoder.Encrypt(text,FileEncoder.EncryptionKey(FileEncoder.KeyGen(pwd)))
			SaveAs(code,filename,'a')
			break
		elif q=='c'or q=='C':
			code = FileEncoder.Encrypt(text,FileEncoder.EncryptionKey(FileEncoder.KeyGen(pwd)))
			SaveAs(code,filename,'a')
		else:
			print("\nInvalid choice, last message cannot be appended\n\n")
			break

def StartDecode():
	# param<filename,password>
	# display/save_as
	# display => print(msg)
	# save_as(msg,new_filename)
	msg = DecodeFile()
	q = input('(D)isplay, (S)ave_as : ')
	if q=='d' or q=='D':
		print('\n\n'+ msg + '\n')
	elif q=='s'or q=='S':
		filename = input("Save as : ") + '.txt'
		SaveAs(msg,filename)
	



def DecodeFile():
	filename = input('Filename : ') + '.txt'
	pwd = input("password for encryption : ")
	with open(filename,'r') as f:
		code = f.read()
		message = FileEncoder.Decrypt(code,FileEncoder.KeyGen(pwd))
		return message


def SaveAs(_msg,filename, open_type = 'w'):  # save_as(text,filename,open_type = 'w')
	with open(filename,open_type) as f:
		f.write(_msg)
