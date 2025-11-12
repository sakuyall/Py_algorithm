"""11/9/25
模拟文件系统
"""
class Node:
    def __init__(self, name, type = "dir"):
        self.name = name
        self.type = type   # "dir" or "file"
        self.children = []
        self.parent = None
    
    def __repr__(self):
        return  self.name

class FileSystemTree:
    def __init__(self):
        self.root = Node("/")    # 传入/的node对象
        self.now = self.root

    def mkdir(self, name):       # 这几个都是模拟的Linux
        # 传入name应以/结尾
        if name[-1] != "/":      # 若结尾不为/就添加一个
            name += "/"
        node = Node(name)        # 把传入的name设为实例化对象node的name,type仍默认为dir
        self.now.children.append(node)   # 正着连
        node.parent = self.now           # 反者连

    def ls(self, name):
        return self.now.children

    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        for child in self.now.children:
            if child.name == name:
                self.now = child
        raise ValueError("invalid dir")

n = Node("hello")
n2 = Node("world")
n.children.append(n2)
n2.parent = n      # 在向下查找的树中无需定义向上关系

tree = FileSystemTree()
tree.mkdir("var/")
print(tree.root.children)

# 知识盲区 推迟