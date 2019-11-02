from setuptools import setup, find_packages

setup(
    name="image_combiner",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "imageio",
        "numpy",
        "matplotlib"
    ],
    entry_points={
        "console_scripts": [
            'combine-images=image_combiner.combine_images:main'
        ]
    }
)
