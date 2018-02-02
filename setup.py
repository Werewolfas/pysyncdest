import re
from distutils.core import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open('pysyncdest/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(name='pysyncdest',
      author='werewolfas',
      author_email='werewolfas@gmail.com',
      version=version,
      license='MIT',
      description='an Destiny 2 API wrapper (for of jgayfer/pydest)',
      install_requires=requirements,
      packages=['pysyncdest'])
