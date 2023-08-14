#!/usr/bin/env python3

import hashlib

c = 'Shaweds'
a = str(c).encode('utf-8')
result = hashlib.sha256(a).hexdigest()
print(result)

