from setuptools import setup, find_packages

setup(
    name='emencia-product-onepage',
    version=__import__('product_onepage').__version__,
    description=__import__('product_onepage').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='dthenon@emencia.com',
    url='http://pypi.python.org/pypi/emencia-product-onepage',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'django-cms>=2.4.3',
        'django-paintstore==0.2',
    ],
    include_package_data=True,
    zip_safe=False
)