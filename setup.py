# setup.py
from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid-ipython',
    'waitress',
    'sqlalchemy',
    'psycopg2'
]

setup(
    name='pyramid_todo',
    version='0.0',
    description='A To-Do List build with Pyramid',
    author='<Your name>',
    author_email='<Your email>',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    # This allows the plaster_pastedeploy package to access what will be the main function in the application for building an application object and serving it.
    entry_points={
        'paste.app_factory': [
            'main = todo:main',
        ]
    }
)