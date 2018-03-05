===================
django-project-base
===================

Sample config/setup files for a generic Django development project. Most of these files can be dropped into new projects as-is, though some do require per-project configuration. See the description of each included file below for more info.

Not all of these files will be relevant to all projects. E.g. when developing a full Django project (as opposed to a distributable Django app), the ``setup.py`` and associated files will most likely not be necessary, nor will ``test_settings.py`` and ``manage.py``.


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

The ``INSTALLED_APPS`` setting needs to be modified to include the Django app being developed. It may also need to include other apps based on dependencies and/or specific Django internals invoked (e.g. ``contrib.auth``).

The ``ROOT_URLCONF`` setting may need to be configured if tests perform any url resolving. This is necessary, for example, when using the test client or ``reverse()``. It can also occur when using the ``RequestFactory``, and not even routing anything through the URLconf. The file referenced by the setting need not actually contain any URLs, though it does need to define ``urlpatterns``.

As with ``INSTALLED_APPS``, other settings may need to be modified or added, depending on which Django internals are required.


manage.py
=========

Another file that is only required for Django apps, **not for full Django projects**. Again, the real ``manage.py`` should be used there instead. For app development, this file gives access to the regular ``manage.py`` commands using the ``test_settings.py`` file.


setup.cfg
=========

**This file will require modification**

This file contains configuration options for ``flake8``, ``isort``, and ``coverage.py``, when those tools are run from the project directory.

The ``[coverage:run]`` section needs modifying to specify the subdirectory to include in the test coverage analysis. E.g. the subdirectory containing the Django app being developed. It also contains an omission for the ``env.py`` file written by the ``vagrant-django`` provisioning process. The path to this file also needs modifying, but can be removed entirely if not using the ``vagrant-django`` provisioning process.

For more configuration options, see:

* ``flake8``: http://flake8.pycqa.org/en/latest/user/options.html
* ``isort``: https://github.com/timothycrosley/isort/wiki/isort-Settings
* ``coverage.py``: http://coverage.readthedocs.io/en/coverage-4.5.1/config.html


tox.coverage.py
===============

This script is designed to be called from within a ``tox`` environment, after generating test coverage data with ``coverage.py``, to generate a report on that data based on the environment in which the test suite was run. If run locally, it uses ``coverage.py`` to print a basic report, skipping files that had complete coverage, and generate a fully detailed HTML report for later viewing in a browser. If run in a Travis CI environment, it uses the ``coveralls`` command from the `coveralls-python <http://coveralls-python.readthedocs.io/en/latest/>`_ library to submit the data to `coveralls.io <https://coveralls.io/>`_.


tox.ini
=======

**This file will require modification**

This configuration file for ``tox`` sets up multiple environments to run:

* the full test suite and coverage measurement (both statement coverage and `branch coverage <http://coverage.readthedocs.io/en/latest/branch.html>`_)
* ``flake8``
* ``isort`` (in ``--check-only`` mode, no changes are made)

It is configured for use on Travis CI, and calls the above-mentioned ``tox.coverage.py`` script after running the test suite, in order to report the coverage results according to the environment (local or Travis).

It includes the ``coverage`` and ``coveralls`` dependencies. Other dependencies may be required.

It also includes an example setup for testing under multiple versions of Django across multiple versions of Python. The specific versions should be modified to suit the project. Note that the Python versions included in ``tox.ini`` should also be included in ``.travis.yml`` (see below).


.travis.yml
===========

**This file will require modification**

A very simple configuration file for Travis CI. It installs `tox-travis <https://tox-travis.readthedocs.io/en/stable/>`_ which, as it advertises, enables seamless integration of ``tox`` into Travis CI. Then it just runs ``tox``.

The listed versions of Python just need to be kept in line with those listed in ``tox.ini``.


docs/_ext/djangodocs.py
=======================

This provides some Sphinx plugins for Django documentation, specifically ``:setting:``, ``:ttag:``, and ``:tfilter:`` roles. It needs to be enabled by editing the Sphinx ``conf.py`` file, see below.


docs/conf.py
============

**This file may require modification**

This file is not included, it must be generated by Sphinx, and then modified.

To generate the file, enter the ``docs/`` directory and run the ``sphinx-quickstart`` command.

.. code-block:: bash

    cd docs
    sphinx-quickstart

This will start a series of prompts. For the most part, the defaults are fine.

Aside from regularly updating the version and copyright year, some other modifications to this file can be useful. The subsequent sections explain each one.

Update paths for autodoc and plugins
------------------------------------

If the documentation makes use of *autodoc*, the Python path needs to be updated to include the project source directory. Likewise, if using the included Django documentation plugins, the path needs to be updated to be able to find ``djangodocs.py``.

An example will be given. Replace it with the new paths. In both cases, ``os.path.abspath()`` is used to build an absolute path from one that is relative to the ``docs/`` directory.

.. code-block:: python

    # Replace this:

    # import os
    # import sys
    # sys.path.insert(0, os.path.abspath('.'))

    # With this:

    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "_ext")))

Setup Django
------------

Again, if the documentation makes use of *autodoc*, and the project code imports certain parts of the Django framework (most parts, really), then Django may need to be set up first - something ``manage.py`` would typically handle.

A settings module is required. The included ``test_settings.py``, or a full Django project's real ``settings.py``, can be used here. Note, however, that *autodoc* doesn't *execute* any code, merely *imports* it, so a bare-minimum settings file is all that is necessary. A separate settings file, e.g. ``doc_settings.py``, could be used for this purpose if the full settings file is not suitable.

