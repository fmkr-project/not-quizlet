import importlib
"""Gets the blueprint with the desired API version"""
def get_api_blueprint(version):
    try:
        # Dynamically import the module based on the version
        print(version)
        version_module = importlib.import_module(f"{version}", package="backend.app.api")
        vi_blueprint = getattr(version_module, f"{version}_blueprint")
        return vi_blueprint  #Get the variable {version}_blueprint
    except ImportError:
        raise ValueError(f"Invalid API version: {version}")
get_api_blueprint("v1")