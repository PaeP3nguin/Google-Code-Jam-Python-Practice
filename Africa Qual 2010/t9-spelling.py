def main():
    keys = (('2', ('a', 'b', 'c')),
            ('3', ('d', 'e', 'f')),
            ('4', ('g', 'h', 'i')),
            ('5', ('j', 'k', 'l')),
            ('6', ('m', 'n', 'o')),
            ('7', ('p', 'q', 'r', 's')),
            ('8', ('t', 'u', 'v')),
            ('9', ('w', 'x', 'y', 'z')),
            ('0', (' ')))

    with open("C-large-practice.in") as in_file:
        with open("t9-spelling-out-large.txt", "w") as fout:
            num_lines = int(in_file.readline())
            print(num_lines)
            for x in range(0, num_lines):
                line = in_file.readline().replace('\n', '')
                out_str = ""
                for char in line:
                    for key in keys:
                        char_index = key[1].index(char) + 1 if char in key[1] else None
                        if char_index is not None:
                            if out_str[-1:] == key[0]:
                                out_str = "".join([out_str] + [' '] + [key[0]] * char_index)
                            else:
                                out_str = "".join([out_str] + [key[0]] * char_index)
                fout.write("Case #{0}: {1}\n".format(x+1, out_str))

if __name__ == "__main__":
    main()
