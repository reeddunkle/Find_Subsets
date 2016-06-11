
STARTING_SET = {'A', 'B'}
TEST = [set([]), {'A'}, {'B'}, {'A', 'B'}]

set_to_run = set()
for item in STARTING_SET:
    set_to_run.add(item)



def find_subsets(s):

    if len(s) == 0:
        empty = set()
        return [empty]

    else:
        to_apply = set()
        to_apply.add(s.pop())
        result = find_subsets(s)
        subsets = []

        for item in result:
            new_subset = set.union(item, to_apply)
            subsets.append(item)
            subsets.append(new_subset)

    return subsets


if __name__ == '__main__':

    subsets = find_subsets(set_to_run)

    print("")
    print("Given the starting set:\n{}\n".format(STARTING_SET))
    print("The found subsets are:\n{}\n".format(subsets))
    print("These are the expected results:\n{}\n".format(TEST == subsets))
