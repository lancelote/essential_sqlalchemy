help:
	@echo "update"
	@echo "    install all requirements"
	@echo "requirements"
	@echo "    update requirements"

update:
	python -m pip install -U pip setuptools
	python -m pip install -r requirements.txt

requirements:
	pur -r requirements.txt