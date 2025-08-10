#!/usr/bin/env bash

apt-get install -y python python-pip python-dev python3-pip

pip3 install --user jsonschema

apt-get install make
apt-get install -y g++
apt-get install -y jsoncpp

apt-get install -y libjsoncpp-dev

apt-get install -y clang-3.9  
ln -s /usr/bin/clang++-3.9 /usr/bin/clang++
