def day(day,month,year):
	k=day
	m=0
	y=year
	C=0
	D=0
	if 3<=month<=12:
		m=month-2
	elif month==1:
		m=11
	elif month==2:
		m=12
	if month==1 or month==2:
		y-=1
	C=y//100
	D=y%100
	F=k+ ((13*m-1)//5) +D+ (D//4)+(C//4)-2*C
	return F%7
def toString(n):
	k=[0,1,2,3,4,5,6,7,8,9]
	c=["0","1","2","3","4","5","6","7","8","9"]
	a=""
	i=n
	while i>=10:
		if i>=10:
			a=c[i%10]+a
			i=i//10
	if i<10:
		a=c[i]+a
	return a
def ed(n):
	c=""
	if n==1:
		c="Mo"
	elif n==2:
		c="Tu"
	elif n==3:
		c="We"
	elif n==4:
		c="Th"
	elif n==5:
		c="Fr"
	elif n==6:
		c="Sa"
	elif n==0:
		c="Su"
	return c
def check_lp(y):
	if y%4!=0:
		return False
	elif y%100!=0:
		return True
	elif y%400!=0:
		return False
	else:
		return True
def mon(i,y):
	f=open('Calendar.txt','w+')
	n=day(1,i,y)
	m=["December "," January ","February ","  March  ","  April  ","   May   ","   June  ","   July  ","  August ","September"," October ","November "]
	f.write("               -"+m[i%12]+"-         \n")
	f.write("    M    T    W    T    F    S    S")
	d=[2,3,4,5,6]
	exd=[1,3,5,7,8,10,12]
	nd=[4,6,9,11]
	if day(1,i,y)==0:
		n+=7
	else:
		n=day(1,i,y)
	while n>=0:
		if n>0 and n<day(1,i,y):
			f.write("   "+"  ")
			n-=1
		elif n>0 and day(1,i,y)==0:
			if n==7:
				f.write("\n")
			f.write("   "+" ")
			n-=1
		elif n==0 and day(1,i,y)==0:
			f.write("      1"+"\n")
			n-=1
			if i in exd:
				for k in range(2,32):
					if k==31 and day(31,i,y)==1:
						f.write("   "+toString(k)+"")
					elif k==31:
						f.write(" "+toString(k)+"")
					elif day(k,i,y)==1 and k<10:
						f.write("    "+toString(k)+"  ")
					elif day(k,i,y)==1 and k>=10:
						f.write("   "+toString(k)+"  ")
					elif day(k,i,y) in d and k<10:
						f.write("  "+toString(k)+"  ")
					elif day(k,i,y) in d and k>=10:
						f.write(" "+toString(k)+"  ")
					elif day(k,i,y)==0 and k<10:
						f.write("  "+toString(k)+"\n")
					elif day(k,i,y)==0 and k>=10:
						f.write(" "+toString(k)+"\n")
				t=day(31,i,y)
				while t%7>0:
					f.write("     ")
					t+=1
			elif i in nd:
				for k in range(2,31):
					if k==30 and day(30,i,y)==1:
						f.write("   "+toString(k)+"")
					elif k==30:
						f.write(" "+toString(k)+"")
					elif day(k,i,y)==1 and k<10:
						f.write("    "+toString(k)+"  ")
					elif day(k,i,y)==1 and k>=10:
						f.write("   "+toString(k)+"  ")
					elif day(k,i,y) in d and k<10:
						f.write("  "+toString(k)+"  ")
					elif day(k,i,y) in d and k>=10:
						f.write(" "+toString(k)+"  ")
					elif day(k,i,y)==0 and k<10:
						f.write("  "+toString(k)+"\n")
					elif day(k,i,y)==0 and k>=10:
						f.write(" "+toString(k)+"\n")
				t=day(30,i,y)
				while t%7>0:
					f.write("     ")
					t+=1
			elif i==2 and check_lp(y):
				for k in range(2,30):
					if k==29 and day(29,i,y)==1:
						f.write("   "+toString(k)+"")
					elif k==29:
						f.write(" "+toString(k)+"")
					elif day(k,i,y)==1 and k<10:
						f.write("    "+toString(k)+"  ")
					elif day(k,i,y)==1 and k>=10:
						f.write("   "+toString(k)+"  ")
					elif day(k,i,y) in d and k<10:
						f.write("  "+toString(k)+"  ")
					elif day(k,i,y) in d and k>=10:
						f.write(" "+toString(k)+"  ")
					elif day(k,i,y)==0 and k<10:
						f.write("  "+toString(k)+"\n")
					elif day(k,i,y)==0 and k>=10:
						f.write(" "+toString(k)+"\n")
				t=day(29,i,y)
				while t%7>0:
					f.write("     ")
					t+=1
			elif i==2 and not check_lp(y):
				for k in range(2,29):
					if k==28 and day(28,i,y)==1:
						f.write("   "+toString(k)+"")
					elif k==28:
						f.write(" "+toString(k)+"")
					elif day(k,i,y)==1 and k<10:
						f.write("    "+toString(k)+"  ")
					elif day(k,i,y)==1 and k>=10:
						f.write("   "+toString(k)+"  ")
					elif day(k,i,y) in d and k<10:
						f.write("  "+toString(k)+"  ")
					elif day(k,i,y) in d and k>=10:
						f.write(" "+toString(k)+"  ")
					elif day(k,i,y)==0 and k<10:
						f.write("  "+toString(k)+"\n")
					elif day(k,i,y)==0 and k>=10:
						f.write(" "+toString(k)+"\n")
				t=day(28,i,y)
				while t%7>0:
					f.write("     ")
					t+=1
		elif n==0:
			f.write("  1"+"  ")
			n-=1
			if i in exd:
				for k in range(2,32):
					if k==31 and day(31,i,y)==1:
						f.write("   "+toString(k)+"")
					elif k==31:
						f.write(" "+toString(k)+"")
					elif day(k,i,y)==1 and k<10:
						f.write("    "+toString(k)+"  ")
					elif day(k,i,y)==1 and k>=10:
						f.write("   "+toString(k)+"  ")
					elif day(k,i,y) in d and k<10:
						f.write("  "+toString(k)+"  ")
					elif day(k,i,y) in d and k>=10:
						f.write(" "+toString(k)+"  ")
					elif day(k,i,y)==0 and k<10:
						f.write("  "+toString(k)+"\n")
					elif day(k,i,y)==0 and k>=10:
						f.write(" "+toString(k)+"\n")
				t=day(31,i,y)
				while t%7>0:
					f.write("     ")
					t+=1
			elif i in nd:
				for k in range(2,31):
					if k==30 and day(30,i,y)==1:
						f.write("    "+toString(k)+"")
					elif k==30:
						f.write(" "+toString(k)+"")
					elif day(k,i,y)==1 and k<10:
						f.write("    "+toString(k)+"  ")
					elif day(k,i,y)==1 and k>=10:
						f.write("   "+toString(k)+"  ")
					elif day(k,i,y) in d and k<10:
						f.write("  "+toString(k)+"  ")
					elif day(k,i,y) in d and k>=10:
						f.write(" "+toString(k)+"  ")
					elif day(k,i,y)==0 and k<10:
						f.write("  "+toString(k)+"\n")
					elif day(k,i,y)==0 and k>=10:
						f.write(" "+toString(k)+"\n")
				t=day(30,i,y)
				while t%7>0:
					f.write("     ")
					t+=1
			elif i==2 and check_lp(y):
				for k in range(2,30):
					if k==29 and day(29,i,y)==1:
						f.write("   "+toString(k)+"")
					elif k==29:
						f.write(" "+toString(k)+"")
					elif day(k,i,y)==1 and k<10:
						f.write("    "+toString(k)+"  ")
					elif day(k,i,y)==1 and k>=10:
						f.write("   "+toString(k)+"  ")
					elif day(k,i,y) in d and k<10:
						f.write("  "+toString(k)+"  ")
					elif day(k,i,y) in d and k>=10:
						f.write(" "+toString(k)+"  ")
					elif day(k,i,y)==0 and k<10:
						f.write("  "+toString(k)+"\n")
					elif day(k,i,y)==0 and k>=10:
						f.write(" "+toString(k)+"\n")
				t=day(29,i,y)
				while t%7>0:
					f.write("     ")
					t+=1
			elif i==2 and not check_lp(y):
				for k in range(2,29):
					if k==28 and day(28,i,y)==1:
						f.write("   "+toString(k)+"")
					elif k==28:
						f.write(" "+toString(k)+"")
					elif day(k,i,y)==1 and k<10:
						f.write("    "+toString(k)+"  ")
					elif day(k,i,y)==1 and k>=10:
						f.write("   "+toString(k)+"  ")
					elif day(k,i,y) in d and k<10:
						f.write("  "+toString(k)+"  ")
					elif day(k,i,y) in d and k>=10:
						f.write(" "+toString(k)+"  ")
					elif day(k,i,y)==0 and k<10:
						f.write("  "+toString(k)+"\n")
					elif day(k,i,y)==0 and k>=10:
						f.write(" "+toString(k)+"\n")
				t=day(28,i,y)
				while t%7>0:
					f.write("     ")
					t+=1
		elif n==day(1,i,y):
			f.write("\n"+"  ")
			n-=1
	f=open('Calendar.txt','r+')
	d=f.readlines()
	while len(d)<=7:
		f.write('\n                                   ')
		d+=['1']
	f=open('Calendar.txt','r')
	mon=f.readlines()
	return mon
def cal(y):
	m=["December.txt",'January.txt','February.txt','March.txt','April.txt','May.txt','June.txt','July.txt','August.txt','September.txt','October.txt','November.txt']
	for o in range(12):
		mon(o,y)
	a=mon(1,y)
	lt1=mon(4,y)
	lt2=mon(7,y)
	lt3=mon(10,y)
	lt=a
	for i in range(2,13):
		if i==2:
			b=mon(i,y)
			for k in range(8):
				if lt[k][-1]==' ':
					lt[k]=lt[k]+'\t\t'+b[k]
				else:	
					lt[k]=lt[k][:-1]+'\t\t'+b[k]
		elif i==3:
			b=mon(i,y)
			for k in range(8):
				if lt[k][-1]==' ':
					lt[k]=lt[k]+'\t\t'+b[k]+'\n'
				else:	
					lt[k]=lt[k][:-1]+'\t\t'+b[k]+'\n'
		elif i==5:
			b=mon(i,y)
			for k in range(8):
				if lt1[k][-1]==' ':
					lt1[k]=lt1[k]+'\t\t'+b[k]
				else:	
					lt1[k]=lt1[k][:-1]+'\t\t'+b[k]
		elif i==6:
			b=mon(i,y)
			for k in range(8):
				if lt1[k][-1]==' ':
					lt1[k]=lt1[k]+'\t\t'+b[k]+'\n'
				else:	
					lt1[k]=lt1[k][:-1]+'\t\t'+b[k]+'\n'
		elif i==8:
			b=mon(i,y)
			for k in range(8):
				if lt2[k][-1]==' ':
					lt2[k]=lt2[k]+'\t\t'+b[k]
				else:	
					lt2[k]=lt2[k][:-1]+'\t\t'+b[k]
		elif i==9:
			b=mon(i,y)
			for k in range(8):
				if lt2[k][-1]==' ':
					lt2[k]=lt2[k]+'\t\t'+b[k]+'\n'
				else:	
					lt2[k]=lt2[k][:-1]+'\t\t'+b[k]+'\n'
		elif i==11:
			b=mon(i,y)
			for k in range(8):
				if lt3[k][-1]==' ':
					lt3[k]=lt3[k]+'\t\t'+b[k]
				else:	
					lt3[k]=lt3[k][:-1]+'\t\t'+b[k]
		elif i==12:
			b=mon(i,y)
			for k in range(8):
				if lt3[k][-1]==' ':
					lt3[k]=lt3[k]+'\t\t'+b[k]+'\n'
				else:	
					lt3[k]=lt3[k][:-1]+'\t\t'+b[k]+'\n'
	cal=open('Calendar.txt','w+')
	cal.writelines(['            \t\t                                     -'+toString(y)+'-\n\n']+lt+lt1+lt2+lt3)
	return ''
print(cal(2021))