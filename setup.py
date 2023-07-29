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
    packages=find_packages(),
    keywords = ['streamlit', 'api', 'bls']
    url = 'https://github.com/tonyhollaar/',
    install_requires=[
        'streamlit',
        'requests',
        'pandas',
    ],
classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    ],
)
