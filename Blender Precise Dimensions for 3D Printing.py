bl_info = {
    "name": "Blender Precise Dimensions for 3D Printing",
    "author": "Paralhama",
    "version": (1, 2),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Item",
    "description": "Show precise dimensions in millimeters",
    "category": "3D View",
}

import bpy

def format_dimension(value):
    """Format value in millimeters without unnecessary zeros"""
    return f"{value:.4f}".rstrip('0').rstrip('.') + " mm"

class DimensionsPanel(bpy.types.Panel):
    """Creates a dimensions panel in the Sidebar"""
    bl_label = "Precise Dimensions"
    bl_idname = "OBJECT_PT_precise_dimensions"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        if obj:
            col = layout.column()
            col.label(text="X: " + format_dimension(obj.dimensions.x))
            col.label(text="Y: " + format_dimension(obj.dimensions.y))
            col.label(text="Z: " + format_dimension(obj.dimensions.z))
        else:
            layout.label(text="No objects selected")

def register():
    bpy.utils.register_class(DimensionsPanel)

def unregister():
    bpy.utils.unregister_class(DimensionsPanel)

if __name__ == "__main__":
    register()