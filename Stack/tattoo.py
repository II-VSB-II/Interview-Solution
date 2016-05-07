You='010100110110000101101011011100110110100001101001'
Me=''.join(chr(int(You[i:i+8], 2)) for i in range(0, len(You), 8))
print(Me)
