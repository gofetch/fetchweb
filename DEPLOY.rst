Initial Setup
=============

set up ubuntu 10.04 x86_64 server on vps

add fetch as user with home directory::

  sudo useradd -d /home/fetch -m fetch
  sudo passwd fetch
  sudo adduser fetch sudo

now set bash to be default shell for fetch::

  chsh -s `which bash` fetch

update aptitude::

  sudo apt-get update

Get Aptitude Dependencies Resolved For Fetch
============================================

install build-essential and python distribute::

  sudo apt-get install build-essential python-dev python-pip python-distribute
  sudo pip install virtualenv
  sudo pip install virtualenvwrapper

install nginx::

  sudo apt-get install nginx

install transmission and transmissionrpc-python::

  sudo apt-get install transmission-cli transmission-common
  sudo pip install transmissionrpc


Python Environments with virtualenv/virtualenvwrapper
=====================================================

create directory which will hold all your virtualenvs::

  mkdir ~/envs

Now, make the virtualenvwrapper available to your session::

  export WORKON_HOME=~/envs
  source $(which virtualenvwrapper.sh)

Make new project for fetchweb::

  mkvirtualenv fetchweb

change current virtualenv to fetchweb::

  workon fetchweb

to quick from the current virtualenv::

  deactivate




