#minstack.py

class stack():
	def __init__(self,stacka,stackb):
		self.stacka=stacka
		self.stackb=stackb

	def pop(self):
		self.stacka.pop()
		self.stackb.pop()

	def push(self,s):
		self.stacka.append(s)

		if not self.stackb:
			stackb.append(s)

		elif s < stackb[-1]:
			self.stackb.append(s)
		else:
			self.stackb.append(stackb[-1])

	def min(self):
		return self.stackb[-1]
stacka=[]
stackb=[]
st=stack(stacka, stackb)

st.push(1)
st.push(2)
st.push(3)
st.push(-4)
st.push(4)
st.push(-1)
st.pop()
st.pop()
st.pop()


print(st.min())
print(st.min())
print(st.stackb)

