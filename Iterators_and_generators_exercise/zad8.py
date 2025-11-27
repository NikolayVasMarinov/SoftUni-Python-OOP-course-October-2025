def get_primes(nums_list: list[int]):
    for num in nums_list:
        if num <= 1:
            continue

        for i in range(2, num):
            if num % i == 0:
                break

        else:
            yield num