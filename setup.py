from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read().rstrip()

setup(
    name="logger_generate",
    version="0.1.3",
    keywords=("logger", "logging", "generate"),
    description="開箱即用的logger。 easy to generate logger.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/we684123/logger_generate",
    author="we684123",
    author_email="we684123@gmail.com",
    packages=find_packages(),
    include_package_data=False,
    platforms="any",
    install_requires=[
        'coloredlogs>=15.0.1'
    ],
    python_requires='>=3.8',
)
