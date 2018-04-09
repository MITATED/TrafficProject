### Чем отличается список от кортежа?

1) Главное отличие в том что список является mutable типом, а кортеж immutable. Все остальные отличия исходят из этого.

```python
>>> t = [1, 2, 3, 4, 5]
>>> t[0] = 2
>>> t
[2, 2, 3, 4, 5]
>>>l = (1, 2, 3, 4, 5)
>>>l[0] = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

```
2) Важно при больших обьемах данных - списки и кортежи имеют разный размер
```python
>>> a = tuple(range(1000))
>>> b = list(range(1000))

>>> a.__sizeof__()
8024
>>> b.__sizeof__()
9088
```

3) Также исходя из того что список тип mutable его нельзя использовать в качестве ключа в словарях, в отличии от кортежа.
```python
>>> a = [1, 2]
>>> b = (1, 2)
>>> x = {a: 2}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> x = {b: 2}
>>> x[(1, 2)]
2
>>> 

```
