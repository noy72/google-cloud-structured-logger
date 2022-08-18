.PHONY: test-deploy
test-deploy:
	rm -rf src/gcstructuredlogger/google_cloud_structured_logger.egg-info dist
	python setup.py sdist bdist_wheel
	twine upload --repository testpypi dist/*


