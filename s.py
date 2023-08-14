#!/usr/bin/env python3

import hashlib

c = 'teste'
a = str(c).encode('utf-8')
result = hashlib.md5(a).hexdigest()
print(result)

