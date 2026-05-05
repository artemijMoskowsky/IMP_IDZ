def count_items(quantity: int) -> int:
    """
    Повертає кількість товарів

    >>> count_items(5)
    5
    >>> count_items(0)
    0
    >>> count_items(-1)
    Traceback (most recent call last):
        ...
    ValueError: Quantity cannot be negative
    """
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    return quantity


if __name__ == "__main__":
    q = int(input("Enter quantity: "))
    print(count_items(q))
