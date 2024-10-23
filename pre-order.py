class Tnode:
    def __init__(self, name, is_directory=True):
        self.name = name
        self.left = None
        self.right = None
        self.is_directory = is_directory

def pre_order(root, path=""):
    if root:
        current_path = path + "/" + root.name
        print(current_path)
        pre_order(root.left, current_path)
        pre_order(root.right, path)


root = Tnode("root")
root.left = Tnode("folder1")
root.right = Tnode("file1.txt", is_directory=False)
root.left.left = Tnode("folder2")
root.left.right = Tnode("file2.txt", is_directory=False)
root.left.left.left = Tnode("file3.txt", is_directory=False)
print("File System Paths (Pre-order):")
pre_order(root)