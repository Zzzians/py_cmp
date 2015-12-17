dp=[None]*2
for i in range(2):
	dp[i]=[0]*1000000
h1=open('./test/test1.py', 'r');h2=open('./test/test2.py','r')
s1=h1.read();s2=h2.read()
s1=s1.replace(" ","");s1=list(s1.replace("\n",""))
s2=s2.replace(" ","");s2=list(s2.replace("\n",""))
s1.insert(0,'a');s2.insert(0,'b')
l1=len(s1);l2=len(s2)
for i in range(1,l1):
	for j in range(1,l2):
		if(s1[i]==s2[j]):add=1
		else:add=0
		dp[i%2][j]=max(dp[(i-1)%2][j-1]+add,dp[i%2][j-1],dp[(i-1)%2][j])
print('the similarity is',dp[(l1-1)%2][l2-1]/min(l1-1,l2-1),'by using lcs')
