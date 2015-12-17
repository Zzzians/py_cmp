com0=["STORE_NAME",'LOAD_NAME','MAKE_FUNCTION','CALL_FUNCTION',"STORE_FAST","LOAD_FAST","BUILD_LIST","SETUP_LOOP","FOR_ITER"]
com2=["IMPORT_NAME","LOAD_GLOBAL","LOAD_ATTR","STORE_GLOBAL"]
def read(hFile):
	s=[]
	for raws in hFile.readlines():
		raws=raws.split()
		for i in range(len(raws)):
			if(raws[i][0] >= 'A' and raws[i][0] <='Z'):
				tmp=raws[i]
				if(raws[i]=="LOAD_CONST"):
					j=i+2;
					while(j<len(raws)):
						tmp+=raws[j]
						j=j+1
				elif ('JUMP' in raws[i] or raws[i] in com0):ssss=1
				elif(raws[i] in com2):tmp+=raws[i+2]
				elif(i+1<len(raws)):tmp+=raws[i+1]
				s.append(tmp)
				continue
	return s
def GST(s1,s2,MML):
	marked1=[0]*20000;marked2=[0]*20000
	samelength=0;mmax=0
	suc=1
	l1=len(s1);l2=len(s2)
	while(suc==1):
		maxmatch=MML
		matches=[]
		for i in range(l1):
			if(marked1[i]):continue
			for j in range(l2):
				if(marked2[j]):continue
				k=0
				while(i+k<l1 and j+k<l2 and s1[i+k]==s2[j+k]):k=k+1
				if(k==maxmatch):
					if(len(matches)==0 or (i>matches[-1][0]+matches[-1][2] and j>matches[-1][1]+matches[-1][2])):matches.append([i,j,k])
				if(k>maxmatch):
					maxmatch=k
					matches=[[i,j,k]]
		for match in matches:
			i1,j1,k1=match[0],match[1],match[2]
			marked1[i1:i1+k1]=[1]*k1;marked2[j1:j1+k1]=[1]*k1
			samelength+=maxmatch
		if(mmax==0 and len(matches)):mmax=maxmatch
		if(maxmatch==MML):suc=0
	return [samelength,mmax,min(l1,l2)]
def main():
	h1=open('./test/test1.in', 'r');h2=open('./test/test2.in','r')
	s1=read(h1);s2=read(h2)
	result=GST(s1,s2,3)
	print("the similarity is",result[0]/result[2],"and the percent that are copied is",result[1]/result[2],"by using gst3")
	result=GST(s1,s2,4)
	print("the similarity is",result[0]/result[2],"and the percent that are copied is",result[1]/result[2],"by using gst4")
main()
