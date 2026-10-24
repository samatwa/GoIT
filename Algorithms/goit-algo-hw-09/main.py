import timeit


# Функція жадібного алгоритму find_coins_greedy
def find_coins_greedy(amount, coins):
    # Сортуємо масив номіналів монет за спаданням
    coins.sort(reverse=True)
    # Результат у вигляді словника, де ключ - номінал монети, значення - кількість монет
    result = {}
    # Проходимося по всіх номіналах монет
    for coin in coins:
        if amount >= coin:
            # Знаходимо максимальну кількість поточного номіналу монет, які можна використати
            count = amount // coin
            # Зменшуємо суму на відповідну кількість цих монет
            amount -= coin * count
            # Зберігаємо кількість монет у результаті
            result[coin] = count
    return result


# Функція динамічного програмування find_min_coins
def find_min_coins(amount, coins):
    # Сортуємо масив номіналів монет за спаданням
    coins.sort(reverse=True)
    # Ініціалізуємо масив для зберігання мінімальної кількості монет для кожної суми
    min_coins = [0] + [float('inf')] * amount
    # Ініціалізуємо масив для зберігання останньої використаної монети для кожної суми
    coin_used = [0] * (amount + 1)
    # Заповнюємо масив мінімальної кількості монет для кожної можливої суми
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin
    # Відновлюємо комбінацію монет за допомогою масиву coin_used
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    return result


def main():
    # Набір доступних монет
    coins = [50, 25, 10, 5, 2, 1]
    # Тестова сума для перевірки
    amount = 113

    print(find_coins_greedy(amount, coins))
    print(find_min_coins(amount, coins))
    print()

    # Тестування часу виконання
    greedy_time = timeit.timeit(
        lambda: find_coins_greedy(amount, coins), number=100000)
    dp_time = timeit.timeit(
        lambda: find_min_coins(amount, coins), number=100000)

    print(f"Test time for greedy algorithm: {greedy_time:.6f} seconds")
    print(f"Test time for dynamic programming: {dp_time:.6f} seconds")


if __name__ == "__main__":
    main()
