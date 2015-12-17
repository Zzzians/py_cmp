import sys
import math

trans=['translate','rotate','scale']
trandic={'translate':3,'rotate':2,'scale':2}
dw=['color','linewidth']
do=['line','rect','filledrect','tri','filledtri','square','filledsquare','penta','filledpenta','hexa','filledhexa','ngon','filledngon']
triagon=['tri','filledtri','square','filledsquare','penta','filledpenta','hexa','filledhexa']
tridic={'tri':[3,0],'filledtri':[3,1],'square':[4,0],'filledsquare':[4,1],'penta':[5,0],'filledpenta':[5,1],'hexa':[6,0],'filledhexa':[6,1]}

def draw(isf):
	if(isf):print("fill")
	else:print("stroke")
def sca(x,t):
	for pos in x:
		pos[0],pos[1]=pos[0]*t,pos[1]*t


def tran(x,xp,yp):
	for pos in x:
		pos[0],pos[1]=pos[0]+xp,pos[1]+yp

def rot(x,angle,x0=0,y0=0):
	for pos in x:
		pos[0],pos[1]=pos[0]-x0,pos[1]-y0
		pos[0],pos[1]=pos[0]*math.cos(math.radians(angle))-pos[1]*math.sin(math.radians(angle)),pos[0]*math.sin(math.radians(angle))+pos[1]*math.cos(math.radians(angle))
		pos[0],pos[1]=pos[0]+x0,pos[1]+y0

def doit(x):
	global ostack
	while(len(ostack)):
		tmp=ostack.pop()
		if(tmp[0]=='rotate'):
			rot(x,float(tmp[1]))
		elif(tmp[0]=='translate'):
			tran(x,float(tmp[1]),float(tmp[2]))
		elif(tmp[0]=='scale'):
			sca(x,float(tmp[1]))

def rect(x1,y1,w,h,f):
	global ostack
	x=[[x1+w,y1],[x1+w,y1+h],[x1,y1+h],[x1,y1]]
	doit(x)
	print(x[3][0],x[3][1],"moveto")
	print(x[0][0],x[0][1],"lineto")
	print(x[1][0],x[1][1],"lineto")
	print(x[2][0],x[2][1],"lineto")
	print(x[3][0],x[3][1],"lineto")
	draw(f)
def line(x1,y1,x2,y2):
	global ostack
	x=[[x1,y1],[x2,y2]];
	doit(x)
	print(x[0][0],x[0][1],"moveto")
	print(x[1][0],x[1][1],"lineto")
	draw(0)

def ngon(x0,y0,r,n,f):
	global ostack
	x=[[x0+r,y0]]
	a=[[x0+r,y0]]
	for i in range(1,n):
		rot(a,360/n,x0,y0)
		x.append([a[0][0],a[0][1]])
	doit(x)
	print(x[0][0],x[0][1],"moveto")
	for i in range(n-1):
		print(x[i+1][0],x[i+1][1],"lineto")
	print(x[0][0],x[0][1],"lineto")
	draw(f)
	
		
s=sys.stdin.read()
global ostack
ostack=[]
s=s.replace('('," ");s=s.replace(')'," ")
inp=s.split()
print("%!PS-Adobe-3.1")
for i in range(len(inp)):
	if(inp[i] in trans):
		tmp=inp[i:i+trandic[inp[i]]]
		ostack.append(tmp)
	elif(inp[i] in dw):
		if(inp[i]=='color'):
			print(inp[i+1],inp[i+2],inp[i+3],'setrgbcolor')
		elif(inp[i]=='linewidth'):
			print(inp[i+1],'setlinewidth')
	elif(inp[i] in do):
		if(inp[i]=='rect'):
			rect(float(inp[i+1]),float(inp[i+2]),float(inp[i+3]),float(inp[i+4]),0)
		elif(inp[i]=='filledrect'):
			rect(float(inp[i+1]),float(inp[i+2]),float(inp[i+3]),float(inp[i+4]),1)
		elif(inp[i]=='line'):
			line(float(inp[i+1]),float(inp[i+2]),float(inp[i+3]),float(inp[i+4]))
		elif(inp[i]=='ngon'):
			ngon(float(inp[i+1]),float(inp[i+2]),float(inp[i+3]),int(inp[i+4]),0)
		elif(inp[i]=='filledngon'):
			ngon(float(inp[i+1]),float(inp[i+2]),float(inp[i+3]),int(inp[i+4]),1)
		elif(inp[i] in triagon):
			ngon(float(inp[i+1]),float(inp[i+2]),float(inp[i+3]),tridic[inp[i]][0],tridic[inp[i]][1])
print("showpage")
		
			
			
		
			
			
