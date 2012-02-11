django-shellng
=================

A management command to start a shell and auto-import all models. Unlike django command extensions shell_plus it doesn't print out a load of gunk to the shell. Provides a signal so that you can add in extra imports that are specific to your project.

Usage::

    $ ./manage.py shellng

Using the signal to add in urllib::

    from shellng import shell_loaded

    def load_extra(sender, imported_objects, **kwargs):
        imported_objects['urllib'] = __import__('urllib')

    shell_loaded.connect(load, dispatch_uid='load_extra')

`imported_objects` is a dictionary of all modules to be imported. You can add or remove to it as you want in the signals. The signal needs to be in a place that will be imported before the command is run. The simplest place to connect the signal is in `settings.py`.
