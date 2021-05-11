from setuptools import find_packages
from setuptools import setup


setup(
    name='pre-commit-terraform-lock',
    description='Pre-commit hooks for check-tf-lock-file-with-zh-entries',
    url='https://github.com/davidcaste/pre-commit-terraform-lock',
    version_format='{tag}+{gitsha}',

    author='Contributors',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'setuptools-git-version',
    ],
    entry_points={
        'console_scripts': [
            'check_tf_lock_file_without_zh_entries = pre_commit_hooks.check_tf_lock_file_without_zh_entries:main',
        ],
    },
)
