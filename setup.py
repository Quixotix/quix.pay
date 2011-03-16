from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Quixotix Payment', 
    version='0.1.4',
    description='Abstract interfacing with online payment gateways such as Authorize.Net.',
    long_description=read('README'),
    author='Micah Carrick',
    url='http://www.quixotix.com',
    author_email='software@quixotix.com',
    packages=find_packages(),
    namespace_packages=['quix'],
    install_requires=['setuptools'],
    license='BSD',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries ",
    ],
    keywords = 'payment gateway processor credit card authorize.net AIM paypal'
)
