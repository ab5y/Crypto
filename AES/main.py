from Crypto.Cipher import AES
from Crypto import Random
from CtrMode import CtrMode

ct1 = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
key = '36f18357be4dbd77f050515c73fcf9f2'
ctrMode = CtrMode()
print ctrMode.decrypt(ct1, key)
# print type(Random.new().read(AES.block_size))