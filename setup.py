from setuptools import setup, find_packages

setup_args = dict(
    name='message_boxes',
    version='0.0.1',
    description='Create easy windows message boxes with python!',
    license='MIT',
    packages=find_packages(),
    author='Cy4',
    keywords=['Message', 'Boxes', 'MessageBoxes'],
    python_requires='>=3.6'
)

if __name__ == '__main__':
    setup(**setup_args)
