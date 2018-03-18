from setuptools import setup

setup (
        name='cli',
        version='1.0',
        packages=['cli'],
        include_package_data=True,
        install_requires=[
            'click',
            ],
        entry_points='''
           [console_scripts]
           cli=cli.cli:main
        ''',
        )
