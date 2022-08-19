from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="google-cloud-structured-logger",
    version="0.1.1",
    url="https://github.com/noy72/google-cloud-structured-logger",
    license="BSD",
    description="A Python library adding a structured log formatter for Google Cloud",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="noy72",
    author_email="noy72@protonmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: System :: Logging',
    ],
    install_requires=[
        "python-json-logger",
    ],
    package_dir={'': 'src'},
    packages=find_packages("src", exclude="tests"),
    python_requires='>=3.5, <4',
    test_suite="tests.test_gclogger",
)
