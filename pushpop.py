# Imported for standard input.
import sys

# Create a stack class.
class Stack:
    # Store the collection of elements.
    __elements = []

    # Initializer.
    def __init__(self):
        self.__elements = []

    # Push an element onto the stack.
    def push(self, element):
        self.__elements.append(element)

    # Pop an elements off the stack.
    def pop(self):
        num_elements = len(self.__elements)
        element = self.__elements[num_elements - 1]
        self.__elements.remove(element)

    # Determine if the stack is empty.
    def isEmpty(self):
        num_elements = len(self.__elements)
        return (num_elements == 0)

    # Retrieve the top element of the stack.
    def getTop(self):
        num_elements = len(self.__elements)
        return self.__elements[num_elements - 1]

    def toString(self):
        return str(self.__elements) + " " + "size:" + " " + str(len(self.__elements))

# Determine if the permutation is possible given the constraints of the problem.
def isPermutationPossible(stack, permutation):
    # Define a temporary stack, the station.
    t_stack = Stack()

    # Find the current element of the permutation.
    while (not(permutation.isEmpty())):
        # Get the current element.
        element = permutation.getTop()
        permutation.pop()

        # Search for the element on top of the temporary stack.
        if (not(t_stack.isEmpty()) and element <= t_stack.getTop()):
            while (not(t_stack.isEmpty())):
                top_element = t_stack.getTop()
                if (top_element == element):
                    break
                t_stack.pop()
        # Search for the element on the original stack.
        elif (not(stack.isEmpty()) and element >= stack.getTop()):
            while (not(stack.isEmpty())):
                top_element = stack.getTop()
                stack.pop()
                t_stack.push(top_element)
                if (top_element == element):
                    break

        # Determine if a solution is still possible.
        if (t_stack.isEmpty()):
            return "No"

        # Pop the found element off the top of the temporary stack.
        t_stack.pop()

    return "Yes"

# Read in the number of elements within the sub-problems.
num_elements = input()


# Continue reading input until a zero is encountered.
while (num_elements != 0):
    # Initialize the original set of numbers.
    __elements = []
    for x in range(1, num_elements+1):
        __elements.append(x)

    # Initialize the original stack of numbers.
    s_stack = Stack()
    __elements.reverse()
    for x in range(0, num_elements):
        element = __elements[x]
        s_stack.push(element)

    # Determine if computation should continue after reading in the permutation.
    __elements = sys.stdin.readline().split()
    if (int(__elements[0]) == 0):
        num_elements = input()
        continue

    # Store the permutation numbers into another stack.
    p_stack = Stack()
    __elements.reverse()
    for x in range(0, num_elements):
        element = int(__elements[x])
        p_stack.push(element)

    # Determine if the permutation is possible.
    result = isPermutationPossible(s_stack, p_stack)
    print(result)

    # Clean up.
    del s_stack
    del p_stack