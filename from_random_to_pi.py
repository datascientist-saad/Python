import random
import matplotlib.pyplot as plt

def estimate_pi(n):
        num_in_circle = 0
        num_in_total = 0
        for i in range(n):
                x = random.uniform(0, 1)
                y = random.uniform(0, 1)
                distance = x**2 + y**2
                if distance <= 1:
                        num_in_circle += 1
                
                num_in_total += 1
                # plt.scatter(x, y)
                # plt.show()
        return 4 * num_in_circle / num_in_total

number_of_points = int(input("Enter number = "))

print(estimate_pi(number_of_points))