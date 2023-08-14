#!/usr/bin/env python3

import hashlib

for c in range(-10,16):
	a = str(c).encode('utf-8')
	result = hashlib.md5(a).hexdigest()
	print(c ,' : ', result)
