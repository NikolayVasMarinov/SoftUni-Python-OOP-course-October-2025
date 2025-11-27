def possible_permutations(el_list: list):
    if len(el_list) <= 1:
        yield el_list
        return

    for i, first in enumerate(el_list):
        rest = el_list[:i] + el_list[i + 1:]

        for perm in possible_permutations(rest):
            yield [first] + perm