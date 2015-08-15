.PHONY: bootstrap
bootstrap :
	pip install -r requirements.txt

.PHONY: install
install : bootstrap
	bash scripts/install.sh

.PHONY: tests
tests :
	python -u -m unittest discover . '*_test.py'

.PHONY: coverage
coverage: coverage_run coverage_report

coverage_run :
	coverage run --omit *_test.py,**/*_test.py,**/__init__.py,/usr/local/lib/python2.7/** -m unittest discover . '*_test.py'

coverage_report:
	coverage report
