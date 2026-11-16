""""
Tool Description: Auto Renaming Tool For Maya
Version: 1.0
Date: 2026-01-20
"""
import maya.cmds as cmds
import pymel.core as pm

from Renaming_Tool.core import base
import importlib
importlib.reload(base)
from Renaming_Tool.ui import gui
importlib.reload(gui)

def apply_on():
    categories = {"Selected": base.get_selected(), "Hierarchy": base.get_hierarchy(), "All": base.get_all()}
    cate_obj = cmds.optionMenu("apply_on", q=True, value=True)
    cate_target = categories.get(cate_obj,[])
    return cate_target

def search_replace():
    """
    search for a name using the search filed
    and replace it with new one using replace field

    :return: None
    """
    search_for = cmds.textField("SearchFor", q=True, text=True)
    replace_with = cmds.textField("ReplaceWith", q=True, text=True)

    if not search_for :
        cmds.warning("Fill the Search for Field!")
        return
    if not replace_with :
        cmds.warning("Fill Replace With Field!")
        return

    for obj in apply_on():
        try:
            full_name, short_name = base.get_obj_name(obj)
            new_name = short_name.replace(search_for, replace_with)

            pm.rename(full_name, new_name)


        except Exception as e:
            print(f"Could not rename {obj}: {e}")



def add_prefix():
    field_prefix = cmds.textField("Prefix", q=True, text=True)
    check_status = cmds.checkBox("PositionPrefix", q=True, value=True)

    if not field_prefix and not check_status:
        cmds.warning("Add a prefix first or check prefix by position!")
        return
    for obj in apply_on():
        try:
            full_name, short_name = base.get_obj_name(obj)
            prefix = None
            rename_status = False
            if check_status:
                pos = base.get_world_translation(obj)
                if pos[0] > 0 and not short_name.startswith("LT"):
                    prefix = "LT"
                    rename_status = True
                elif pos[0] < 0 and not short_name.startswith("RT"):
                    prefix = "RT"
                    rename_status = True
                elif pos[0] == 0 and not short_name.startswith("CT"):
                    prefix = "CT"
                    rename_status = True
                else:
                    cmds.warning("Prefix already exists!")
            else:
                prefix = field_prefix
                rename_status = True

            if rename_status:
                pm.rename(full_name, f"{prefix}_{short_name}")
        except Exception as e:
            print(f"Could not rename: {e}")

    """
def add_suffix():
    light_types = [
        "ambientLight",
        "directionalLight",
        "pointLight",
        "spotLight",
        "areaLight",
        "volumeLight"
    ]
    field_suffix = cmds.textField("Suffix", q=True, text=True)
    check_status = cmds.checkBox("TypeSuffix", q=True, value=True)
    suffix = None
    rename_status = False
    for obj in cmds.ls(sl=True):
        full_name, short_name = base.get_obj_name(obj)
        obj_type = base.get_obj_type(obj)
        if check_status:
            if obj_type == "mesh" and not short_name.endswith("Mesh"):
                suffix = "Mesh"
                rename_status = True
            elif obj_type == "camera" and not short_name.endswith("Cam"):
                suffix = "Cam"
                rename_status = True
            elif obj_type in light_types and not short_name.endswith("Light"):
                suffix = "Light"
                rename_status = True
            elif obj_type == "joint" and not short_name.endswith("JNT"):
                suffix = "JNT"
                rename_status = True
            elif obj_type == "nurbsCurve" and not short_name.endswith("Ctrl"):
                suffix = "Ctrl"
                rename_status = True
            elif obj_type == "curve" and not short_name.endswith("Ctrl"):
                suffix = "Ctrl"
                rename_status = True
            else:
                cmds.warning("The Type Suffix has already exists!")

        else:
            suffix = field_suffix
            rename_status = True

        if rename_status:
            cmds.rename(full_name, f"{short_name}_{suffix}")


def rename_with_offset():
    name = cmds.textField("Name", q=True, text=True)
    index_off = cmds.intField("Index", q=True, value=True)

    for index, obj in enumerate(cmds.ls(sl=True)):
        full_name, short_name = base.get_obj_name(obj)
        cmds.rename(short_name, f"{name}_0{index+index_off}")


def skeleton_joints_rename():
    skeleton_types={"Games":{"Cog":"Pelvis", "Spine":"Spine_0", "Leg":["Thigh", "Calf", "Foot", "Toe", "ToeEnd"],
                           "Arm":["Clavicle", "UpperArm", "ForeArm", "Hand"]},
                    "VFX":{"Cog":"COG", "Spine":"Spine_0", "Leg":["Hip", "Knee", "Ankle", "Toe", "ToeTip"],
                         "Arm":["Scapula", "Shoulder", "Elbow", "Wrist"]}}
    ind_type = cmds.optionMenu("Skeleton_type", q=True, value=True)
    part_name = cmds.optionMenu("Part_Name", q=True, value=True)


    target_name = skeleton_types[ind_type][part_name]
    if not target_name:
        cmds.warning("The NamingConvention Is not Right!")

    for index, obj in enumerate(cmds.ls(sl=True)):
        full_name, short_name = base.get_obj_name(obj)
        if isinstance(target_name, list):
            name = target_name[index]
        else:
            if part_name == "Spine":
                name = f"Spine_0{index+1}"
            else:
                name = target_name
        cmds.rename(obj, name)

"""



