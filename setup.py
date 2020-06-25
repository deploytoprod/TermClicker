import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TermClicker",
    version="1.0.0",
    author="Rafael Lopes",
    author_email="dev@rafalop.es",
    description="Your CLI presentations will never be the same!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bobeirasa/TermClicker",
    py_modules=['itermprint','itermreprint'],
    entry_points={'console_scripts':
                ['tcprint = itermprint:main',
                'tcreprint = itermreprint:main']}
)
