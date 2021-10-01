try:
	a = float (input('Введите A'))
	b = float (input('Введите B'))
	c = float (input('Введите C'))
	if a < b and b < c:
		print('Выполняется A<B<C')
	elif a > b and b > c:
		print('Выполняется A>B>C')
	elif a == b or b == c:
		print('Ни одно из двух неравенств не выполняется')
	else:
		print('Ни одно из двух неравенств не выполняется')
except ValueError :
	print('Ошибка. Ввидети число.')
