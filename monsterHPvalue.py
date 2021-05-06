def checkMonsterLive(array, hp, start):
    total = hp
    total_array = 0
    original_start = start
    while 1:
        total_array += array[start]
        hp += array[start]
        if hp <= 0:
            return start
        print("start: ", start, "array: ", array[start], "hp: ", hp, "total_array: ", total_array)
        start += 1
        start  = start%len(array)
        if start == original_start:
            break

    if total_array >= 0:
        return -1

    else:
        hp = hp % (-total_array)
        while hp > 0:
            hp += array[start]
            if hp  <= 0:
                return start
            start += 1
            start %= len(array)

    return start

if __name__ == "__main__":
    array = [-2, -3, 4, -5, 10]
    hp = 6
    print(checkMonsterLive(array, hp, 3))

