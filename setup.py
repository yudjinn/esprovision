from setuptools import setup

setup(
    name='esprovision',
    version='0.1',
    py_modules=['esprovision'],
    install_requires=['Click', 'jinja2'],
    entry_points='''
        [console_scripts]
        esprovision:esprovision.cli
    ''',
)
