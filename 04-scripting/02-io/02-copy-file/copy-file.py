import sys
with open(sys.argv[1], 'r') as f1:
    content = f1.read()
with open(sys.argv[2], 'w') as f2:
    f2.write(content)