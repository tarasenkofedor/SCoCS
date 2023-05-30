from tests.test_objects import *


def foo_test(deserialize, serialize):
    functions = [test_mul, test_fact, test_wrapper, test_vars]
    for some_function in functions:
        sd_function = deserialize(serialize(some_function))
        assert (sd_function(5) == some_function(5))

    sd_func_with_builtin_func = deserialize(serialize(func_with_builtin_func))
    assert (sd_func_with_builtin_func([5, 4, -1, 15]) == func_with_builtin_func([5, 4, -1, 15]))


def class_test(deserialize, serialize):
    sd_class = deserialize(serialize(Person))
    sd_object = sd_class(15)
    person = Person(15)

    assert (person.religion == sd_object.religion)
    assert (person.get_age() == sd_object.get_age())


def object_test(deserialize, serialize):
    person = Person(3)
    sd_person = deserialize(serialize(person))
    assert (sd_person.age == person.age)
    assert (sd_person.religion == person.religion)
    assert (sd_person.get_age() == sd_person.get_age())


def complicated_test(deserialize, serialize):
    sd_complicated_type = deserialize(serialize(VeyComplicatedClass))
    assert (sd_complicated_type.country == VeyComplicatedClass.country)
    normal_object = VeyComplicatedClass(4)
    sd_object = sd_complicated_type(4)

    assert (sd_object.country == normal_object.country)
    assert (sd_object.get_some_useless_info() == normal_object.get_some_useless_info())


def lambda_test(deserialize, serialize):
    x = lambda a: a + 10
    y = deserialize(serialize(lambda a: a + 10))
    z = deserialize(serialize(x))
    assert (x(10) == y(10) == z(10))


def rumours_test(deserialize, serialize):
    inputs = [(1, 3), (2, 3), (14, 8)]
    sd_rumour = deserialize(serialize(rumour))
    for arg in inputs:
        assert (sd_rumour(*arg) == rumour(*arg))


def recursion_test(deserialize, serialize):
    x1 = deserialize(serialize(rec(2)))
    x2 = rec(2)

    assert (x1 == x2)
