
bl_info = {
    'name': 'XRay Engine Tools',
    'author': 'Vakhurin Sergey (igel)',
    'version': (0, 2, 5),
    'blender': (2, 7, 0),
    'category': 'Import-Export',
    'location': 'File > Import/Export',
    'description': 'Import/Export X-Ray Engine formats',
    'wiki_url': 'https://github.com/igelbox/blender-xray',
    'tracker_url': 'https://github.com/igelbox/blender-xray/issues',
    'warning': 'Under construction!'
    }

from .plugin import register, unregister
