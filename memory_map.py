import mmap

with open('tips.txt', "r+b") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    while True:
        line = m.readline()
        if line == b'':
            break
        print(line.rstrip().decode())
