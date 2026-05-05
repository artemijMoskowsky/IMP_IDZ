# Test CI

Невеликий Python-додаток для створення CI.

---

## Можливості

* Юніт-тести
* Док-тести
* Перевірка форматування

---

## Завантаження

1. Схиляти репозиторій:

``` bash
git clone https://github.com/artemijMoskowsky/IMP_IDZ
```

2. Перейти до папки проекту:

``` bash
cd IMP_IDZ
```

---

## Запуск

Запуск основної програми:

``` bash
python -m app.cart
```

---

## Запуск тестів

Тести запускаються через окремий файл:

``` bash
python -m tests.test_cart
```

## Вимоги

* Python 3.8+

---

## Налаштування Git-Hook
``` bash
  pip install -r requirements.txt
  pre-commit install
```