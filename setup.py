import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='blockstream',
      version='0.2.0',
      author='psqnt',
      description='API wrapper for blockstream block explorer',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/pasquantonio/blockstream',
      license='MIT',
      packages=setuptools.find_packages(),
      python_requires='>=3',
      install_requires=['requests'],
      classfifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSE Approved :: MIT License',
            'Operating System :: OS Independent',
      ],
)
