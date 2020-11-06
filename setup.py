from setuptools import setup, find_packages

setup_args = dict(
    name='message_boxes',
    version='0.2.0',
    description='Create easy windows message boxes with python!',
    license='MIT',
    packages=find_packages(),
    author='Cy4',
    keywords=['Message', 'Boxes', 'MessageBoxes'],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]
)

if __name__ == '__main__':
    setup(**setup_args)
