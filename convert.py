import base64
from sys import argv

def convert_file(filename, des_fmt):
	with open(filename, 'rb') as f:
		f_read = f.read()
		encoded = base64.encodestring(f_read) 
		decoded = base64.decodestring(encoded) #Decoded string ready to be written

	filename = filename.split('.')[0]
	new_fmt	= lambda x : x + '.' + des_fmt

	with open(new_fmt(filename), 'wb') as new_file:
		new_file.write(decoded)

	return new_fmt(filename) + ' Has been converted to ' + des_fmt

#Check if any files were selected
check = lambda x : True if x > 2 else False

if check(len(argv)) == True:
	#If any of the files are selected
	for i in range(2,len(argv)): #Start from argv[1].. (First )
		result = convert_file(argv[i], argv[1])
		print result

else:
	print 'Please select files you want to convert'




