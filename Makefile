.PHONY: build
build:
	rm -rf src/gcstructuredlogger/google_cloud_structured_logger.egg-info dist
	python setup.py sdist bdist_wheel

.PHONY: deploy
deploy: build
	twine upload --repository pypi dist/*

.PHONY: test-deploy
test-deploy: build
	twine upload --repository testpypi dist/*


