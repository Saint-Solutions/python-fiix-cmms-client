from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'fiixclient',   
  packages = ['fiixclient'],  
  version = '1.1.2', 
  license='MIT',
  description = 'An easy to use Python wrapper for the Fiix CMMS API', 
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Ronald Langeveld',   
  author_email = 'hi@ronaldlangeveld.com',  
  url = 'https://www.ronaldlangeveld.com',
  download_url = 'https://github.com/ronaldlangeveld/python-fiix-cmms-client/archive/refs/tags/Latest.tar.gz',
  keywords = ['FIIX', 'CMMS', 'API', 'MAINTENANCE'], 
  install_requires=[   
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',  
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)