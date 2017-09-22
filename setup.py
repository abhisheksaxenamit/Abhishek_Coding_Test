from setuptools import setup

setup(name='BBC_Coding_Test',
      version='0.1',
      description='Validating http urls and storing response',
      url='https://github.com/abhisheksaxenamit/Abhishek_Coding_Test.git',
      author='Abhishek Saxena',
      author_email='abhishek.saxena.mit@gmail.com',
      license='MIT',
      packages=['BBC_Coding_Test'],
      install_requires=[
          'urllib3',
          'requests',
      ],
      zip_safe=False)
