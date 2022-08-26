import base64
import Crypto.Util.number as cp 
import pwnlib
#ex1
# a = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
# flag = ''
# for i in a:
#     flag += chr(i)
# print(flag)

#ex2
# a = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
# a = bytes.fromhex(a)
# print(a)

#ex3
# a = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
# a = bytes.fromhex(a)
# print(a)
# a = base64.b64encode(a)
# print(a)

#ex4
# a = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# a = cp.long_to_bytes(a)
# print(a)

#ex5
# a = "label"
# b = ""
# for i in a:
#     b += chr(ord(i) ^ 13)
# print(b)

#ex6
# one = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
# onextwo = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
# twoxthree = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
# flagxall = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
# #two = one ^ (one ^ two)
# two = (cp.bytes_to_long(bytes.fromhex(one)) ^ cp.bytes_to_long(bytes.fromhex(onextwo)) )
# two = bytes.hex(cp.long_to_bytes(two))
# three = (cp.bytes_to_long(bytes.fromhex(two)) ^ cp.bytes_to_long(bytes.fromhex(twoxthree)) )
# three = bytes.hex(cp.long_to_bytes(three))
# flag = (cp.bytes_to_long(bytes.fromhex(flagxall)) ^ (cp.bytes_to_long(bytes.fromhex(one)) ^ cp.bytes_to_long(bytes.fromhex(two)) ^ cp.bytes_to_long(bytes.fromhex(three)) ))
# flag = cp.long_to_bytes(flag)
# print(flag)

#ex7
# a = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
# a = bytes.fromhex(a)
# flag = " "

# for i in range(255):
#     results = [chr(n ^ i) for n in a]
#     flag = "".join(results)
#     if "crypto" in flag:
#         print(flag)
#         print(i)

#ex8
# from pwn import xor
# a = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
# b = xor(a[:7], b'crypto{')
# print(b)
# partial_key = 'myXORkey'
# print(xor(a,partial_key))
    

     




