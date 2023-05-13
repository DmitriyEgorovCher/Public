def sorting(l):
    for i in range(len(l)):
        x = l[i]
        idx = i
        while idx > 0 and l[idx - 1] > x:
            l[idx] = l[idx - 1]
            idx -= 1
        l[idx] = x
    return l


def binary_search(array, num, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if num > array[middle] and num <= array[middle + 1]:
        return middle, middle + 1
    elif array[middle] == num:
        return middle - 1, middle
    elif num < array[middle]:
        return binary_search(array, num, left, middle - 1)
    else:
        return binary_search(array, num, middle + 1, right)

l = (list(map(int, input('Введите числа от 1 до 999 через пробел: ').split())))
array = sorting(l)

while True:
    try:
        num = int(input("Введите число от 1 до 999: "))
        if num <= 0 or num > 999 or num > max(l):
            raise Exception
        break

    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")

print(binary_search(array,num,0,len(array)-1))

