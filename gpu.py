import re
import bpy
scene = bpy.context.scene
scene.cycles.device = 'GPU'
prefs = bpy.context.preferences
prefs.addons['cycles'].preferences.get_devices()
cprefs = prefs.addons['cycles'].preferences

# Find GPU to set
for compute_device_type in ('OPENCL', 'CUDA', 'NONE'):
    try:
        cprefs.compute_device_type = compute_device_type
        break
    except TypeError:
        pass
# Activate All GPUs
for device in cprefs.devices:
    if not re.match('intel', device.name, re.I):
        device.use = True