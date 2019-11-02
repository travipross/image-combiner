from setuptools import setup, find_packages

setup(
    name="beer_sign_creator",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "imageio",
        "numpy",
        "matplotlib"
    ],
    entry_points={
        "console_scripts": [
            'create-sign=beer_sign_creator.create_sign:main'
        ]
    }
)
