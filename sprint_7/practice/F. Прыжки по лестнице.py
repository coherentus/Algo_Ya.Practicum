def get_quantity(to_step, jmp_size):
    dp = [0] * (to_step)
    dp[0] = 1
    for i in range(to_step - 1):
        for j in range(i + 1, min(i + 1 + jmp_size, to_step)):
            dp[j] = (dp[i] + dp[j]) % 1000000007
    return dp.pop()


def main():
    with open('input.txt') as file_in:
        num_n, num_k = list(map(int, file_in.readline().split()))
        file_in.close()

    print(get_quantity(num_n, num_k))


if __name__ == '__main__':
    main()
