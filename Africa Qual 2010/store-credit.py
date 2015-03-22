def main():
    with open("A-large-practice.in") as in_file:
        with open("store-credit-out-large.txt", "w") as fout:
            num_lines = int(in_file.readline())
            print(num_lines)
            for x in range(1, num_lines + 1):
                credit = int(in_file.readline())
                item_count = int(in_file.readline())
                items = in_file.readline().replace('\n', '').split(' ')
                items = [int(y) for y in items]
                items_sorted = sorted(items)
                i = 0
                j = len(items_sorted) - 1
                total = items_sorted[i] + items_sorted[j]
                while total != credit:
                    if total < credit:
                        i += 1
                    else:
                        j -= 1
                    total = items_sorted[i] + items_sorted[j]

                i = items.index(items_sorted[i]) + 1
                j = len(items) - items[::-1].index(items_sorted[j])
                result = [i, j]
                result.sort()
                result = [str(y) for y in result]
                result = ' '.join(result)
                fout.write("Case #{0}: {1}\n".format(x, result))

if __name__ == "__main__":
    main()
