import pandas as pd
import matplotlib.pyplot as plt

def plot_graphs(csv_filename):
    data = pd.read_csv(csv_filename)

    wind_A = data['Ветер:А']
    wind_B = data['Ветер:Б']
    sun = data['Солнце']
    hospitals = data['Больницы']
    factories = data['Заводы']
    homes_A = data['Дома А']
    homes_B = data['Дома Б']

    plt.figure(figsize=(10, 6))

    plt.plot(wind_A, label='Ветер:А')
    plt.plot(wind_B, label='Ветер:Б')
    plt.plot(sun, label='Солнце')
    plt.title('График генерации')
    plt.xlabel('Время')
    plt.ylabel('Значение')
    plt.legend()

    plt.figure(figsize=(10, 6))
    plt.plot(hospitals, label='Больницы')
    plt.plot(factories, label='Заводы')
    plt.plot(homes_A, label='Дома А')
    plt.plot(homes_B, label='Дома Б')
    plt.title('График потребления')
    plt.xlabel('Время')
    plt.ylabel('Значение')
    plt.legend()

    plt.show()

if __name__ == '__main__':
    csv_filename = './data/forecast_2023-06-22T02.37_58.978Z.csv'
    plot_graphs(csv_filename)
