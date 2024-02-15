"""Модуль порівняння алгоритмів сортування"""

from random import randint
import sys
import timeit

import algorithms


# алгоритмів тестування: злиттям, вставками, вбудований sorted (використовує алгоритм Timsort)
algorithms = [algorithms.merge_sort, algorithms.insertion_sort, sorted]


def parse_arguments():
    """Отримує та парсить аргументи командного рядка"""

    attempts = "1"
    data_range_sets = "100,1000,10000"

    if len(sys.argv) > 2:
        attempts = sys.argv[1]
        data_range_sets = sys.argv[2]
    elif len(sys.argv) > 1:
        attempts = sys.argv[1]

    data_range_sets = data_range_sets.split(",")
    data_range_sets = [int(x) for x in data_range_sets]
    attempts = int(attempts)

    return (attempts, data_range_sets)


def run_tests():
    """Запускає тестування алгоритмів на тестових наборах даних"""

    attempts, data_range_sets = parse_arguments()
    algorithms_result = [0.0] * len(algorithms)

    for _ in range(attempts):
        for data_range in data_range_sets:
            random_array = [randint(1, 100) for _ in range(data_range + 1)]

            for index, algorithm in enumerate(algorithms):
                algorithms_result[index] += timeit.timeit(
                    lambda: algorithm(random_array), number=1
                )

    # Вивід статистичних даних
    print(f"Кількість спроб: {attempts}")
    print(f"Набори даних: {data_range_sets}")
    print("\nСередній час:")

    for index, algorithm in enumerate(algorithms):
        print(f"{algorithm.__name__}: {algorithms_result[index]/attempts:.6f}")


def main():
    run_tests()


if __name__ == "__main__":
    main()
