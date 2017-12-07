import argparse
class Parameter():
	"""docstring for ClassName"""
	def __init__(self):
		self.parser = argparse.ArgumentParser(description="BD Exploits")
		self.group = self.parser.add_mutually_exclusive_group()
		self.group.add_argument("-d", "--day", help="Hace Cuantos Dias",type=int)
		self.group.add_argument("-m", "--month", help="Hace Cuantos meses",type=int)
		self.group.add_argument("-y", "--year", help="Hace Cuantos años",type=int)
		self.parser.add_argument("-f","--date", help="Rango Fecha AA-MM-DD::AA-MM-DD")
		self.parser.add_argument("-p","--pag", help="Pages",type=int,default=10)
		self.parser.add_argument("-pi","--pini", help="Pag inicio",type=int,default=1)
		self.parser.add_argument("-allp","--allpages", help="Pag inicio",type=int,default=0)
		self.parser.add_argument("-t","--type", help="type",type=int)

	def get_agurments(self):
		return self.parser.parse_args()