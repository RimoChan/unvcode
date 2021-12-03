import setuptools


setuptools.setup(
    name='unvcode',
    version='1.0.0',
    author='RimoChan',
    author_email='the@librian.net',
    description='unvcode',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RimoChan/unvcode',
    packages=['unvcode'],
    package_data={
        'unvcode': ['NotoSerifSC-SemiBold.otf'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'numpy>=1.16.6',
        'Pillow>=8.0.1',
    ],
    python_requires='>=3.6',
)
