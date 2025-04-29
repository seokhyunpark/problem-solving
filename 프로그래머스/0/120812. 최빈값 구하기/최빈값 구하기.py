def solution(array):
    numbers = {}
    for number in array:
        if number not in numbers.keys():
            numbers[number] = 0
        numbers[number] += 1

    sorted_numbers = sorted(numbers.items(), key=lambda x: x[1], reverse = True)
    if len(sorted_numbers) > 1 and sorted_numbers[0][1] == sorted_numbers[1][1]:
        return -1
    return sorted_numbers[0][0]
