from claseconjunto import Conjunto

def test():

	conjunto1 = Conjunto([1, 2, 3, 4])
	conjunto2 = Conjunto([4, 6, 7])
	conjunto3 = Conjunto([1, 2, 3, 4])

	assert conjunto1 == conjunto3
	assert conjunto1 != conjunto2
	assert conjunto1 + conjunto2 == Conjunto([1, 2, 3, 4, 6, 7])
	assert conjunto1 - conjunto2 == Conjunto([1, 2, 3])


if __name__ == '__main__':

	test()
	conjunto1 = Conjunto([1, 2, 3, 4])
	conjunto2 = Conjunto([3, 6, 9])
	conjunto3 = Conjunto([1, 2, 3, 4])

	print("Conjunto 1:", conjunto1)
	print("Conjunto 2:", conjunto2)
	print("Conjunto 3:", conjunto3)
	print("1 + 2:",  conjunto1 +  conjunto2)
	print("1 - 2:",  conjunto1 -  conjunto2)
	print("1 == 2:", conjunto1 == conjunto2)
	print("1 == 3:", conjunto1 == conjunto3)
