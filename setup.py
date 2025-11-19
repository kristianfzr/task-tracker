from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="task-tracker-cli",
    version="1.0.0",
    author="Kristian Kanchev",
    description="A CLI task tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kristianfzr/task-tracker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "task-tracker=task_tracker.cli:main",
        ],
    },
)