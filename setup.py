from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(name='regex_builder',
    author='Zomatree',
    url='https://github.com/Zomatree/regex-builder',
    version="1.0.0",
    packages=['regex_builder'],
    license='MIT',
    description='programmatically make regex in python',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.0',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
