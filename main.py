import matplotlib.pyplot as plt


def calc_quantil(values):
    values.sort()
    k = 3 / 5 * (len(values) - 1)
    if k + 1 < 3 / 5 * len(values):
        quantile = values[int(k) + 1]
    elif k + 1 == 3 / 5 * len(values):
        quantile = (values[int(k)] + values[int(k) + 1]) / 2
    else:
        quantile = values[int(k)]
    return quantile


def draw_edf(values, name):
    values.sort()
    edf_values = [(i + 1) / len(values) for i in range(len(values))]
    plt.step(values, edf_values)
    plt.xlabel('ИМТ')
    plt.ylabel('Вероятность')
    plt.title(name)
    plt.grid(True)
    plt.show()


def draw_hist(values, name):
    plt.hist(values, bins=20)
    plt.xlabel('ИМТ')
    plt.ylabel('Количество')
    plt.title(name)
    plt.grid(True)
    plt.show()


def draw_boxplot(values, name):
    plt.boxplot(values)
    plt.xlabel('ИМТ')
    plt.title(name)
    plt.grid(True)
    plt.show()


with open("sex_bmi_smokers.csv", encoding="utf8", mode="r") as f:
    data = [i.strip().split(",") for i in f.readlines()[1:]]
    for i in range(len(data)):
        data[i][0] = data[i][0][1:-1]
        data[i][1] = float(data[i][1])
        data[i][2] = data[i][2][1:-1]

# количество курящих мужчин и некурящих женщин
cnt_smoke_men = 0
cnt_not_smoke_women = 0
for i in data:
    if i[0] == 'male' and i[2] == 'yes':
        cnt_smoke_men += 1
    elif i[0] == 'female' and i[2] == 'no':
        cnt_not_smoke_women += 1
print(f'Курящих мужчин: {cnt_smoke_men}, некурящих женщин: {cnt_not_smoke_women}. Выборка из {len(data)} испытуемых')

# значения ИМТ
bmi_values = [i[1] for i in data]

# выборочное среднее
avg = sum(bmi_values) / len(bmi_values)
print(f'Выборочное среднее ИМТ: {avg}')

# выборочная дисперсия
variance = sum([i ** 2 for i in bmi_values]) / len(bmi_values) - avg ** 2
print(f'Выборочная дисперсия ИМТ: {variance}')

# Расчет выборочной медианы
bmi_values.sort()
if len(bmi_values) % 2 == 0:
    median = (bmi_values[len(bmi_values) // 2 - 1] + bmi_values[len(bmi_values) // 2]) / 2
else:
    median = bmi_values[len(bmi_values) // 2]
print(f'Выборочная медиана ИМТ: {median}')

# Расчет выборочной квантили порядка 3/5
print(f'Выборочная квантиль порядка 3/5 ИМТ: {calc_quantil(bmi_values)}')
smoke_men = [int(i[1]) for i in filter(lambda el: el[0] == 'male' and el[2] == 'yes', data)]
print(f'Выборочная квантиль порядка 3/5 ИМТ для курящих мужчин: {calc_quantil(smoke_men)}')
not_smoke_men = [int(i[1]) for i in filter(lambda el: el[0] == 'male' and el[2] == 'no', data)]
print(f'Выборочная квантиль порядка 3/5 ИМТ для некурящих мужчин: {calc_quantil(not_smoke_men)}')
smoke_women = [int(i[1]) for i in filter(lambda el: el[0] == 'female' and el[2] == 'yes', data)]
print(f'Выборочная квантиль порядка 3/5 ИМТ для курящих женщин: {calc_quantil(smoke_women)}')
not_smoke_women = [int(i[1]) for i in filter(lambda el: el[0] == 'female' and el[2] == 'no', data)]
print(f'Выборочная квантиль порядка 3/5 ИМТ для некурящих женщин: {calc_quantil(not_smoke_women)}')

# Эмпирическая функция распределения
draw_edf(bmi_values, 'Эмпирическая функция распределения ИМТ')
draw_edf(smoke_men, 'Эмпирическая функция распределения ИМТ для курящих мужчин')
draw_edf(not_smoke_men, 'Эмпирическая функция распределения ИМТ для некурящих мужчин')
draw_edf(smoke_women, 'Эмпирическая функция распределения ИМТ для курящих женщин')
draw_edf(not_smoke_women, 'Эмпирическая функция распределения ИМТ для некурящих женщин')

# Гистограмма
draw_hist(bmi_values, 'Гистограмма ИМТ')
draw_hist(smoke_men, 'Гистограмма ИМТ для курящих мужчин')
draw_hist(not_smoke_men, 'Гистограмма ИМТ для некурящих мужчин')
draw_hist(smoke_women, 'Гистограмма ИМТ для курящих женщин')
draw_hist(not_smoke_women, 'Гистограмма ИМТ для некурящих женщин')

# box-plot
draw_boxplot(bmi_values, 'Box-plot ИМТ')
draw_boxplot(smoke_men, 'Box-plot ИМТ для курящих мужчин')
draw_boxplot(not_smoke_men, 'Box-plot ИМТ для некурящих мужчин')
draw_boxplot(smoke_women, 'Box-plot ИМТ для курящих женщин')
draw_boxplot(not_smoke_women, 'Box-plot ИМТ для некурящих женщин')
