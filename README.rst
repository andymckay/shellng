django-shellng
=================

A management command to start a shell and auto-import all models. Unlike django command extensions shell_plus it doesn't print out a load of gunk to the shell. Provides a mechanism so that you can add in extra imports that are specific to your project.

Install::

    $ pip install django-shellng

Add into installed apps::

    INSTALLED_APPS += ('shellng',)

Usage::

    $ ./manage.py shellng

To import more things add a file containing a method `shellng` and assign that
in settings. For example, make a file in the root of your Django project (or
somewhere importable) called::

    shellng_local.py

In it, place the following::

    def shellng(imported_objects):
        modules = ('urllib',)  # This will add in urllib.
        for mod in modules:
            imported_objects[mod] = __import__(mod)

`imported_objects` is a dictionary of all modules to be imported. You can add
or remove to it as you want in the methods. Finally add in to `settings.py`::

    SHELLNG_METHODS = ('shellng_local',)

