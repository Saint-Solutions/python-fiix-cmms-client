from distutils.core import setup

setup(
  name = 'fiixclient',         # How you named your package folder (MyLib)
  packages = ['fiixclient'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'An easy to use Python wrapper for the Fiix CMMS API',   # Give a short description about your library
  author = 'Ronald Langeveld',                   # Type in your name
  author_email = 'hi@ronaldlangeveld.com',      # Type in your E-Mail
  url = 'https://www.ronaldlangeveld.com',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ronaldlangeveld/python-fiix-cmms-client/archive/refs/tags/Beta.tar.gz',    # I explain this later on
  keywords = ['FIIX', 'CMMS', 'API', 'MAINTENANCE'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)