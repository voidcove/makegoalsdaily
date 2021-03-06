import os
from setuptools import find_packages, setup
from makegoalsdaily.settings.base import APP_VERSION

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), 'rb') as require:
    REQUIRE = require.read().decode('utf-8').splitlines() + ['setuptools']

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='make-goals-daily',
    version=APP_VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIRE,
    license='MIT',
    description='Make contribution to your short term goals daily.',
    long_description=README,
    url='http://makegoalsdaily.com',
    author='Sundeep Anand',
    author_email='web@sundeep.co.in',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
