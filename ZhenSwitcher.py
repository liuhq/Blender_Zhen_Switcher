bl_info = {
    "name": "Blender Zhen Switcher",
    "description": "switch zh/en",
    "author": "QoQiyu",
    "version": (1, 0, 1),
    "blender": (3, 0, 0),
    "location": "",
    "warning": "",
    "category": "User",
    "doc_url": "https://github.com/qoqiyu/Blender_Zhen_Switcher#readme"
}

import bpy

class ZhenSwitcherPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    notTranslateTooltips: bpy.props.BoolProperty(
        name="do not translate tooltips: 不翻译工具提示",
        default=False,
    )

    def draw(self, context):
        self.layout.label(text="Something Settings: 一些设置...")
        self.layout.prop(self, "notTranslateTooltips")

class ZhenSwitcher(bpy.types.Operator):
    """Switch zh/en: 切换中英文"""
    bl_idname = 'wm.zhen_switcher'
    bl_label = 'Switch zh/en'
    bl_options = {'UNDO'}

    def execute(self, context):
        lang = context.preferences.view.language
        addonPrefs = context.preferences.addons[__name__].preferences

        if lang == 'en_US':
            context.preferences.view.language = 'zh_CN'
            context.preferences.view.use_translate_interface = True
            context.preferences.view.use_translate_new_dataname = False
            context.preferences.view.use_translate_tooltips = not(addonPrefs.notTranslateTooltips)
        else:
            context.preferences.view.language = 'en_US'

        return {'FINISHED'}


def drawSwitcherUI(self,context):
    self.layout.operator('wm.zhen_switcher', text='Zhen')

def register():
    bpy.utils.register_class(ZhenSwitcher)
    bpy.utils.register_class(ZhenSwitcherPreferences)
    # toggle comments to remove the button
    bpy.types.VIEW3D_HT_tool_header.append(drawSwitcherUI)

def unregister():
    bpy.utils.unregister_class(ZhenSwitcher)
    bpy.utils.unregister_class(ZhenSwitcherPreferences)
    # toggle comments to remove the button
    bpy.types.VIEW3D_HT_tool_header.remove(drawSwitcherUI)
