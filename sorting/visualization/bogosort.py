import matplotlib.pyplot as plt
import numpy as np

def visualize(function):
    def wrapper(array):
        n_print = 10
        for i, a in enumerate(function(array)):
            if n_print > 0:
                print(f"guess {i:>4}: {a}. Nope.")
            elif n_print == 0:
                print(f"{'':6}...")
            n_print -= 1
        print(f"guess {i:>4}: {a}. Yes!")

        print("\nTrying 100 more times...")
        n_iterations = []
        for _ in range(100):
            i_max = 0
            for _ in function(array):
                i_max += 1
            n_iterations.append(i_max)
        
        i, n = np.unique(n_iterations, return_counts=True)
        print(f"avg n_iterations: {np.mean(n_iterations):.3f}")
        print(f"std n_iterations: {np.std(n_iterations):.3f}")

        plt.bar(i, n, width=[5]*len(i))
        plt.yticks(range(0, max(n)+1))
        plt.xlabel("n_iterations")
        plt.ylabel("frequency")

    return wrapper
