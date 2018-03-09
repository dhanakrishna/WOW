
#!/usr/bin/python3
def add(*args):
	s = 0;
	for x in args:
		s = s+x;
	return s


z  = add(*[1,2,3,4])
print(z)
