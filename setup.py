from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="superagi_client",
    version="0.0.1",
    packages=find_packages(exclude=["tests*"]),
    url="https://app.superagi.com",
    license="MIT",
    author="superagi",
    author_email="mukunda@superagi.com",
    description="Python package for Superagi",
    install_requires=["pydantic==1.10.8", "requests==2.31.0", "pytest==7.3.2"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
