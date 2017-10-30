import codecs
encodings = ['utf-8', 'windows-1250', 'windows-1252']
for e in encodings:
	try:
		fh = codecs.open('STUDY_PI.csv', 'r', encoding=e)
		fh.readlines()
		fh.seek(0)
	except UnicodeDecodeError:
			print('got unicode error with %s , trying different encoding' % e)
	else:
		print('opening the file with encoding:  %s ' % e)
	break 