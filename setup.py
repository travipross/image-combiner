from setuptools import setup, find_packages

setup(
    name="image_combiner",
    packages=find_packages(),
    install_requires=["opencv-python", "imageio", "numpy", "matplotlib", "gphotospy"],
    entry_points={
        "console_scripts": [
            "combine-images=image_combiner.combine_images:main",
            "set-menu=photo_library.cmd.upload:set_menu",
            "set-home=photo_library.cmd.upload:set_home",
            "list-menus=photo_library.cmd.utils:list_archived_menus",
        ]
    },
)
