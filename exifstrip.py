import Image, os, sys

file_image = raw_input('Enter the location of the file: ')

if os.path.isfile(file_image):
	directory, filename = os.path.split(file_image)

	image = Image.open(file_image)

	data = list(image.getdata())

	image_without_exif = Image.new(image.mode, image.size)

	image_without_exif.putdata(data)

	image_without_exif.save(directory + "/Exif_Stripped_" + filename)

	print("[*] File Saved: %s/Exif_Stripped_%s" %(directory, filename))

	sys.exit(0)

else:
	print("[*] Image Path Does not Exist")
	sys.exit(1)
