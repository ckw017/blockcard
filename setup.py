import setuptools
import re

with open('README.md', 'r') as readme:
    long_desc = readme.read()

with open('requirements.txt', 'r') as reqf:
    requirements = reqf.read().splitlines()

version = ''
with open('blockcard/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

setuptools.setup(
    name='blockcard',
    version=version,
    author='Chris K. W.',
    author_email='chriskw.xyz@gmail.com',
    license='MIT',
    include_package_data=True,
    description='It\'s the proof-of-thought that counts',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/ckw017/blockcard',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Natural Language :: English',
    ]
)

