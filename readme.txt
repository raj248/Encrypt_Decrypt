INTRODUCTION----------------------------------

ED_1 is an console application written in python programming language.

ED_1's purpose is to encode sensitive files (txt,csv) so that it remains hidden from or inaccessible to unauthorized users. It helps protect private information, sensitive data and can enhance security of communication between client apps and servers

Encryption is important because it allows you to securely protect data that you don't want anyone else to have access to.

TUTORIAL/ HOW TO USE PROGRAM----------------------------

ED_1 can encrypt and decrypt data from '.txt' file.

-Encrypting :
	Choose 'e' on the startup menu to start encrypting.

	Encrypt either a file('f') or a text message('t')
	- you can encrypt a '.txt' file directly and save the decrypted message directly in a new file 
	parameters : filename, encryption password, filename of file containing encrypted message

	- you can encrypt a text message and append('a') it to a file or create('c') a new file. you can also append to a single file multiple time in one session
	parameters : To append --> text, filename, password
				 To create --> text, filename, password, name of new file

	NOTE: - Password should be a 9 digit number without any repeation of any number. Range for each digit --> 1 to 9
		  - All files should be in same directories
		  - while writing filename extension type of file should be ignored unless mentioned


-Decrypting :
	Choose 'd' on the startup menu to start decrypting from a file

	parameters : filename, password, (conditional)name of file to save decrypted text

	Decrypt a file by giving filename and appropriate password, either display('d') message on the screen or save('s') it with custom name



CODE INSIGHTS-----------------------------


-Functions :
	
	FileEncoder.py : - KeyGen()
					 - EncryptionKey()
					 - Encrypt()
					 - Decrypt()

	EncoderUI.py : - StartEncode()
				   - EncodeFile()
				   - EncodeText()
				   - StartDecode()
				   - DecodeFile()
				   - SaveAs()

	Encoder.py : - main()


-Dependencies :
	
	Encoder.py imports Encoder.py imports FileEncoder.py
	if all three file are not present together, ModuleNotFoundError is raised


-FileEncoder.py : 
	 
	It contains implementation of Encryption algorithm as functions

	-KeyGen() : 
		generates key(3x3 matrix) from password

		it takes password as an argument which consists of 9 unique numbers. Each number is from 1 to 9

		It iterate through a 3x3 matrix and password, then assigns elements of matrix corresponding to the password

			say if password is 123456789
			then key = [[1,2,3]
						[4,5,6]
						[7,8,9]]

		parameters : password(str)
		returns : 3x3 matrix (this is the key)
		key : it is used directly for decryption 
			  or can be passed as an argument in EncryptionKey()
			  to generate a emcryption key


	-EncryptionKey() :
		generates an encryption key which is used to encrypt a file
		takes key(generated from KeyGen()) as an argument

		it creates a list containing positions of all elements
		in matrix each element of the matrix represents index value 
		of encryption_key(list)  

		say if key = [[1,2,3]
					  [4,5,6]
					  [7,8,9]]

		then encryption_key = [None,'00','01,'02,'10','11','12','20','21','22']

		encryption_key[element] = position_in_matrix

		parameter : key(3x3 matrix)
		returns : encryption_key(list)


	-Encrypt : 
		It encrypts the text according to the encryption_key
		it takes text and encryption key as an argument 

		encryption takes place in 2 steps:
			1.	Generating ordinal list: iterate through text and
				appends ordinal values of each character in a list
				named initialize_msg as string

			2.	Replacing ordinal values with code: then it iterate
				through each ordinal value to pick each digit, then
				uses that digit/number as index value of
				encryption to access and append that value in a string 
				containing coded message. If the digit is 0 then coded
				value is '44'

		parameters : _msg(str)(default = ' '), encryption_key(list)(default = [0])

		returns : coded_msg(str)

		say if text = 'Hello' 
		and encryption_key = [None,'00','01,'02,'10','11','12','20','21','22']
		then initialize_msg = ['72', '101', '108', '108', '111']
		and coded_msg = '2001 004400 004421 004421 000000 '


	-Decrypt : 
		It is the reverse of Encrypt() and generates readable data
		from encrypted files
		it takes coded message(str) and key(generated from KeyGen()) 
		as arguments

		decryption takes place in 2 steps:
			1.	Replacing code with ordinal values: first, it makes
				a list of code using split() on coded_msg.
				Then it iterates through each list and each coded_msg
				accessing 2 elements in each iteration, then access 
				element in the key(3x3 matrix) and add it to a temporary string.
				temporary string is appended to a list named partial_
				decrypt after each iteration of outer loop
				whenever 4 is found in code then it appends 0 as ordinal values

			2.	then iterating through partial_decrypt list containing
				ordinal values, each ordinal value is converted back 
				to a character and added to decrypted_msg string

		parameters : _msg(str), _key(3x3 matrix)(generated from KeyGen())

		returns : decrypted_msg(str)

		say if coded_msg = '2001 004400 004421 004421 000000 '
		and key = [[1,2,3]
				   [4,5,6]
				   [7,8,9]]
		then partial_decrypt = ['72', '101', '108', '108', '111']
		and decrypted_msg = 'Hello'



-EncoderUI.py :

	It contains implementation of user interface

		-StartEncode() :
			Pushes program flow to encode a file or text depending 
			on user's choice
			if choice is 'f' then it calls EncodeFile() 
			if choice is 'd' then it calls EncodeText()
			and if none of the choice matches then print Invalid choice

		-EncodeFile() : 
			input : filename, password, newfilename 

			Encrypt contents of a '.txt' file, then saves
			it as newfilename. It read code from a file then calls
			Encrypt() from FileEncoder.py and passes code and password,
			then it saves the encrypted_msg by passing appropriate
			arguments in SaveAs()

		-EncodeText() : 
			input : text_msg, password, filename,choice<append/create>
			
			encrypt text_msg and append it to a file filename or create
			a new file named filename

			uses 'while True' to append multiple times in a single file
			and open_type = 'a' is passed in SaveAs() to open file in
			append mode

		-StartDecode() : 
			input :  choice<display/save>, (if choice is 's') filename

			calls DecodeFile(), then display or save decypted text
			according to user's choice

			if choice is 'd' then display msg
			if choice is 's' then take input<filename> and call SaveAs()

		-DecodeFile() : 
			input : filename, password

			takes filename of file to decrypt as input then 
			calls Decrypt() from FileEncoder.py to return a decrypted_msg

			returns : decrypted_msg(str)

		-SaveAs() : 
			parameters : text(str), filename(str), open_type(str)(default = 'w')

			opens a file named filename in open_type mode and write text
			in file
-Encoder.py :
	
	This is driver program of application

	main():
		input : choice<Encrypt/Decrypt>

		takes user's choice to push program flow to encrypt or decrypt
		a file by calling StartEncode() and StartDecode() respectively
		from EncoderUI

		if choice is 'e' then start encrypting
		if choice is 'd' then start decrypting
		if choice is 'h' or 'help' then print this readme.txt
		if choice is 'q' then quit program



	