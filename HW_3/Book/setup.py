from setuptools import setup, find_namespace_packages

setup(
    name='Book',
    version='1.0.0',
    description='DictBook',
    url='http://github.com/dummy_user/useful',
    author='Roman',
    author_email='dp240193srn@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['Book = Book.Book_rev1:main']}
)
