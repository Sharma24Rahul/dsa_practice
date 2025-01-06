"""
This function has O(n) time complexity.
In a graph, the relationship between input size (x-axis) and the number of operations (y-axis) is proportional, forming a straight line.

- X-axis: Input size (n)
- Y-axis: Number of operations
Since the number of operations grows linearly with the input size, the graph will always be a straight line.

"""
def print_item(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
"""
adding another for loop , it looks it will be O(2n) but it is same as O(n) so we can remove the contstant 
vbecasue it represent samr growth rate
"""


if __name__ == '__main__':
    print_item(10)