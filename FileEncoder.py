def KeyGen(password): # Generates a key from password
	indx = 0
	matrixA = [None]*3
	for i in range(3):
		for j in range(3):
			if(matrixA[i]==None):
				matrixA[i] = [None]*3
			matrixA[i][j] = int(password[indx])
			indx +=1
	return matrixA

def EncryptionKey(_key): # Generates a encryption key from a key
	enc = [None]*10
	for i in range(3):
		for j in range(3):
			enc[_key[i][j]] = str(i)+str(j)
	return enc

def Encrypt(_msg = " ",encyption_key = [0]): # Takes encryption key
	initialize_msg = []
	for i in _msg:
		initialize_msg.append(str(ord(i)))
	coded_msg = ''
	for i in initialize_msg:
		for j in i:
			if int(j)!=0:
				coded_msg += encyption_key[int(j)]
			else:
				coded_msg +='44'
		coded_msg += ' '
	return coded_msg

def Decrypt(_msg=' ',_key=[0]): # Takes Generated Key
	code = _msg.split()
	partial_decrypt = []
	for i in code:
		temp = ''
		for j in range(0,len(i)-1,2):
			if int(i[j])!=4:
				temp += str(_key[int(i[j])][int(i[j+1])])
			else:
				temp+='0'
		partial_decrypt.append(temp)
	decrypted_msg = ''
	for i in partial_decrypt:
		decrypted_msg+= chr(int(i))
	return decrypted_msg


# For testing purposes .......
'''
pwd = input('Enter the password : ')
key = KeyGen(pwd)
print('The key is :',key)
enc_key = EncryptionKey(key)
print('Encryption protocol is :',enc_key)
msg = input('Enter the msg : ')
encrypted_msg = Encrypt(msg,enc_key)
SaveAsText(encrypted_msg,'msg.txt')
print(Decrypt(encrypted_msg,key))
DecryptFrom()
'''

# 968175243

'''

0101 1100 1102 0212 0222 2220 0111 1120 0112 1101 1101 0100 1102 1110 0100 2220 0222 1100 
1101 0212 0221 1122 1100 1102 2220 1202 102010 101010 101011 2220 0000 0011 101044 2220 104400 
101010 104444 104412 104420 102010 2220 104412 101044 101020 101011 101001 2220 101001 104410 
102044 101001 2220 104400 104410 101012 101012 0011 104422 104410 2220 0011 101044 104444 2220
0011 104444 104444 2220 0011 2220 101044 104410 101000 2220 104402 104412 101044 104410 2220
0000 104421 0011 101021 0011 0000 101001 104410 101021 2220 101001 101010 2220 104412 
101001 2220 104402 104412 104411 104410 2220 1202 2220 101001 104410 102044 101001 2220 0110 
2220 104412 101044 101020 101011 101001 2144 2200 1111 104410 101012 101012 0011 104422 
104410 2220 1202 2220 2200 2110 2220 2122 2220 2144 2200 0020 101044 2200 2110 

'''
