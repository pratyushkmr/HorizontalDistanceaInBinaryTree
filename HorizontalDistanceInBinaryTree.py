import sys, io

# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to  print level order traversal of tree
class Operation():
    def printLevelOrder(self, root):
        ht = self.height(root)
        self.fill_missing_nodes(root, 1, ht)
        for i in range(1, ht + 1):
            self.print_given_level(root, i)
            print(" ")

    # Filling missing nodes
    def fill_missing_nodes(self, root, level, ht):

        if level == ht:
            return
        elif level < ht:
            if (root.left == None and level < ht):
                root.left = Node("X")
            if (root.right == None and level < ht):
                root.right = Node("X")
            self.fill_missing_nodes(root.left, level + 1, ht)
            self.fill_missing_nodes(root.right, level + 1, ht)

    # Print nodes at a given level
    def print_given_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end=" ")
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    """ Compute the height of a tree--the number of nodes 
        along the longest path from the root node down to 
        the farthest leaf node 
    """

    def height(self, node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            #Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    # Assign print to a variable
    def storing_print(self, root):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        self.printLevelOrder(root)

        output = new_stdout.getvalue()
        sys.stdout = old_stdout
        return [x.split() for x in output.replace("\n", "").split("  ")]

    # Calculating distance between two nodes
    def calculate_dist(self, node1, node2):
        check = False
        for li in output2:
            if node1 in li:
                node1_index = li.index(node1)
                li[node1_index] = "empty"
                if node2 in li:
                    distance = abs(node1_index - li.index(node2)) - 1
                    if distance >= 0:
                        return True, distance
                    else:
                        pass
                        
        return check, None

    # Print ditance or error
    def print_result(self, check, distance, node1, node2):
        print("Value either not in a tree or not in a same level"
              ) if not check else print(
                  f"Horizontal distance between {node1} and {node2}: " +
                  str(distance))


# Driver program to test above function
if __name__ == "__main__":
    root = Node(5)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.left.left = Node(9)
    root.right.right = Node(1)
    root.right.right.left = Node(4)
    root.right.right.right = Node(6)

    operation_object = Operation()

    output2 = operation_object.storing_print(root)

    node1, node2 = (input("Enter 2 nodes value in the format '7 1'\n").split())
    check, distance = operation_object.calculate_dist(node1, node2)

    operation_object.print_result(check, distance, node1, node2)
