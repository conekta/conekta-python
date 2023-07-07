# coding: utf-8

"""
    Conekta API

    Conekta sdk  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@conekta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "conekta"
VERSION = "6.0.1"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum"
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
    Conekta sdk  # noqa: E501
    """
)
