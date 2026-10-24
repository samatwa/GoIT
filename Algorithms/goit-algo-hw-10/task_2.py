import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
import random

# Візуалізація
def visualize_graph(f, a, b):
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Integration graph of f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


# Метод Монте-Карло
def monte_carlo_integration(f, a, b, num_points):
    """Виконує обчислення визначеного інтеграла методом Монте-Карло."""
    total_sum = 0
    for _ in range(num_points):
        x = random.uniform(a, b)
        total_sum += f(x)
    integral = (b - a) * total_sum / num_points
    return integral

def main():
    # Визначення функції
    def f(x):
        return x ** 2

    # Межі інтегрування
    a = 0
    b = 2

    # кількість випадкових точок
    num_points = 10000

    # Метод Монте-Карло
    integral_mc = monte_carlo_integration(f, a, b, num_points)
    # Перевірка за допомогою quad
    integral_quad, error = spi.quad(f, a, b)

    # Вивід результатів
    print(f"Integral using Monte Carlo: {integral_mc}")
    print(f"Integral using quad: {integral_quad}")
    print(f"Difference: {abs(integral_mc - integral_quad)}")

    # Візуалізація
    visualize_graph(f, a, b)


if __name__ == "__main__":
    main()