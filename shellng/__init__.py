from management.commands.shellng import shell_loaded


def load_models(sender, imported_objects, **kwargs):
    # Load the django models.
    from django.db.models.loading import get_models
    loaded_models = get_models()
        
    for model in loaded_models:
        imported_objects[model.__name__] = model
       
shell_loaded.connect(load_models, dispatch_uid='load_models')
