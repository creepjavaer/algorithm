#enunzip.py

def enhancezip(str):
	stack=[]

	result=""
	number=""
	end=-1
	p=""
	temp=""
	for ch in str:
		if ch !="]":
			stack.append(ch)
			print(stack)
		elif ch=="]":
			p=stack.pop()
			if stack:
				while p!="[":
					temp+=p
					print("hahh")
					p=stack.pop()
			print(p)
			result=temp
			p=""
			temp=""
			print(stack)
			temp=stack.pop()
			print(temp)
			if stack:
				while temp.isdigit():
					number+=temp
					if stack:
						temp=stack.pop()
			if not number:
				number=temp
			else:

				stack.append(temp)

			print(temp)
			print(stack)
			temp=""
			print(number)
			print("$$")
			print(number)
			new=number[::-1]
			print(new)
			number=""

			count=int(new)
			result=result[::-1]*count
			stack.append(result)
			result=""
		#else:
			#stack.append(ch)
	for strs in stack:
		result+=strs
	return result
	

print(enhancezip("1[a]2[b3[c]]"))










