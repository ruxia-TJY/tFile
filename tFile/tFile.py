import os

def removeFileByExtFromDir(dir:str,ext:list):
	'''
	删除文件夹下所有指定扩展名的文件
	:param dir: 要删除的文件夹
	:param ext:	要删除文件的扩展名
	:return: bool
	'''
	if not os.path.exists(dir):
		raise Exception(f"路径 {dir} 不存在")
	try:
		for fp,dn,fns in os.walk(dir):
			for fn in fns:
				if os.path.splitext(os.path.join(fp,fn))[1] in ext:
					os.remove(os.path.join(fp,fn))
	except Exception as e:
		print(e)
		return False
	else:
		return True

