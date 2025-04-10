# coding: utf-8

"""
    Conekta API

    Conekta sdk

    The version of the OpenAPI document: 2.2.0
    Contact: engineering@conekta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "conekta"
VERSION = "7.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Conekta API",
    author="Engineering Conekta",
    author_email="engineering@conekta.com",
    url="https://github.com/conekta/conekta-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Conekta API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT-LICENSE",
    long_description_content_type='text/markdown',
    long_description="""\
    Conekta sdk
    """,  # noqa: E501
    package_data={"conekta": ["py.typed"]},
)
