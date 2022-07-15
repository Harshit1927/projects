def op(a,b,p):		#This function gives the output after doing operation "p" on number a and b, if the operator "p" is not valid (i.e. not in ["+","-","*","/"] then the output is number a)
	c=a
	k=["+","-","*","/"]
	if p not in k:
		c=a
	if p=="+":
		c=a+b
	elif p=="-":
		c=a-b
	elif p=="*":
		c=a*b
	elif p=="/":
		c=a/b
	elif p=="(" or p==")":
		return "Error"
	return c
def postf(l):
	ope=["+","-","*","/"]
	oparens=["("]
	cparens=[")"]
	k=["1","2","3","4","5","6","7","8","9","0"]
	do=["."]
	s=[]
	ls=[]
	i=0
	while (i<len(l)):
		if l[i] in oparens:
			ls+=[l[i]]
			i+=1
		elif l[i] in ope:
			if l[i]=='*' or l[i]=='/':
				while (len(ls)>0 and (ls[-1]=='*' or ls[-1]=='/')):
					s+=[ls[-1]]
					ls.pop()
			else:
				while (len(ls)>0 and ls[-1]!='('):
					s+=[ls[-1]]
					ls.pop();
			ls+=[l[i]]
			i+=1
		elif l[i] in cparens:
			while (ls[-1]!='('):
				s+=[ls[-1]]
				ls.pop()
			ls.pop()
			i+=1
		else:
			s1=""
			while i<len(l) and (l[i] in k or l[i]=='.'):
				s1+=l[i]
				i+=1
			s+=[s1]
	while (len(ls)>0):
		s+=ls[-1]
		ls.pop()
	return s
def evaluate(l):
	s=postf(l)
	ls=[]
	k=["1","2","3","4","5","6","7","8","9","0"]
	do=["."]
	for j in s:
		if (j[0] in k or j[0] in do):
			ls+=[float(j)]
		else:
			num1=ls.pop()
			num2=ls.pop()
			ls+=[op(num2, num1, j)]
	return ls.pop()
print(evaluate("1+2*(345.6+4*5)-6"))
