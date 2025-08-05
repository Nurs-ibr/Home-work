import numpy as np

def guess_number(number: int = 1) -> int:
    """Угадываем число с использованием бинарного поиска"""
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict = (low + high) // 2  # середина диапазона

        if predict == number:
            break
        elif predict < number:
            low = predict + 1
        else:
            high = predict - 1

    return count


def score_game(guess_func) -> int:
    """Запускаем игру 1000 раз и находим среднее количество попыток"""
    np.random.seed(1)  # фиксируем seed
    random_numbers = np.random.randint(1, 101, size=1000)
    attempts = [guess_func(number) for number in random_numbers]

    average_attempts = int(np.mean(attempts))
    print(f"Ваш алгоритм угадывает число в среднем за: {average_attempts} попыток")
    return average_attempts


# Запуск
score_game(guess_number)