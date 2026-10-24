import random
import matplotlib.pyplot as plt

def roll_dice(num_rolls):
    sums = [0] * 13  # Індекси від 0 до 12, але ми використовуємо тільки від 2 до 12
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums[die1 + die2] += 1
    return sums

def calculate_probabilities(sums, num_rolls):
    probabilities = [count / num_rolls for count in sums]
    return probabilities

def monte_carlo_simulation(num_rolls):
    sums = roll_dice(num_rolls)
    probabilities = calculate_probabilities(sums, num_rolls)
    return probabilities

def plot_probabilities(probabilities):
    possible_sums = list(range(2, 13))
    analytical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

    plt.figure(figsize=(10, 6))
    plt.bar(possible_sums, probabilities[2:], width=0.4, label='Monte Carlo', color='blue', alpha=0.7)
    plt.bar([x + 0.4 for x in possible_sums], analytical_probabilities, width=0.4, label='Analytical', color='red', alpha=0.7)
    plt.xlabel('Sum')
    plt.ylabel('Probability')
    plt.title('Probability of Sum')
    plt.xticks(possible_sums)
    plt.legend()
    plt.show()

def main():
    num_rolls = 1000000  # Велика кількість кидків для методу Монте-Карло
    probabilities = monte_carlo_simulation(num_rolls)
    
    # Виведення результатів
    print("Monte Carlo probabilities:")
    print("Sum\tProbability")
    for i in range(2, 13):
        print(f"{i}\t{probabilities[i]:.4f}")
    
    # Порівняння з аналітичними ймовірностями
    print("\nAnalytical probabilities:")
    analytical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    print("Sum\tProbability")
    for i, prob in zip(range(2, 13), analytical_probabilities):
        print(f"{i}\t{prob:.4f}")
    
    # Побудова графіка
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
