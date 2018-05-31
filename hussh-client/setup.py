import setuptools

setuptools.setup(name='hussh',
                 #version=Version('1.0.0').number,
                 version=1.0,
                 description='Hussh an improved ssh sharing tool',
                 #long_description=open('README.md').read().strip(),
                 author='Surya Prashanth',
                 author_email='prashantsurya@ymail.com',
                 #url='http://path-to-my-packagename',
                 py_modules=['hussh'],
                 install_requires=['Click'],
                 license='MIT License',
                 entry_points='''
                    [console_scripts]
                    hussh=hussh:cli
                 ''',
                 zip_safe=False)