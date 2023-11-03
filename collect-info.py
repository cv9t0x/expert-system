import powerstand
import os

def process_and_save_data(column_name, data, filename):
    with open(filename, 'a') as f:
        print(column_name)
        for value in data:
            print(value.value, file=f)  # float
            print(value.value)

psm = powerstand.init()

process_and_save_data("Дома", psm.houses, "./collected-data/houses.txt")
process_and_save_data("Заводы", psm.factories, "./collected-data/factories.txt")
process_and_save_data("Больницы", psm.hospitals, "./collected-data/hospitals.txt")
process_and_save_data("Солнечные панели", psm.sun_gens, "./collected-data/sun_gen.txt")
process_and_save_data("Ветряки", psm.wind_gens, "./collected-data/wind_gen.txt")
process_and_save_data("Ветер", [psm.wind], "./collected-data/wind.txt")
process_and_save_data("Солнце", [psm.sun], "./collected-data/sun.txt")

print(os.getcwd())

psm.save_and_exit()
