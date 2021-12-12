class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob
        # symbol
        self.symbol = symbol
        # left node
        self.left = left
        # right node
        self.right = right
        # tree direction (0/1)
        self.code = ''


def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) is None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


# A helper function to print the codes of symbols by traveling Huffman Tree
codes = dict()


def Calculate_Codes(self, val=''):
    # huffman code for current node
    newVal = val + str(self.code)
    if self.left:
        Calculate_Codes(self.left, newVal)
    if self.right:
        Calculate_Codes(self.right, newVal)
    if not self.left and not self.right:
        codes[self.symbol] = newVal
    return codes


# A helper function to obtain the encoded output
def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])
    string = ''.join([str(item) for item in encoding_output])
    return string


def Output_Decoded(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol is None and huffman_tree.right.symbol is None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    string = ''.join([str(item) for item in decoded_output])
    return string


def Huffman_Encoding(data):
    symbol_with_probs = Calculate_Probability(data)
    symbols = symbol_with_probs.keys()
    symbol_with_probs.values()

    nodes = []

    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)

        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1

        # combine the 2 smallest nodes to create new node
        newNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = Calculate_Codes(nodes[0])
    encoded_output = Output_Encoded(data, huffman_encoding)
    return encoded_output, nodes
