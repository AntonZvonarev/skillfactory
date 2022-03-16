# Задание 12.7.3. Звонарев А.Г.
# Программа для расчета суммы вклада и поиска наиболее выгодного предложения

# Процентные ставки по вкладам
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Ввод вносимой суммы на вклад
monеy=float(input("Введите сумму, вносимую на депозит:"))
print("\nПервоначальная сумма:", monеy)

# Заполнение списка значениями накопленных сумм за год
deposit = [per_cent.get('ТКБ')*monеy/100, per_cent.get('СКБ')*monеy/100, per_cent.get('ВТБ')*monеy/100, per_cent.get('СБЕР')*monеy/100]

# Вывод на экран накопленных сумм за год
print("\nСумма процентов Вашего вклада через 12 месяцев:",
      "\nТКБ:", deposit[0],
      "\nСКБ:", deposit[1],
      "\nВТБ:", deposit[2],
      "\nСБЕР:", deposit[3],)

# Вывод на экран значения максимальной из сумм
print("\nМаксимальная сумма, которую вы можете заработать — ", max(deposit))