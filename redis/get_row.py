count = 0

thefile = open('m_value', 'rb')

while True:
    buffer = thefile.read(1024 * 8192)
    if not buffer:
        break
    count += buffer.count('\n')
thefile.close()

print count