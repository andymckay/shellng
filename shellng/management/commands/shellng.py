import code
import os

from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.db.models.loading import get_models
from django.utils.importlib import import_module


class Command(NoArgsCommand):
    help = "Runs a Python interactive interpreter."

    requires_model_validation = False

    def import_models(self, imported_objects):
        loaded_models = get_models()

        for model in loaded_models:
            imported_objects[model.__name__] = model


    def handle_noargs(self, **options):
        # Connect to this event to do whatever you'd like.
        imported_objects = {}
        self.import_models(imported_objects)
        for startup in getattr(settings, 'SHELLNG_METHODS', ''):
            import_module(startup).shellng(imported_objects)

        try:
            # Try activating rlcompleter, because it's handy.
            import readline
        except ImportError:
            pass
        else:
            # We don't have to wrap the following import in a 'try', because
            # we already know 'readline' was imported successfully.
            import rlcompleter
            readline.set_completer(rlcompleter.Completer(imported_objects)
                                              .complete)
            readline.parse_and_bind("tab:complete")

        # We want to honor both $PYTHONSTARTUP and .pythonrc.py, so follow
        # system conventions and get $PYTHONSTARTUP first then import user.
        pythonrc = os.environ.get("PYTHONSTARTUP")
        if pythonrc and os.path.isfile(pythonrc):
            try:
                execfile(pythonrc)
            except NameError:
                pass

        # This will import .pythonrc.py as a side-effect
        import user
        code.interact(local=imported_objects)
