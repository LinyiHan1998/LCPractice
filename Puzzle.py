def funcSubstring(inputStr):
	# Write your code here
	stk = []
	res = []
	tmp = ''
	for s in inputStr:
		if stk and stk[-1] == s:
			stk.pop()
			tmp = s + tmp + s
		else:
			stk.append(s)
			res.append(tmp)
			tmp = ''
			print()
	res.sort()
	return res[0] if res else 'None'

def main():
	#input for inputStr
	inputStr = str(input())
	
	
	result = funcSubstring(inputStr)
	print(result)	

if __name__ == "__main__":
	main()