import setuptools

setuptools.setup(
    name="wdm",
    version="0.1.0",
    author="Egor Dmitriev",
    author_email="egordmitriev2@gmail.com",
    description="WebDevMagento Tools",
    long_description='WebDevMagento Tools',
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'wdm = wdm.main:cli'
        ]
    }
)
