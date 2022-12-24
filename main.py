import heapq
from heapq import heappop, heappush

def isLeaf(root):
    return root.left is None and root.right is None


class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def encode(root, s, huffman_code):
    if root is None:
        return

    if isLeaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'

    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '1', huffman_code)


def decode(root, index, s):
    if root is None:
        return index

    if isLeaf(root):
        print(root.ch, end='')
        return index

    index = index + 1
    root = root.left if s[index] == '0' else root.right
    return decode(root, index, s)


def buildHuffmanTree(text):
    if len(text) == 0:
        return

    freq = {i: text.count(i) for i in set(text)}

    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)

    while len(pq) != 1:

        left = heappop(pq)
        right = heappop(pq)


        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))

    root = pq[0]

    huffmanCode = {}
    encode(root, '', huffmanCode)

    print('Коды Хаффмана:', huffmanCode)
    print('Исходная строка:', text, '', len(text) * 8, 'бит')

    s = ''
    for c in text:
        s += huffmanCode.get(c)

    print('Закодированная строка:', s,':', s.count('1'), 'бит')
    print('Декодированная строка:', end=' ')

    if isLeaf(root):
        while root.freq > 0:
            print(root.ch, end='')
            root.freq = root.freq - 1
    else:
        index = -1
        while index < len(s) - 1:
            index = decode(root, index, s)


if __name__ == '__main__':
    text = 'ну вот короче вроде получилось.'
    buildHuffmanTree(text)

