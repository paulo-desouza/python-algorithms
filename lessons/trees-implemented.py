# TREES IMPLEMENTATION : 
# Representation of a tree using functions and lists.

# define the tree root
def binary_tree(r):
    return[r, [], []]


def insert_left(root, new_branch):
   
    t = root.pop(1)

    if len(t) > 1:
        # if there is a leaf inside this branch, we store it in 't' and push it to the bottom-most of the tree.
        root.insert(1, [new_branch, t, []])
    else:
        # if it is empty, we insert a new branch with two empty children. 
        root.insert(1, [new_branch, [], []])

    return root

def insert_right(root, new_branch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root

def get_root_value(root):
    return root[0]

def set_root_value(root, new_value):
    root[0] = new_value

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


r = binary_tree('/')
insert_left(r, 'Downloads')
insert_left(r, 'home')
insert_right(r, 'etc')

print(r)

