class math:
	def __init__(self) -> None:
		pass
		
	def add(self,*args) -> str or bool:
		"""
		函数说明：
			求和函数，可以传入多个参数，参数类型可以为int或float，返回值为字符串类型。
			如果传入的参数类型不为int或float，则返回False。
		"""
		try:
			# 遍历*args，将所有参数转换为int/float类型，并求和，返回字符串类型
			result = 0
			for arg in args:
				if isinstance(arg,int) or isinstance(arg,float):
					result += arg
				else:
					return False
			return str(result)
		except:
			return False
	
