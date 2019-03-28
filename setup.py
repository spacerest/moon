from distutils.core import setup

setup(
    name = 'moonmask',
    packages = ['moonmask'],
    version = '1.2',
    license='MIT',
    description = 'Gets moon visualizations courtesy of Ernie Wright and uses them for artistic collages',
    author = 'Sadie Parker',
    author_email = 'sadiemparker@gmail.com',
    url = 'https://github.com/spacerest/moonmask',
    download_url = 'https://github.com/spacerest/moonmask/archive/v_12.tar.gz',
    keywords = ['MOON', 'ART'],
    install_requires=[
        'Pillow==5.4.1',
        'decorator==4.0.11',
        'imageio==2.1.2',
        'InstagramAPI==1.0.2',
        'moviepy==0.2.3.2',
        'numpy==1.16.2',
        'requests==2.20.0',
        'requests-toolbelt==0.7.0',
        'tqdm==4.11.2'
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