This segment should be included somewhere near the top of ``conf.py``. If necessary, replace ``test_settings`` with the name of the appropriate settings file to use.

.. code-block:: python

    import django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
    django.setup()

In order for the ``django`` package (and any other dependencies the project may have) to be available when the documentation is built on readthedocs.org, it needs to know about and be able to install those dependencies. They should be listed in ``setup.py`` (see below) and the RTD project should be configured to install it inside a virtualenv (Admin > Advanced Settings > Install Project).

In addition, if using Django 2.0 or later, readthedocs.org needs to be instructed to build the documentation under Python 3. This is done in the ``.readthedocs.yml`` file (see below).

Enable useful extensions
------------------------

Specify which extensions Sphinx should use when building the documentation. This may be partially completed already, depending on how the ``sphinx-quickstart`` prompts were answered. Some useful options here are:

* `autodoc <http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_: Enables including in-code docstrings in the documentation via directives such as ``.. automodule::``, ``.. autoclass::``, ``.. autofunction::``, etc.
* `viewcode <http://www.sphinx-doc.org/en/stable/ext/viewcode.html>`_: Enables including separate documentation pages containing source code, with links from the main documentation, when using directives such as ``.. class::``, ``.. function::``, etc.
* djangodocs: The included extension providing ``:setting:``, ``:ttag:``, and ``:tfilter:`` roles.

.. code-block:: python

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'djangodocs'
    ]

Enable the RTD theme
--------------------

Enable the theme used by default by readthedocs.org, allowing the documentation to be viewed locally in the same theme. It only needs configuring when building the documentation locally, as it is the default on RTD, so an environment variable is used to detect which environment the build is taking place in.

.. code-block:: python

    # Replace this:

    html_theme = '...'

    # With this:

    # Only import and set the RTD theme if we're building docs locally. Otherwise,
    # readthedocs.org uses their theme by default, so no need to specify it.
    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
    if not on_rtd:
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

Writing docs
------------

To start writing docs, edit ``index.rst``, and link to additional files from there. To build the docs as HTML for viewing in the browser as they would appear on readthedocs.org, run ``make html`` from the ``docs/`` directory.


.readthedocs.yml
================

Config file for readthedocs.org. Used exclusively to configure documentation to be built under Python 3 - required if installing Django >= 2.0 as part of building the docs (e.g. when using *autodoc*, as noted in the ``conf.py`` notes above).


LICENSE
=======

**This file will require modification**

This file holds the license under which the project is released.

The included license is the `MIT license <https://tldrlegal.com/license/mit-license>`_, being that with which ``django-project-base`` itself is licensed. It should be changed as necessary.

Even if not changing the license itself, the copyright year and copyright holder should be updated accordingly.


MANIFEST.in
===========

This file is the `manifest template <https://docs.python.org/2/distutils/sourcedist.html#the-manifest-in-template>`_ used by ``distutils``/``setuptools`` when creating a source distribution. This is the list of files to include in the distribution (in addition to the defaults).

This is a very simple manifest, simply including the above-mentioned ``LICENSE`` file, and the ``README.rst`` file.


setup.py
========

**This file will require modification**

This file is the setup script for building, distributing, and installing the project as a Python module. The included file uses the ``setuptools`` `extension of <http://setuptools.readthedocs.io/en/latest/setuptools.html>`_ ``distutils``, as it makes it easier to define the package setup.

It primarily consists of a call to the imported ``setup()`` function, the arguments to which define the attributes of the project necessary to build, distribute, and install it. Most of the arguments are project-specific and require custom configuration, but a few things are included that can be common across projects:

* The ``version`` argument is set by reading the value of the ``__version__`` module-level variable included in the ``__init__.py`` file of the source directory. This helps reduce the number of places the version number needs to be modified when it is updated. It assumes a few things:

    * There is a subdirectory under the main project directory (in which these config files reside) that contains the project's source code. The path to this subdirectory should be set using the ``source_dir`` variable at the top of ``setup.py``.
    * There is a ``__version__`` module-level variable in that subdirectory's ``__init__.py`` file that defines a sane version string, such as ``'2.8'``, ``'1.6.2'``, ``'0.4.6dev1'``, etc.

* The ``long_description`` argument is populated from the ``README.rst`` file. Again, this helps avoid repetition, and can provide a more useful extended description of the project than could easily be written in ``setup.py`` itself.

* The ``packages`` argument is set using the ``find_packages()`` `helper function <http://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages>`_, which locates all relevant Python packages to include in the distribution. It excludes the ``docs/`` directory, which is not useful to be included.

When properly configured, ``setup.py`` allows a distribution for the project to be built and uploaded to PyPI using:

.. code-block:: bash

    # Build
    python setup.py sdist

    # Upload
    python setup.py upload

    # Together
    python setup.py sdist upload

Uploading to PyPI requires suitable PyPI credentials be provided. Due to a bug in ``distutils`` `discussed here <https://github.com/pypa/setuptools/issues/941>`_, the password may be prompted for without the username. In order for the username to be correctly supplied, it must be added to a ``.pypirc`` file located in the logged-in user's home directory. This ``~/.pypirc`` file should look like:

.. code-block:: ini

    [distutils]
    index-servers =
        pypi

    [pypi]
    username: <username>
    password:

The username should be populated accordingly. The password can be left blank to allow the ``setup.py upload`` command to prompt for it.


README.rst
==========

**This file will require modification**

Hopefully obvious, this file should be updated with the project's own readme.
