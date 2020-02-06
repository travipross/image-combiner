#!/bin/bash

# Check for environment variable
echo "Checking for \$VENV_IMAGE_COMBINER environment variable..."
if [ -z $VENV_IMAGE_COMBINER ]; then
    echo "Not found. Creating VENV_IMAGE_COMBINER environment variable"
    echo "export VENV_IMAGE_COMBINER=$HOME/git/virtualenvs/imagecombiner" >> $HOME/.profile
    source $HOME/.profile
fi
echo -e "---------------------------\n\n"


# If virtual environment doesn't exist, create it
echo "Checking for virtual environment 'imagecombiner'..."
if [ ! -d $VENV_IMAGE_COMBINER ]; then
    echo "virtual environment not found at $VENV_IMAGE_COMBINER ... Creating now."
    virtualenv -p python3 $VENV_IMAGE_COMBINER
fi
echo -e "---------------------------\n\n"

# Activating environment and installing package
echo "Installing  image_combiner"
source $VENV_IMAGE_COMBINER/bin/activate
pip install -e .
echo -e "---------------------------\n\n"


# Copying executables to /usr/local/bin
echo "Copying executable to make 'combine_images' command available anywhere for $USER"
sudo install resources/combine_images /usr/local/bin
echo "Installation complete. You may need to log out and log back in for changes to take effect"
