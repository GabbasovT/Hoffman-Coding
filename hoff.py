from collections import Counter
import heapq
from typing import Dict, List, Tuple

file_path = 'test.bmp'
with open(file_path, 'rb') as file:
    data = file.read()

byte_frequencies = Counter(data)

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
        
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(byte_frequencies: Dict[int, int]) -> Node:
    heap = [Node(freq, byte) for byte, freq in byte_frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, merged)
    return heap[0]

def generate_huffman_codes(node: Node, code: str = "") -> Dict[int, str]:
    if node.symbol is not None:
        return {node.symbol: code}
    codes = {}
    if node.left:
        codes.update(generate_huffman_codes(node.left, code + "0"))
    if node.right:
        codes.update(generate_huffman_codes(node.right, code + "1"))
    return codes

huffman_tree = build_huffman_tree(byte_frequencies)
huffman_codes = generate_huffman_codes(huffman_tree)

byte_frequencies_list = list(byte_frequencies.items())
huffman_codes_list = list(huffman_codes.items())

print(byte_frequencies_list[:10], huffman_codes_list[:10], sep='\n')
