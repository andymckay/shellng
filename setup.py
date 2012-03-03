from distutils.core import setup
import os

setup(
    name='django-shellng',
    version='0.1.2',
    description='Improved shell for Django',
    long_description=open(os.path.join(
                          os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/andymckay/shellng',
    author='Andy McKay',
    license='BSD',
    author_email='andy@clearwind.ca',
    packages=['shellng',
              'shellng/management',
              'shellng/management/commands'],
    include_package_data=True,
    zip_safe=True,
    classifiers=['Programming Language :: Python',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Framework :: Django'],
)
