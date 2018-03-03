===================
django-project-base
===================

Sample config/setup files for a generic Django project. Most of these files can be dropped into new projects as-is, though some do require per-project configuration. See the description of each included file below for more info.


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

This is a pip requirements file that provides a base list of standard requirements *for development*. It includes:

* ``Django``
* ``django-extensions``, for helpful development tools such as ``shell_plus``
* ``sphinx``, for building documentation
* ``sphinx_rtd_theme``, so documentation can be previewed in the theme it would use on readthedocs.org (to enable the theme, see ??? below)
* ``flake8`` and ``isort``, for code linting
* ``tox``, for testing under different versions of Django, Python, etc
* ``coverage``, for analysing code coverage by the test suite

Any additional *development* dependencies for the project can be added to this file.


test_settings.py
================

**This file will require modification**

This is a bare-minimum settings file required for "starting" Django, such as during tests, or building documentation that involves *autodoc* (more details below). It is useful when creating Django apps, and is **not necessary for full Django projects** - the project's actual ``settings.py`` file should be used in that case.

The ``INSTALLED_APPS`` setting needs to be modified to include the Django app being developed. It may also need to include other apps based on dependencies and/or specific Django internals invoked.

The ``ROOT_URLCONF`` setting may need to be configured if tests perform any url resolving. This is necessary, for example, when using the test client or ``reverse()``. It can also occur when using the ``RequestFactory``, and not even routing anything through the URLconf. The file referenced by the setting need not actually contain any URLs, though it does need to define ``urlpatterns``.

As with ``INSTALLED_APPS``, other settings may need to be modified or added, depending on which Django internals are required.


manage.py
=========

Another file that is only required for Django apps, **not for full Django projects**. Again, the real ``manage.py`` should be used there instead. For app development, this file gives access to the regular ``manage.py`` commands using the ``test_settings.py`` file.
