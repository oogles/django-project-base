===================
django-project-base
===================

Sample config/setup files for a generic Django project.


.gitignore
==========

A pretty basic ``.gitignore`` file that excludes:

* compiled Python files
* the ``node_modules`` directory
* environment-specific files that should not be committed (including some specific to projects using `vagrant-django <https://github.com/oogles/vagrant-django>`_)
* temporary/build directories for Vagrant, Sphinx documentation, tox, coverage.py and distutils


.ignore
=======

A simple ignore file for tools such as ``ag`` (The Silver Searcher). See https://geoff.greer.fm/2016/09/26/ignore/.

This one ignores:

* the ``Vagrantfile``
* the ``README`` file
* the ``docs/`` directory
* all ``migrations/`` directories
