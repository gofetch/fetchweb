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

Nginx
=====

dependencies::

  sudo apt-get install libpcre3 libpcre3-dev libpcrecpp0 \
      libssl-dev zlib1g-dev openssl apache2-utils libssl-dev

get nginx source::

  wget http://nginx.org/download/nginx-1.2.0.tar.gz
  tar -xvf nginx-1.2.0.tar.gz

get mod_zip module for nginx::

  wget  http://mod-zip.googlecode.com/files/mod_zip-1.1.6.tar.gz
  tar -xvf mod_zip-1.1.6.tar.gz

now build nginx with modules::

  ./configure --with-http_mp4_module  \
      --with-http_ssl_module --with-http_dav_module --add-module=$HOME/sources/mod_zip-1.1.6 \
      --prefix=$HOME/nginx


Python Environments with virtualenv/virtualenvwrapper
=====================================================

install build-essential and python distribute::

  sudo apt-get install build-essential python-dev python-pip python-distribute
  sudo pip install virtualenv
  sudo pip install virtualenvwrapper

create directory which will hold all your virtualenvs::

  mkdir ~/envs

Now, make the virtualenvwrapper available to your session::

  export WORKON_HOME=~/envs
  source $(which virtualenvwrapper.sh)

Make new project for fetchweb::

  mkvirtualenv fetchweb

change current virtualenv to fetchweb::

  workon fetchweb

to quit from the current virtualenv::

  deactivate

Session Management
==================
install tmux and screen::

  sudo apt-get install tmux screen

RTorrent
========

install rtorrent from repo::

  sudo apt-get update
  sudo apt-get -y install python-software-properties
  sudo add-apt-repository ppa:patricksissons/rtorrent
  sudo apt-get update
  sudo apt-get install curl unrar-free rtorrent

set up config for it with help from rtorrent.rc in this package::

  mv rtorrent.rc $HOME/.rtorrent.rc

Flask
=====

Get flask::

  pip install flask

Mocking Framework
=================

We use unittest and pymox::

  pip install mox







