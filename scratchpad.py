import re

m = re.findall(r"(?=(eight|two|\d+))", "eightwo1")
print(m)
