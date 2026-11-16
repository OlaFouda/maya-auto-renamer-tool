""""
Tool Description: Auto Renaming Tool For Maya
Version: 1.0
Date: 2026-01-20
"""
import maya.cmds as cmds

from Renaming_Tool.utils import methods
import importlib


gui_colors = {"yellow": (1, 1, 0),
              "dark_green": (0.35, 0.43, 0.41),
              "red": (0.33, 0.15, 0.16),
              "white_blue": (0.2, 0.7, 0.9),
              "blue": (0.2, 0.6, 0.7),
              "orange": (0.9, 0.5, 0.2),
              "white_orange": (1, 0.7, 0.5),
              "pink": (0.7, 0.5, 0.5),
              "black": (0.1, 0.1, 0.1),
              "cyan": (0, 1, 1),
              "blue_grey": (0.28, 0.37, 0.41),
              "beige": (0.99, 0.79, 0.63)
              }

importlib.reload(methods)


Tool_Version = "1.0"
def connect_check_to_field(check_name, field_name):
    check_status = cmds.checkBox(check_name, query=True, value=True)

    field_status = not check_status

    cmds.textField(field_name, edit=True, enable=field_status)


def auto_renaming_gui():
    if cmds.window("AutoRename", exists=True):
        cmds.deleteUI("AutoRename")
    rename_window = cmds.window("AutoRename", title="Renaming Tool", w=300, h=300)


    #___________ MainLayout ______________


    main_layout = cmds.columnLayout("MainLayout", adjustableColumn=True, columnAlign="center", bgc =gui_colors["red"])
    cmds.separator(height=10, style="in")
    cmds.text(f"Renaming Tool -- Version: {Tool_Version}", align="center", font="boldLabelFont")
    cmds.separator(height=10, style="in")


    #______________ apply on layout ________________

    cmds.rowLayout("apply_on_layout", numberOfColumns=2, adjustableColumn=True)
    cmds.columnLayout("apply_on_col")
    cmds.optionMenu("apply_on", label="Apply On:", w=213, h=20, ebg=True)
    cmds.setParent("..")
    cmds.menuItem(label="Selected")
    cmds.menuItem(label="Hierarchy")
    cmds.menuItem(label="All")
    cmds.setParent("..")
    cmds.separator(height=10, style="in")


    #____________ search and replace Layout__________

    cmds.frameLayout(label="Search/Replace",
                     backgroundColor=gui_colors["dark_green"],
                     marginWidth=10,
                     collapsable=True)
    cmds.rowLayout("search_replace_layout", numberOfColumns=2, adjustableColumn=True)
    cmds.columnLayout("search_replace_col")
    cmds.rowLayout("search_row", numberOfColumns=2)
    cmds.text(label="Search: ", font = "boldLabelFont", h=20, w=40, align="left")
    cmds.textField("SearchFor", w=160, placeholderText="Add What you Search For!", h=20, bgc=gui_colors["blue_grey"])
    cmds.setParent("..")

    cmds.rowLayout("replace_row", numberOfColumns=2)
    cmds.text(label="Replace: ", font="boldLabelFont", h=20, w=40, align="left")
    cmds.textField("ReplaceWith", w=160, placeholderText="Add The Replacement!", h=20, bgc=gui_colors["blue_grey"])
    cmds.setParent("..")

    cmds.rowLayout("SR_button_row", numberOfColumns=1)
    cmds.button(label="Search/Replace", command=lambda x: methods.search_replace(), h=30, w=200, bgc=gui_colors["beige"], align="center")

    cmds.setParent(main_layout)
    cmds.separator(height=10, style="in")


    #_____________ prefix Layout ____________

    cmds.frameLayout(label="Prefix",
                     backgroundColor=gui_colors["dark_green"],
                     marginWidth=10,
                     collapsable=True)
    cmds.rowLayout("prefix_main_layout", numberOfColumns=2, adjustableColumn=True)
    cmds.columnLayout("prefix_col")
    cmds.rowLayout("prefix_row", numberOfColumns=2)
    cmds.text(label="Prefix: ", w=40, font="boldLabelFont", h=20, align="left")
    cmds.textField("Prefix", w=160, placeholderText="Add The Prefix!", h=20, bgc=gui_colors["blue_grey"])
    cmds.setParent("..")

    cmds.checkBox("PositionPrefix", label="Prefix By Position", h=20,
                  changeCommand=lambda x: connect_check_to_field("PositionPrefix", "Prefix"))
    cmds.setParent("..")
    cmds.setParent("..")

    cmds.rowLayout("pre_button_row", numberOfColumns=1)
    cmds.button(label="Add Prefix!", command=lambda x: methods.add_prefix(), h=30, w=200, bgc=gui_colors["beige"])
    cmds.setParent(main_layout)
    cmds.separator(height=10, style="in")


    #______________ Suffix Layout ____________

    cmds.frameLayout(label="Suffix",
                     backgroundColor=gui_colors["dark_green"],
                     marginWidth=10,
                     collapsable=True)
    cmds.rowLayout("suffix_main_layout", numberOfColumns=2, adjustableColumn=True)
    cmds.columnLayout("suffix_col")
    cmds.rowLayout("suffix_row", numberOfColumns=2)
    cmds.text(label="Suffix: ", w=40, font="boldLabelFont", h=20, align="left")
    cmds.textField("Suffix", w=160, placeholderText="Add The Suffix!", h=20, bgc=gui_colors["blue_grey"])
    cmds.setParent("..")

    cmds.checkBox("TypeSuffix", label="Suffix By Type", h=20,
                  changeCommand=lambda x: connect_check_to_field("TypeSuffix", "Suffix"))
    cmds.setParent("..")
    cmds.setParent("..")
    cmds.rowLayout("Suf_button_row", numberOfColumns=1)
    cmds.button(label="Add Suffix!", command=lambda x: methods.add_suffix(), h=30, w=200, bgc=gui_colors["beige"])
    cmds.setParent(main_layout)
    cmds.separator(height=10, style="in")


    #___________ Rename Layout ____________
    cmds.frameLayout(label="Rename",
                     backgroundColor=gui_colors["dark_green"],
                     marginWidth=10,
                     collapsable=True)
    cmds.rowLayout("rename_main_layout", numberOfColumns=2, adjustableColumn=True)
    cmds.columnLayout("rename_col")
    cmds.rowLayout("rename_row", numberOfColumns=2)
    cmds.text(label="Name: ", w=40, font="boldLabelFont", h=20, align="left")
    cmds.textField("Name", w=150, placeholderText="Add The New Name!", h=20, bgc=gui_colors["blue_grey"])
    cmds.setParent("..")

    cmds.rowLayout("index_row", numberOfColumns=2)
    cmds.text(label="Index: ", w=40, font="boldLabelFont", h=20, align="left")
    cmds.intField("Index", w=150, h=20, bgc=gui_colors["blue_grey"])
    cmds.setParent("..")
    cmds.setParent("..")
    cmds.setParent("..")

    cmds.rowLayout("rename_button_row", numberOfColumns=1)
    cmds.button(label="Rename!", command=lambda x: methods.rename_with_offset(), h=30, w=200, bgc=gui_colors["beige"])
    cmds.setParent(main_layout)

    cmds.separator(height=10, style="in")


    #________________ Skeleton Layout _____________
    cmds.frameLayout(label="Define Skeleton",
                     backgroundColor=gui_colors["dark_green"],
                     marginWidth=10,
                     collapsable=True)
    cmds.rowLayout("skeleton_layout", numberOfColumns=2, adjustableColumn=True)
    cmds.columnLayout("skeleton_col")
    cmds.rowLayout("skeleton_row", numberOfColumns=2)
    cmds.optionMenu("Skel_type", label="Skelet type: ", w=200, h=20)
    cmds.setParent("..")
    cmds.menuItem(label="Pibed")
    cmds.menuItem(label="Quad")

    cmds.rowLayout("Industry_layout", numberOfColumns=2, adjustableColumn=True)
    cmds.columnLayout("industry_col")
    cmds.rowLayout("industry_row", numberOfColumns=2)
    cmds.optionMenu("industry_type", label="Indust type: ",w=200, h=20)
    cmds.setParent("..")
    cmds.menuItem(label="Games")
    cmds.menuItem(label="VFX")
    cmds.optionMenu("Part_Name", label="Part Name: ",w=200, h=20)
    cmds.setParent("..")
    cmds.menuItem(label="Cog")
    cmds.menuItem(label="Spine")
    cmds.menuItem(label="Leg")
    cmds.menuItem(label="Arm")
    cmds.setParent("..")


    cmds.button(label="Change Chain Name!", command=lambda x: methods.skeleton_joints_rename(), h=30, w=200, align="center", bgc=gui_colors["beige"])
    cmds.setParent("..")
    cmds.setParent(main_layout)

    cmds.separator(height=10, style="in")

    cmds.text(label="-- @All Right Reserved --", align="center", font="boldLabelFont")
    cmds.separator(height=10, style="in")

    cmds.showWindow("AutoRename")



