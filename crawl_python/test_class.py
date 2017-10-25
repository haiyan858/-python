# test_class.py
'''
class a():
	"""docstring for a"""
	# def __init__(self, arg_a):
	# 	super(a, self).__init__()
	# 	self.arg_a = arg_a

	def run(self):
		# print("a class ......",self.arg_a)
		print("a class ......")

class b(a):
	"""docstring for b"""
	# def __init__(self, arg_b):
	# 	super(a, self).__init__()
	# 	self.arg_b = arg_b

	def run(self):
		# print("b class ......",self.arg_b)
		print("b class ......",)

class c(a):
	"""docstring for c"""
	# def __init__(self, arg_c):
	# 	super(c, self).__init__()
	# 	self.arg_c = arg_c

	def hello(self):
		# print("hello c ......")
		print("hello c ......")

# ac=a("a_class")
# print(ac.run())
# bc=b("b_class")
# print(bc.run())
# cc = c("c_class")
# print(cc.run())
'''

class a():
    def run(self,args_one):
        print('a class...',args_one)

class b(a):
    def run(self,):
        print('b class...')


bc=b()
print(bc.run())

# ac=a()
# print(ac.run())
#
# cc = c()
# print(cc.hello())








