def GST(s1,s2):
	marked1=[0]*20000;marked2=[0]*20000
	MML=3
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
				if(k==maxmatch):matches.append([i,j,k])
				if(k>maxmatch):
					maxmatch=k
					matches=[[i,j,k]]
		for match in matches:
			i1,j1,k1=match[0],match[1],match[2]
			marked1[i1:i1+k1]=[1]*k1;marked2[j1:j1+k1]=[1]*k1
			samelength+=maxmatch
		if(mmax==0):mmax=maxmatch
		if(maxmatch==MML):suc=0
	return [samelength,mmax]
		
				
