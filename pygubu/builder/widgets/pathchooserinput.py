# encoding: utf8
from pygubu import BuilderObject, register_widget, register_property
from pygubu.widgets.pathchooserinput import PathChooserInput


class PathChooserInputBuilder(BuilderObject):
    class_ = PathChooserInput
    OPTIONS_CUSTOM = ('type', 'path', 'image', 'textvariable', 'state')
    properties = OPTIONS_CUSTOM
    virtual_events = ('<<PathChooserPathChanged>>',)
    
    def _code_set_property(self, targetid, pname, value, code_bag):
        if pname == 'type':
            code_bag[pname] = "'{0}'".format(value)
        else:
            super(PathChooserInputBuilder, self)._code_set_property(
                targetid, pname, value, code_bag)


register_widget('pygubu.builder.widgets.pathchooserinput', PathChooserInputBuilder,
                'PathChooserInput', ('ttk', 'Pygubu Widgets'))

props = {
    'type': {
        'editor': 'choice',
        'params': {
            'values': (PathChooserInput.FILE, PathChooserInput.DIR), 'state': 'readonly'},
        'default': PathChooserInput.FILE
        },
    'path': {
        'editor': 'entry'
        },
    'image': {
        'editor': 'imageentry'
        },
    'textvariable': {
        'editor': 'tkvarentry'
        },
    'state': {
        'editor': 'choice',
        'pygubu.builder.widgets.pathchooserinput': {
            'params': {
                'values': ('', 'normal', 'disabled', 'readonly'),
                'state': 'readonly'}},
        }
    }

for p in props:
    register_property(p, props[p])

