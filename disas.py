import dis
import types
import sys
def disas(inpath,outpath):
	r=open(inpath, 'r')
	sys.stdout=open(outpath,'w')
	content=r.read()
	code=compile(content,'','exec')
	dis.dis(code)
	for item in code.co_consts:
		if isinstance(item, types.CodeType):
			co=item
			dis.dis(co)
disas(sys.argv[1],'./test/test1.in')
disas(sys.argv[2],'./test/test2.in')
