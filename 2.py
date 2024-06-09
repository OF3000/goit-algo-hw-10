import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

def draw_func(x_in, y_in, a, b):

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)
    ax.scatter(x_in,y_in, color = "red")

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

def monte_carlo(a,b, iterations):
    x_rand = np.random.uniform(a,b, iterations)
    y_rand = np.random.uniform(0, f(b), iterations)
    under_curve = y_rand < f(x_rand)
    integral_mk = (b - a) * f(b) * np.sum(under_curve) / iterations

    result, error = spi.quad(f, a, b)

    draw_func(x_rand,y_rand,a,b)
    print(f"Monte karlo: {integral_mk}; quad: {result}") 




if __name__ == "__main__":
    a = 0  # Нижня межа
    b = 2  # Верхня межа
    iterations = [100, 1000, 10000, 100000]

    for iter in iterations:
        monte_carlo(a, b, iter)
    
