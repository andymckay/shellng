import code
import datetime
from optparse import make_option
import os

from django.core.management.base import NoArgsCommand
import django.dispatch

shell_loaded = django.dispatch.Signal(providing_args=['imported_objects'])


class Command(NoArgsCommand):
    help = "Runs a Python interactive interpreter."

    requires_model_validation = False

    def handle_noargs(self, **options):
	# Connect to this event to do whatever you'd like.
	imported_objects = {}
        shell_loaded.send(sender=self, imported_objects=imported_objects)

        try: # Try activating rlcompleter, because it's handy.
            import readline
        except ImportError:
            pass
        else:
            # We don't have to wrap the following import in a 'try', because
            # we already know 'readline' was imported successfully.
            import rlcompleter
            readline.set_completer(rlcompleter.Completer(imported_objects).complete)
            readline.parse_and_bind("tab:complete")

        # We want to honor both $PYTHONSTARTUP and .pythonrc.py, so follow system
        # conventions and get $PYTHONSTARTUP first then import user.
        pythonrc = os.environ.get("PYTHONSTARTUP") 
        if pythonrc and os.path.isfile(pythonrc): 
            try: 
                execfile(pythonrc) 
            except NameError: 
                pass
        	
	# This will import .pythonrc.py as a side-effect
	import user
	code.interact(local=imported_objects)
