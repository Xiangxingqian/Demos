#python
def test(name, age = 10):
	print 'name:'+name
	print 'age:',age
	
test("10",20)
test("10")

'''
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'er
fc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gam
ma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'mod
f', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
'''
import math,sys,os,package
print dir(math)
print math.sin(math.pi/2)
print math.log(math.e)
print math.log(2**8,2)
print math.log1p(math.e-1)
print math.pow(2,5);print math.exp(5);print math.pow(math.e,5);print math.__doc__; print math.__name__;print math.__package__

package.test1()

list = [1,2,3,"4",5,(6,2,5*2,5**2)]
print sys.path
print list;print os.path;print os.path.split(os.path.realpath(__file__))

#执行shell命令
str = os.system("java -version")
print str
str = input("Please enter a line\n")
print str