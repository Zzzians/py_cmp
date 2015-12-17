import sys,math

global st,sta
st=[]
sta=[]

DIC=['tri','square','penta','hexa']
DICC=['filledtri','filledsquare','filledpenta','filledhexa']
dic={'tri':3,'filledtri':3,'square':4,'filledsquare':4,'penta':5,'filledpenta':5,'hexa':6,'filledhexa':6}
TF=['translate','rotate','scale']
tf={'translate':3,'rotate':2,'scale':2}

def deal():	
	global st	
	#s=open('draw2.test')
	st=sys.stdin.read()
	st=st.replace('('," ")
	st=st.replace(')'," ")
	st=st.split()
	print("%!PS-Adobe-3.1")
	return

def scale(s,a,n):
	for i in range(n):
		s[i][0]*=a
		s[i][1]*=a
	return s

def rotate(s,a,n):
	for i in range(n):
		s[i][0],s[i][1]=s[i][0]*math.cos(math.radians(a))-s[i][1]*math.sin(math.radians(a)),s[i][0]*math.sin(math.radians(a))+s[i][1]*math.cos(math.radians(a))
	return s

def translate(s,a,b,n):
	for i in range(n):
		s[i][0]+=a
		s[i][1]+=b
	return s

def ini(ng,n,a,b,r):
	ng.append([a+r,b])	
	for i in range(1,n):
		ng.append([r*math.cos(math.radians(360*i/n))+a,r*math.sin(math.radians(360*i/n))+b])
	return ng
	
def makeng(s,n,flag):
	global sta
	for i in range(len(sta)):
		if sta[i]=='scale':
			s=scale(s,float(sta[i-1]),n)
		elif sta[i]=='rotate':
			s=rotate(s,float(sta[i-1]),n)
		elif sta[i]=='translate':
			s=translate(s,float(sta[i-1]),float(sta[i-2]),n)
	print(s[0][0],s[0][1],'moveto')
	for i in range(1,n):
		print(s[i][0],s[i][1],'lineto')
	print(s[0][0],s[0][1],'lineto')
	if flag:
		print('stroke')
	else:
		print('fill')
	sta=[]

def makeln(s,n):
	global sta
	for i in range(len(sta)):
		if sta[i]=='scale':
			s=scale(s,float(sta[i-1]),n)
		elif sta[i]=='rotate':
			s=rotate(s,float(sta[i-1]),n)
		elif sta[i]=='translate':
			s=translate(s,float(sta[i-1]),float(sta[i-2]),n)
	print(s[0][0],s[0][1],'moveto')
	print(s[1][0],s[1][1],'lineto')
	print('stroke')
	sta=[]
	




deal()
i=0
while i<len(st):
	if st[i] in TF:
		for j in range(tf[st[i]]):
			sta.insert(0,st[i+j])
		i+=tf[st[i]]-1
	elif st[i]=='color':
		print(st[i+1],st[i+2],st[i+3],'setrgbcolor')
		i+=3
	elif st[i]=='linewidth':
		i+=1
		print(st[i],'setlinewidth')
	elif st[i] in DIC:
		flag=True		
		coor=[]
		ini(coor,dic[st[i]],float(st[i+1]),float(st[i+2]),float(st[i+3]))
		makeng(coor,dic[st[i]],flag)		
		i+=3
	elif st[i] in DICC:
		flag=False
		coor=[]
		ini(coor,dic[st[i]],float(st[i+1]),float(st[i+2]),float(st[i+3]))
		makeng(coor,dic[st[i]],flag)
		i+=3
	elif st[i]=='ngon':
		flag=True
		coor=[]
		ini(coor,int(st[i+4]),float(st[i+1]),float(st[i+2]),float(st[i+3]))
		makeng(coor,int(st[i+4]),flag)
		i+=4
	elif st[i]=='filledngon':
		flag=False
		coor=[]
		ini(coor,int(st[i+4]),float(st[i+1]),float(st[i+2]),float(st[i+3]))
		makeng(coor,int(st[i+4]),flag)
		i+=4
	elif st[i]=='line':
		flag=True
		coor=[]
		coor.append([float(st[i+1]),float(st[i+2])])
		coor.append([float(st[i+3]),float(st[i+4])])
		makeln(coor,2)
		i+=4
	elif st[i]=='rect':
		flag=True
		coor=[]
		a,b,w,h=float(st[i+1]),float(st[i+2]),float(st[i+3]),float(st[i+4])
		coor.append([a,b])
		coor.append([a+w,b])
		coor.append([a+w,b+h])
		coor.append([a,b+h])
		makeng(coor,4,flag)
		i+=4
	elif st[i]=='filledrect':
		flag=False
		coor=[]
		a,b,w,h=float(st[i+1]),float(st[i+2]),float(st[i+3]),float(st[i+4])
		coor.append([a,b])
		coor.append([a+w,b])
		coor.append([a+w,b+h])
		coor.append([a,b+h])
		makeng(coor,4,flag)
		i+=4
	i+=1
print("showpage")                                                                                                                                                  
                                                                               
