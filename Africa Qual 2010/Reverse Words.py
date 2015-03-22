with open("B-large-practice.in") as f:
    with open("reverse-words-out.txt", "w") as fout:
        n = int(f.readline())
        for x in range(0, n):
            line = f.readline().replace('\n','')
            rev_line = line[::-1].split(' ')
            rev_line = [y[::-1] for y in rev_line]
            out = ' '.join(rev_line)
            fout.write("Case #{0}: {1}\n".format(str(x+1), out))