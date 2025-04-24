from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1.0",
    description="A package for detecting emotions in text using Watson NLP.",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests"
    ],
    python_requires=">=3.6",
)
