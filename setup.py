from setuptools import setup, find_packages

setup(
    name='MITS_gems',
    version='0.1',
    packages=find_packages(),
    description='A simple Euclidean distance calculator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PenugondaAyesha/MITS_gems',
    author='Ayesha_Ganeshwari_Manasa',
    author_email='payesha171@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)