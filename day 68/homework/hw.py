def count_positives_sum_negatives(arr):
    if not arr:
        return []
    return [len([x for x in arr if x > 0]), sum(x for x in arr if x < 0)]

#zogi codwars ar mexsneba saiti wedavs

def print_array(arr):
    return ",".join(str(x) for x in arr)
