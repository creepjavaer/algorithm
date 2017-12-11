#searchchange.py
# preordder the node 
def seach(tree,k1,k2,l):
	if tree:
		if k1<tree.data<k2:
			l.append(tree.data)

		search(tree.left)
		serch(search.right)



