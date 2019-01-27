from setuptools import setup, find_packages

setup(name="random_sample_tpgmartin",
      version="0.1",
      url="http://github.com/tpgmartin/random_sample_tpgmartin",
      author="Tom Martin",
      author_email="tpgmartin@gmail.com",
      license="MIT",
      packages=find_packages(),
      install_requires=[
        "numpy",
        "prettytable"
      ])