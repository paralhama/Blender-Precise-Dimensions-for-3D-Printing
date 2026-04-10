bl_info = {
    "name": "Precise Dimensions",
    "author": "Paralhama",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Item",
    "description": "Mostra dimensões precisas em mm",
    "category": "3D View",
}

import bpy


def format_dimension(value_meters):
    """Converte metros para mm e formata sem zeros desnecessários"""
    value_mm = value_meters * 1000
    return f"{value_mm:.4f}".rstrip('0').rstrip('.') + " mm"


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
            layout.label(text="Nenhum objeto selecionado")


def register():
    bpy.utils.register_class(DimensionsPanel)


def unregister():
    bpy.utils.unregister_class(DimensionsPanel)


if __name__ == "__main__":
    register()