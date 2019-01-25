from setuptools import setup, find_packages

setup(
    name="profile-viewer",
    url="http://www.vrplumber.com/programming/profile_viewer/",
    download_url="http://www.vrplumber.com/programming/profile_viewer/",
    description="GUI Viewer for Python profiling runs",
    author="Mike C. Fletcher",
    author_email="mcfletch@vrplumber.com",
    install_requires=[
        'SquareMap3 >= 1.0.3',
        'wxPython',
    ],
    license="BSD",
    package_dir={
        'profile_viewer': 'profile_viewer',
    },
    packages=[
        'profile_viewer',
    ],
    options={
        'sdist': {
            'force_manifest': 1,
            'formats': ['gztar', 'zip'],
        },
    },
    zip_safe=False,
    entry_points={
        'gui_scripts': [
            'runsnake=profile_viewer.runsnake:main',
            'runsnakemem=profile_viewer.runsnake:meliaemain',
        ],
    },
    use_2to3=True,
    setup_requires=['setuptools_scm'],
    long_description_markdown_filename='README.md',
    classifiers=[
        """License :: OSI Approved :: BSD License""",
        """Programming Language :: Python""",
        """Topic :: Software Development :: Libraries :: Python Modules""",
        """Intended Audience :: Developers""",
    ],
    keywords='profile,gui,wxPython,squaremap',
    platforms=['Any'],
    install_package_data=True,
    use_scm_version=True)
