from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = 'dialamoon',
    packages = find_packages(),
    version = '1.0',
    license='MIT',
    description = 'Gets moon visualizations courtesy of NASA/Ernie Wright',
    author = 'Sadie Parker',
    author_email = 'sadiemparker@gmail.com',
    url = 'https://github.com/spacerest/dialamoon',
    download_url = 'https://github.com/spacerest/dialamoon/archive/v_1_0.tar.gz',
    keywords = ['MOON', 'ART'],
    install_requires=[
        'numpy~=1.17.1',
        'opencv-python~=4.1.1.26'
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Other Audience',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
