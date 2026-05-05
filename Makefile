run:
	python app/cart.py

test:
	python -m tests.test_cart
	python -m doctest app/cart.py

fromat:
	black .

lint:
	flake8 .

check:
	safety check