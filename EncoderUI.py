import FileEncoder

def StartEncode(): 
	# encode a file/text_msg
	# file => EncodeFile(), text_msg => EncodeText()
	q = input('Encode file/Encode text (f/t)  : ')
	if q=='f': 
		EncodeFile()
	elif q=='t': 
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
	filename = input('Save as (name of new file with extension) : ')
	SaveAs(code,filename)

def EncodeText():
	# param<text,password,append/create> 
	# append => filename, save_as(text,filename,open_type = 'a')
	# end append => append_more/home
	# create => filename, save_as(text,filename)
	# BONUS HINT: solution is in the code and this project includes code
	text = input('Message : ') 
	pwd = input('password for encryption : ')
	open_type = input('append/create (a/c) : ')
	filename = input('Filename : ') + '.txt'
	code = FileEncoder.Encrypt(text,FileEncoder.EncryptionKey(FileEncoder.KeyGen(pwd)))
	if open_type=='a':
		while True:
			SaveAs(code,filename,open_type)
			q = input('Continue_Append/Home (a/h) : ')
			if q=='h':
				break
			text = input('Message : ')
			code = FileEncoder.Encrypt(text,FileEncoder.EncryptionKey(FileEncoder.KeyGen(pwd)))
	elif open_type=='c':
		SaveAs(code,filename)
	else:
		print("Invalid open_type")

def StartDecode():
	# param<filename,password>
	# display/save_as
	# display => print(msg)
	# save_as(msg,new_filename)
	msg = DecodeFile()
	q = input('display/save_as (d/s) : ')
	if q=='d':
		print('\n\n'+ msg + '\n')
	elif q=='s':
		filename = input("Save as (name of new file with extension) : ")
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
