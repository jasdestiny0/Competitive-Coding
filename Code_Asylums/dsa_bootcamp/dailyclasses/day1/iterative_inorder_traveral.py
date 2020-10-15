def iterative_inorder(self, node):
    stack=[]
    while True:
        if node!=None:
            stack.append(node)
            node=node.left
        elif stack:
            node=stack.pop()
            print(node.value)
            node=node.right
        else:
            break
