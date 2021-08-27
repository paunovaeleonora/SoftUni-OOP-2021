class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class TestIntegersList(TestCase):
    def test_init_attr(self):
        integers_list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual([1, 2, 3, 4, 5], integers_list._IntegerList__data)

    def test_add_operation(self):
        integers_list = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(ValueError) as ex:
            integers_list.add('5')
        self.assertEqual('Element is not Integer', str(ex.exception))

        result = integers_list.add(6)
        self.assertEqual([1, 2, 3, 4, 5, 6], result)

    def test_remove_index(self):
        integers_list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual([1, 2, 3, 4, 5], integers_list.get_data())

        integers_list.remove_index(0)
        expected_result = [2, 3, 4, 5]
        actual_result = integers_list.get_data()
        self.assertEqual(expected_result, actual_result)

        integers_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], integers_list.get_data())

        with self.assertRaises(IndexError) as ex:
            integers_list.remove_index(4)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_init(self):
        integers_list = IntegerList(1, 2, 3, 4, 'agdgyh')
        self.assertEqual([1, 2, 3, 4], integers_list._IntegerList__data)

    def test_get(self):
        integers_list = IntegerList(1, 2, 3, 4, 'agdgyh')
        self.assertEqual([1, 2, 3, 4], integers_list.get_data())
        integers_list.get(2)
        self.assertEqual(3, integers_list.get_data()[2])

        with self.assertRaises(IndexError) as ex:
            integers_list.get(6)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert(self):
        integers_list = IntegerList(1, 2, 3, 4, 'agdgyh')
        self.assertEqual([1, 2, 3, 4], integers_list.get_data())
        integers_list.insert(2, 2)
        self.assertEqual([1, 2, 2, 3, 4], integers_list.get_data())

        ints_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], ints_list.get_data())
        with self.assertRaises(IndexError) as ex:
            ints_list.insert(3, 1)
        self.assertEqual('Index is out of range', str(ex.exception))

        int_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2,3], int_list.get_data())
        with self.assertRaises(ValueError) as ex:
            int_list.insert(0, 'a')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_get_biggest(self):
        integers_list = IntegerList(1, 2, 3, 4)
        self.assertEqual(4, integers_list.get_biggest())

    def test_get_index(self):
        integers_list = IntegerList(1, 2, 3, 4)
        self.assertEqual([1, 2, 3, 4], integers_list.get_data())
        integers_list.get_index(4)
        self.assertEqual(3, integers_list.get_index(4))


if __name__ == '__main__':
    main()
