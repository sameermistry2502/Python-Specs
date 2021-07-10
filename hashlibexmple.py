import hashlib

hash_var = hashlib.md5()

type(hash_var)
hash_var.update("sameer")

print(hash_var.digest())
