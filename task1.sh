#!/bin/bash
pyenv install 2.7.18 && pyenv install 3.7.10
mkdir py2 && mkdir py3
pyenv virtualenv 2.7.18 py2 && pyenv virtualenv 3.7.10 py3
cd py2 && pyenv local py2
cd ../py3 && pyenv local py3
