# from RLE import runLengthEncoding
from LZMA import compressor
# import numpy as np
import time

start = time.perf_counter()
# input = np.array(list("aaaaabbbadsackkkadnddadiqnnqllldsds"))
# print(runLengthEncoding(input))
print(compressor(b"aaaaabbbadsackkkadnddadiqnnqllldsds"))
print(time.perf_counter() - start)
