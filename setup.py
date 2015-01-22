import sys
import errno
import subprocess
from distutils.core import setup


VERSION_FILE = 'LNcommon/version.py'
PY3 = sys.version_info[0] >= 3


def get_version():
    if PY3:
        version_vars = {}
        with open(VERSION_FILE) as f:
            code = compile(f.read(), VERSION_FILE, 'exec')
            exec(code, None, version_vars)
        return version_vars['__version__']
    else:
        execfile(VERSION_FILE)
        return __version__


setup(
    name='LNcommon',
    version=get_version(),
    description='The LN Digitals common function modules.',
    author='Lemaker',
    author_email='support@lemaker.org',
    license='GPLv3+',
    url='https://github.com/LeMaker/LNcommon',
    packages=['LNcommon'],
    long_description=open('README.md').read(),
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or "
        "later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='LN Digitals common functions bananapi',
)
