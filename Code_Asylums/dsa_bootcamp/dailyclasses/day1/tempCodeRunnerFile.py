if self.left==None and self.value>val:
            self.left=tree(val)
        elif self.value>val:
            self.left.insert(val)
        elif self.right==None and self.value<=val:
            self.right=tree(val)
        else:
            self.right.insert(val)