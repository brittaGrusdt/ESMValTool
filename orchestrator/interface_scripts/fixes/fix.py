import importlib


class Fix(object):
    """
    Base class for fixes
    """
    def __init__(self, cube):
        self.cube = cube

    def fix_metadata(self):
        pass

    def fix_data(self):
        pass

    @staticmethod
    def get_fix(project, model, variable):
        project = project.replace('-', '_')
        model = model.replace('-', '_')
        variable = variable.replace('-', '_')
        try:
            fix = importlib.import_module('orchestrator.interface_scripts.fixes.{0}.{1}'.format(project, model))
            fix = getattr(fix, variable)
        except (AttributeError, ImportError):
            fix = None
        return fix
