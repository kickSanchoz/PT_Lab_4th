import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def getDataset():
    """
    Survived Indicator (выжил пассажир или нет)

    Passenger Class (класс)

    Name (имя)

    Sex (пол)

    Age (возраст)

    Siblings/Spouses Aboard (есть ли братья, сестры или супруг(а) на борту)

    Parents/Children Aboard (есть ли родители или дети на борту)

    Fare(цена билета в фунтах стерлингов)

    :return: dataframe
    """
    return pd.read_csv('titanic.csv')


def checkMissingValues():
    """
    1. Определите, содержит ли какой-нибудь столбец датасета пропущенные значения.
    """
    haveNa = df.isna().values.any()
    if haveNa:
        df.dropna(inplace=True)

    print("1. Определите, содержит ли какой-нибудь столбец датасета пропущенные значения: {}".format(haveNa), "\n")


def deadFirstClassKids():
    """
    2. Число погибших детей в возрасте до 12 лет, путешествующих первым классом.
    """
    count = len(df[(df["Pclass"] == 1) & (df["Survived"] == 0) & (df["Age"] < 12)])
    print("2. Число погибших детей в возрасте до 12 лет, путешествующих первым классом: {}".format(count), "\n")


def priceDistribution(needShow: bool = False):
    """
    3. Постройте диаграмму распределения значений цены билета по всем пассажирам. Проинтерпретируйте результат.
    Можно ли сказать, что в данных наблюдаются выбросы?
    """
    if needShow:
        sns.displot(df["Fare"])
        plt.show()

    print("3. Можно ли сказать, что в данных наблюдаются выбросы?", "Выброс наблюдаются в дешевых билетах", "\n")


def ticketClassByRelatives(needShow: bool = False):
    """
    4. Чем больше родственников у человека, тем выше шанс того, что он купит билет третьего класса.
    """
    df['Relatives'] = df['Siblings/Spouses Aboard'] + df['Parents/Children Aboard']
    if needShow:
        sns.barplot(x=df["Pclass"], y=df['Relatives'])
        plt.show()

    print("4. Чем больше родственников у человека, тем выше шанс того, что он купит билет третьего класса?\n"
          "Ответ: Сгруппировав данные билетов по классу, заметно, что пассажире третьего в "
          "среднем имеют больше родственников", "\n")


def dropNameColumn():
    """
    5. Столбец с именем пассажиров вряд ли будет иметь значение для последующего анализа данных. Удалите этот столбец
    из датафрейма. Выведите на экран полученный датасет.
    """
    df.drop(['Name'], axis=1, inplace=True)
    print("5. Удалите столбец с именем пассажиров из датафрейма", df.head(), "\n")


def oneHotEncoding():
    """
    6. Столбец "пол пассажира" является категориальным. Закодируйте его с помощью ohe-hot-кодирования (OHE).
    Выведите на экран полученный датасет.
    """
    global df
    dummies = pd.get_dummies(df["Sex"], prefix="is", drop_first=True, dtype="int64")
    df = pd.concat([df, dummies], axis=1)
    df.drop(["Sex"], axis=1, inplace=True)

    print("6. Закодируйте столбец \"пол пассажира\" с помощью one-hot-кодирования\n", df, "\n")


def scatterBetweenAgeAndPrice(needShow: bool = False):
    """
    7. Постройте диаграмму рассеяния между признаками "Возраст" и "Цена билета". Проинтерпретируйте ответ.
    """
    if needShow:
        sns.scatterplot(x=df["Age"], y=df["Fare"])
        plt.show()

    print("7. Диаграмму рассеяния между признаками \"Возраст\" и \"Цена билета\"\n"
          "Ответ: В основном, люди всех возрастов покупают билеты дешевле 100 фунтов", "\n")


def normalizeAgeAndPrice():
    """

    """
    global df
    df["Age"] = (df["Age"] - df["Age"].min()) / (df["Age"].max() - df["Age"].min())
    df["Fare"] = (df["Fare"] - df["Fare"].min()) / (df["Fare"].max() - df["Fare"].min())

    print("8. Отнормируйте значения признаков \"Возраст\" и \"Цена билета\". Выведите на экран полученный датасет.\n",
          df, "\n")


def histSexAndAgeByClass(needShow: bool = False):
    """
    9. Постройте гистограммы распределения пассажиров по полу и по возрасту для каждого класса. Расположите
    гистограммы одна под другой. Оси абсцисс должны быть одинаковыми.
    """
    if needShow:
        fig, ax = plt.subplots(2, 1)
        # sns.histplot(x=dfAge.index.values, y=dfAge["Age"])
        sns.histplot(x=df["Pclass"], y=df["is_male"], ax=ax[0], cbar=True)
        sns.histplot(x=df["Pclass"], y=df["Age"], ax=ax[1], cbar=True)
        fig.tight_layout()

        plt.show()

    print("9. Гистограммы распределения пассажиров по полу и по возрасту для каждого класса. Расположите "
          "гистограммы одна под другой. Оси абсцисс должны быть одинаковыми.", "\n")


def conclusion():
     """
     10. Сделайте выводы по работе.
     """
     print("10. Сделайте выводы по работе.\n"
           "Ответ: В данной лабораторной работе мною были изучены основы работы с pandas и построение графиков "
           "с помощью seaborn.")

def main():
    # 1. Определите, содержит ли какой-нибудь столбец датасета пропущенные значения.
    checkMissingValues()

    # 2. Число погибших детей в возрасте до 12 лет, путешествующих первым классом.
    deadFirstClassKids()

    # 3. Постройте диаграмму распределения значений цены билета по всем пассажирам. Проинтерпретируйте результат.
    # Можно ли сказать, что в данных наблюдаются выбросы?
    priceDistribution(needShow=False)

    # 4. Чем больше родственников у человека, тем выше шанс того, что он купит билет третьего класса.
    # ticketClassByRelatives(needShow=True)
    ticketClassByRelatives(needShow=False)

    # 5. Столбец с именем пассажиров вряд ли будет иметь значение для последующего анализа данных. Удалите этот столбец
    # из датафрейма. Выведите на экран полученный датасет.
    dropNameColumn()

    # 6. Столбец "пол пассажира" является категориальным. Закодируйте его с помощью ohe-hot-кодирования (OHE).
    # Выведите на экран полученный датасет.
    oneHotEncoding()

    # 7. Постройте диаграмму рассеяния между признаками "Возраст" и "Цена билета". Проинтерпретируйте ответ.
    scatterBetweenAgeAndPrice(needShow=False)

    # 8. Отнормируйте значения признаков "Возраст" и "Цена билета". Выведите на экран полученный датасет.
    # normalizeAgeAndPrice()

    # 9. Постройте гистограммы распределения пассажиров по полу и по возрасту для каждого класса. Расположите
    # гистограммы одна под другой. Оси абсцисс должны быть однаковыми.
    # histSexAndAgeByClass(needShow=True)
    histSexAndAgeByClass(needShow=False)

    # 10. Сделайте выводы по работе.
    conclusion()


if __name__ == '__main__':
    pd.set_option("display.max_columns", None)
    # pd.reset_option("display.max_columns")
    pd.set_option("display.expand_frame_repr", False)

    df = getDataset()
    print(df.head())
    main()
