# CSE 101 - IP HW2
# K-Map Minimization 
# Name: HARSH KUMAR
# Roll Number: 2018285
# Section: B
# Group: 6
# Date: 17/10/2018

def minFunc(n, f):
	ef = f[1:(f.find(')',1))] #normal minterms
	ed = f[(f.find('d')+2):-1]#don't care minterms
	fn = ef.split(',')#normal  minterms in list
	dn = ed.split(',')#don't care minterms in list
	if (dn==['']):
		cn = fn
	else:
		cn = fn + dn #taking the normal minterms and the don't care minterms in one list
	deno = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','10':'1010','11':'1011','12':'1100','13':'1101','14':'1110','15':'1111'}
	cn.sort()
	if (cn==['']):
		return ('0')
	g0={}
	g1={}
	g2={}
	g3={}
	g4={}
	g00={}
	g11={}
	g22={}
	g33={}
	g000={}
	g111={}
	g222={}
	g0000={}
	g1111={}
	g00000={}
	pifv={}
	mpd={}
	pi={}
	dn.sort()
	valn = {1:'W',2:'X',3:'Y',4:'Z'}
	valc = {1:'w',2:'x',3:'y',4:'z'}
	def nonrepv2(s):#function for removing repeating essential prime implicants
		s = s.split('+')
		s = list(set(s))
		dans = ''
		for x in s:
			dans+=x+'+'
		return dans
	def existcheck(e1,e2):#function to check if the normal minterms are part of the following essential minterms
		c=0
		el = e2.split('-')
		for o in (el):
			if (o==e1):
				c+=1
		if (c==1):
			return True
		else:
			return False
	def nonrep(d):#function to remove repeating prime implicants
		l = len(d)
		li = list(d.keys())
		for x in range(0,l-1):
			flag = True
			for y in range(x+1,l):
				l1 = list(map(int,li[x].split('-')))
				l2 = list(map(int,li[y].split('-')))
				l1.sort()
				l2.sort()
				if (l1==l2 and flag):
					flag = False
					del d[li[y]]
		return (d)
	def pic(c1,c2,c3):#function for checking if the following function is a prime implicanr
		c = 0
		for r in c1:
			for s in c2:
				if (r==s):
					c+=1
		if (c==c3):
			return True
		else:
			return False
	def bitchecker(b1,b2):#to check each bits of the decimal minterms, to check the matching groups
		c = 0
		bn = ''
		for p in range (0,4):
			if (b1[p]!=b2[p]):
				c+=1
				bn+='_'
			else:
				bn+=b1[p]
		if (c==1):
			return [True,bn]
		else:
			return [False,bn]
	def assign(a1,a2):#function to assign the letters (w,z,y,z or complements of them) to the functions
		if (a2=='1'):
			return(valn[a1])
		elif (a2=='0'):
			return(valc[a1])
		else:
			return ('')
	def kmap(cn):#the main body of the program
		for x in cn:#for categorizing the mintermns in the groups according to the number of 1s
			if (x=='0'):
				g0[x] = deno[x]
			if (x=='1' or x=='2' or x=='4' or x=='8'):
				g1[x] = deno[x]
			if (x=='3' or x=='5' or x=='6' or x=='9' or x=='10' or x=='12'):
				g2[x] = deno[x]
			if (x=='7' or x=='11' or x=='13' or x=='14'):
				g3[x] = deno[x]
			if(x=='15'):
				g4[x] = deno[x]
		#for checking the first matching groups
		for x in g0:
			for y in g1:
				bc = bitchecker(deno[x],deno[y])
				if (bc[0]):
					g00[x+'-'+y] = bc[1]
		for x in g1:
			for y in g2:
				bc = bitchecker(deno[x],deno[y])
				if (bc[0]):
					g11[x+'-'+y] = bc[1]
		for x in g2:
			for y in g3:
				bc = bitchecker(deno[x],deno[y])
				if (bc[0]):
					g22[x+'-'+y] = bc[1]
		for x in g3:
			for y in g4:
				bc = bitchecker(deno[x],deno[y])
				if (bc[0]):
					g33[x+'-'+y] = bc[1]
		#for checking the second matching groups
		for x in g00:
			for y in g11:
				bc = bitchecker(g00[x],g11[y])
				if (bc[0]):
					g000[x+'-'+y] = bc[1]
		for x in g11:
			for y in g22:
				bc = bitchecker(g11[x],g22[y])
				if (bc[0]):
					g111[x+'-'+y] = bc[1]
		for x in g22:
			for y in g33:
				bc = bitchecker(g22[x],g33[y])
				if (bc[0]):
					g222[x+'-'+y] = bc[1]
		#for checking the third matching groups
		for x in g000:
			for y in g111:
				bc = bitchecker(g000[x],g111[y])
				if (bc[0]):
					g0000[x+'-'+y] = bc[1]
		for x in g111:
			for y in g222:
				bc = bitchecker(g111[x],g222[y])
				if (bc[0]):
					g1111[x+'-'+y] = bc[1]
		if (len(g0000)!=0 or len(g1111)!=0):
			for x in g000:
				c=0
				for y in g0000:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,4)):
						c+=1
				if(c==0):
					pi[x]=g000[x]
			for x in g111:
				c=0
				for y in g0000:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,4)):
						c+=1
				for z in g1111:
					vx = x.split('-')
					vz = z.split('-')
					if(pic(vz,vx,4)):
						c+=1
				if (c==0):
					pi[x]=g111[x]
			for x in g222:
				c=0
				for y in g1111:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,4)):
						c+=1
				if(c==0):
					pi[x]=g222[x]
			for x in g0000:
				pi[x] = g0000[x]
			for x in g1111:
				pi[x] = g1111[x]
			nrpi = nonrep(pi)
		elif (len(g000)!=0 or len(g111)!=0 or len(g222)!=0):
			for x in g00:
				c=0
				for y in g000:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,2)):
						c+=1
				if (c==0):
					pi[x] = g00[x]
			for x in g11:
				c=0
				for y in g000:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,2)):
						c+=1
				for z in g111:
					vx = x.split('-')
					vz = z.split('-')
					if(pic(vz,vx,2)):
						c+=1
				if(c==0):
					pi[x] = g11[x]
			for x in g22:
				c=0
				for y in g111:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,2)):
						c+=1
				for z in g222:
					vx = x.split('-')
					vz = z.split('-')
					if(pic(vz,vx,2)):
						c+=1
				if(c==0):
					pi[x] = g22[x]
			for x in g33:
				c=0
				for y in g222:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,2)):
						c+=1
				if (c==0):
					pi[x] = g33[x]
			for x in g000:
				pi[x] = g000[x]
			for x in g111:
				pi[x] = g111[x]
			for x in g222:
				pi[x] = g222[x]
			nrpi = nonrep(pi)
		elif (len(g00)!=0 or len(g11)!=0 or len(g22)!=0 or len(g33)!=0):
			for x in g0:
				c=0
				for y in g00:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,1)):
						c+=1
				if (c==0):
					pi[x]=g0[x]
			for x in g1:
				c=0
				for y in g00:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,1)):
						c+=1
				for z in g11:
					vx = x.split('-')
					vz = z.split('-')
					if(pic(vz,vx,1)):
						c+=1
				if(c==0):
					pi[x]=g1[x]
			for x in g2:
				c=0
				for y in g11:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,1)):
						c+=1
				for z in g22:
					vx = x.split('-')
					vz = z.split('-')
					if(pic(vz,vx,1)):
						c+=1
				if(c==0):
					pi[x]=g1[x]
			for x in g3:
				c=0
				for y in g22:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,1)):
						c+=1
				for z in g33:
					vx = x.split('-')
					vz = z.split('-')
					if(pic(vz,vx,1)):
						c+=1
				if(c==0):
					pi[x]=g1[x]
			for x in g4:
				c=0
				for y in g33:
					vx = x.split('-')
					vy = y.split('-')
					if(pic(vy,vx,1)):
						c+=1
				if(c==0):
					pi[x]=g4[x]
			for x in g00:
				pi[x] = g00[x]
			for x in g11:
				pi[x] = g11[x]
			for x in g22:
				pi[x] = g22[x]
			for x in g33:
				pi[x] = g33[x]
			nrpi = nonrep(pi)
		else:
			for x in g0:
				pi[x] = g0[x]
			for x in g1:
				pi[x] = g1[x]
			for x in g2:
				pi[x] = g2[x]
			for x in g3:
				pi[x] = g3[x]
			for x in g4:
				pi[x] = g4[x]
			nrpi = nonrep(pi)
		piv=''
		for x in nrpi:
			c=0
			piv=''
			vipi = nrpi[x]
			for y in vipi:
				c+=1
				piv+=assign(c,y)
			pifv[piv] = x
		for x in pifv:
			mpl=''
			for y in fn:
				if (existcheck(y,pifv[x])):
					mpl+='X'
				else:
					mpl+='_'
			mpd[x]=mpl
		ans=''
		for x in range(0,len(fn)):
			c=0
			for y in mpd:
				if ((mpd[y])[x]=='X'):
					c+=1
					mvp=y
			if (c==1):
				ans+=mvp+'+'
		ans = ans[:-1]
		ans = (nonrepv2(ans))[:-1]
		ans = ans.split('+')
		fans=''
		if (n==4):
			if (len(cn)==16):
				return('1')
			else:
				for x in ans:
					fans+=x+'+'
		if (n==3):
			if (len(cn)==8):
				return('1')
			else:
				for x in ans:
					c=0
					for y in x:
						if(c>0):
							if (y=='W' or y=='X' or y=='Y' or y=='Z'):
								fans+=valn[(ord(y)-86)-1]
							else:
								fans+=valc[(ord(y)-118)-1]
						c+=1
					fans+='+'
		if (n==2):
			if (len(cn)==4):
				return ('1')
			else:
				for x in ans:
					c=0
					for y in x:
						if(c>1):
							if (y=='W' or y=='X' or y=='Y' or y=='Z'):
								fans+=valn[(ord(y)-86)-2]
							else:
								fans+=valc[(ord(y)-118)-2]
						c+=1
					fans+='+'
		if(n==1):
			if (len(cn)==2):
				return ('1')
			else:
				for x in ans:
					c=0
					for y in x:
						if(c>2):
							if (y=='W' or y=='X' or y=='Y' or y=='Z'):
								fans+=valn[(ord(y)-86)-3]
							else:
								fans+=valc[(ord(y)-118)-3]
						c+=1
					fans+='+'
		ofa=''
		fans=fans[:-1]
		fansl=fans.split('+')
		fansl = sorted(fansl, key=lambda s: s.casefold())
		for x in fansl:
			lans=''
			for y in x:
				if y in valn.values():
					lans+=chr(ord(y)+32)
				else:
					lans+=y+'\''
			ofa+=lans+'+'
		return (ofa[:-1])
	return kmap(cn)