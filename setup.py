# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pathlib import Path


install_requires = [
    'colorama>=0.4.3,<=0.5.0',
    'docker>=4.2.2,<5.0.0',
    'typer>=0.3.1,<0.4.0',
    'pillow>=7.2.0<8.0.0',
]

entry_points = {
    'console_scripts': [
        'battlebots = battlebots.__main__:main'
    ]
}

here = Path.resolve(Path(__file__).parent)
def read(fname):
    with open(here / fname, 'r') as f:
        return f.read()

setup_kwargs = {
    'name': 'battlebots',
    'version': '1.0.0',
    'description': 'BagelCon Battlebots Runner',
    'long_description': read('README.md'),
    'long_description_content_type': 'text/markdown',
    'author': 'Tyler Lubeck',
    'author_email': 'tyler@tylerlubeck.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TylerLubeck/battlebots',
    'package_dir': {'': 'src'},
    'packages': find_packages('src'),
    'package_data': {'': ['*']},
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}

setup(**setup_kwargs)
