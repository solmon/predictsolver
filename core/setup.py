from setuptools import setup, find_packages

setup(
    name="predictsolver-core",
    version="0.1.0",
    packages=find_packages(),
    description="Core ML libraries for the predictsolver project",
    author="PredictSolver Team",
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "torch>=1.10.0",
    ],
    python_requires=">=3.8",
)
