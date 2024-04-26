import re
def verify_IPv4(input: str)-> bool:
	if isinstance(input, str):
		ipv4_regex = re.compile(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$')
		if ipv4_regex.match(input):
			return True
	return False