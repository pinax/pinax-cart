from setuptools import find_packages, setup


LONG_DESCRIPTION = """
==========
Pinax Cart
==========
.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/travis/pinax/pinax-cart.svg
    :target: https://travis-ci.org/pinax/pinax-cart
.. image:: https://img.shields.io/coveralls/pinax/pinax-cart.svg
    :target: https://coveralls.io/r/pinax/pinax-cart
.. image:: https://img.shields.io/pypi/dm/pinax-cart.svg
    :target:  https://pypi.python.org/pypi/pinax-cart/
.. image:: https://img.shields.io/pypi/v/pinax-cart.svg
    :target:  https://pypi.python.org/pypi/pinax-cart/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target:  https://pypi.python.org/pypi/pinax-cart/

Pinax
------

Pinax is an open-source platform built on the Django Web Framework. It is an
ecosystem of reusable Django apps, themes, and starter project templates.
This collection can be found at http://pinaxproject.com.
This app was developed as part of the Pinax ecosystem but is just a Django app
and can be used independently of other Pinax apps.

pinax-cart
----------

`pinax-cart` is a shopping cart app for Django.
"""


setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a shopping cart app for Django",
    name="pinax-cart",
    long_description=LONG_DESCRIPTION,
    version="0.1",
    url="http://github.com/pinax/pinax-cart/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "cart": []
    },
    test_suite="runtests.runtests",
    tests_require=[
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
