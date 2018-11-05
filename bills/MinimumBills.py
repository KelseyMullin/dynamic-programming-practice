def num_bills_dynamic(k, D):
    A = [0]
    for j in range(1, k + 1):
        mn = k + 1
        for i in range(1, 9):
            if D[i] == j:
                mn = 1
            elif D[i] < j:
                temp = A[D[i]] + A[j - D[i]]
                if temp < mn:
                    mn = temp
        A.append(mn)
    return A


def num_bills_greedy(k, D):
    num = 0
    while k > 0:
        i = 1
        while i < 9 and D[i] <= k:
            i = i + 1
        k = k - D[i-1]
        num = num + 1
    return num


def num_bills_greedy_array(n, D):
    C = [0]
    for j in range(1, n+1):
        C.append(num_bills_greedy(j, D))
    return C


dream_dollars = [0, 1, 4, 7, 13, 28, 52, 91, 365]
b = 1000

dynamic_array = num_bills_dynamic(b, dream_dollars)
greedy_array = num_bills_greedy_array(b, dream_dollars)


for i in range(1, b):
    if dynamic_array[i] != greedy_array[i]:
        print("Greedy algorithm is wrong for: $" + str(i))
        print("Greedy: {} bills; Dynamic: {} bills\n".format(greedy_array[i], dynamic_array[i]))