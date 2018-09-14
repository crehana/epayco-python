try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

    def find_packages():
        return ['pyepayco']

install_requires = [
    "requests >= 2.4.3",
    "pycrypto >= 2.3"
]

setup(
    name="pyepayco",
    version="1.0.0",
    author="ePayco Development Team",
    author_email="desarrollo@epayco.co",
    packages=find_packages(),
    url='https://epayco.co/',
    download_url="https://github.com/lamurga/epayco-python",
    license="MIT",
    description="Python library for ePayco Payment API",
    long_description="Basic python library to interact with ePayco Payment API",
    install_requires=install_requires,
    include_package_data=True,
)
