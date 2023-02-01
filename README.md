# Blender_Zhen_Switcher

blender Zhen 中英一键切换脚本

## 安装 - installation

1. 下载脚本文件 `ZhenSwitcher.py` :arrow_double_down: [release]

2. 安装脚本：Edit(编辑) > Preferences(偏好设置) > Add-ons(插件) > Install...(安装...)

![step_01]

![step_02]

找到脚本下载位置，选择脚本 `ZhenSwitcher.py`，点击 install Add-on(安装插件)

![step_03]

## 使用 - usage

点击 `Header (标题栏)` 最右边的 `Zhen` 按钮即可随时切换中/英文界面与工具提示（数据相关信息不会切换到中文，请放心）

![usage]

:anchor: 设置快捷键有两种方式：
1. 右键单击按钮，选择 `Assign Shortcut(指定快捷键)`，即可绑定快捷键

![add_shortcut_1]

2. 进入偏好设置中，Edit(编辑) > Preferences(偏好设置) > Keymap(键位映射) > Window(窗口)，按 `Add New` 添加新快捷键，在输入框 `Identifier` 输入 `wm.zhen_switcher`，并指定快捷键即可

![add_shortcut_2]

> 另外，在插件设置中可以选择是否翻译工具提示

## 无按钮/纯快捷键设置 - only shortcut

打开脚本文件 `ZhenSwitcher.py`, 将下述代码注释掉即可（在对应代码行前面输入 `#` 符号）

```python
# 第55行:
    # toggle comments to remove the button
    bpy.types.VIEW3D_HT_tool_header.append(drawSwitcherUI)

# 第61行:
    # toggle comments to remove the button
    bpy.types.VIEW3D_HT_tool_header.remove(drawSwitcherUI)
```

> P.S. 个人学艺不精，大佬如有直接在设置中去除按钮的方法，还请告知或直接PR，谢谢啦！

[release]: https://github.com/qoqiyu/Blender_Zhen_Switcher/releases
[step_01]: ./img/step_01.png "step 1"
[step_02]: ./img/step_02.png "step 2"
[step_03]: ./img/step_03.png "step 3"
[usage]: ./img/usage.png "usage"
[add_shortcut_1]: ./img/add_shortcut_1.png "add shortcut one"
[add_shortcut_2]: ./img/add_shortcut_2.png "add shortcut two"
