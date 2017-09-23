from setuptools import setup

setup(name='BBC_Coding_Test',
      version='0.2',
      description='Fixing Bugs, adding unit test cases',
      url='https://github.com/abhisheksaxenamit/Abhishek_Coding_Test.git',
      author='Abhishek Saxena',
      author_email='abhishek.saxena.mit@gmail.com',
      license='MIT',
      packages=['BBC_Coding_Test'],
      install_requires=[
          'urllib3',
          'requests',
          'tldextract',
      ],
      zip_safe=False)
