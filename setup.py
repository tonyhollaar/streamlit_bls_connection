from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='streamlit_bls_connection',
    version='0.5',
    license='MIT',  
    description='A package to fetch Bureau of Labor Statistics data using Streamlit',
    author='Tony Hollaar',
    author_email='thollaar@gmail.com',
    url='https://github.com/tonyhollaar/',
    download_url='https://github.com/tonyhollaar/streamlit_bls_connection/archive/refs/tags/v4.tar.gz',
    packages=find_packages(),
    keywords=['streamlit', 'api', 'bls'],  # <-- Comma added here
    install_requires=[
        'streamlit',
        'requests',
        'pandas',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)