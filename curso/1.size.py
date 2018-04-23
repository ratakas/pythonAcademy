import sys
import math
suffixez={1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
print (sys.version)

def approximate_size(size,a_kilobyte=True):
	if size<0:
		raise ValueError('number must be non-negative')

	multiple = 1024 if a_kilobyte else 1000
	for suffix in suffixez[multiple]:
		size /=multiple
		if size < multiple:
			return '{0:.1f}{1}'.format(size,suffix)

	raise ValueError('number too large')

if __name__ == '__main__':
	print(approximate_size(1000000000,False))
	print(approximate_size(1000000000000))
	print(int(math.pi))
