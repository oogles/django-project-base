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


dev_requirements.txt
====================

This is a pip requirements file that provides a base list standard requirements *for development*. It includes:

* ``Django``
* ``django-extensions``, for helpful development tools such as ``shell_plus``
* ``sphinx``, for building documentation
* ``sphinx_rtd_theme``, so documentation can be previewed in the theme it would use on readthedocs.org (to enable the theme, see ??? below)
* ``flake8`` and ``isort``, for code linting
* ``tox``, for testing under different versions of Django, Python, etc
* ``coverage``, for analysing code coverage by the test suite
