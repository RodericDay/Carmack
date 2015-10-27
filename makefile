main:
	- pkill python
	python -u server.py & python -m py.test testing/tests.py
