#! /bin/bash

xcode-select --install
xcode-select -p

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew install ta-lib
brew install snappy

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

conda create -y -n qtc python=3.6 anaconda
source activate qtc

pip install pip==9.0.1
pip install -r requirements.txt
pip uninstall -y gevent

rqalpha update_bundle