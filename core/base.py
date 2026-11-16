""""
Tool Description: Auto Renaming Tool For Maya
Version: 1.0
Date: 2026-01-20
"""
import maya.cmds as cmds
import pymel.core as pm

def get_all():
    all = pm.ls(dag=True, editable=True, ro=False, assemblies=True)

    return all


def get_selected():
    selection = pm.ls(sl=True)
    return selection


def get_hierarchy():
    hier = get_selected()
    children = pm.listRelatives(hier, ad=1)
    children.reverse()
    hier.extend(children)
    return hier



def get_obj_name(obj):

    full_name = pm.ls(obj,long=True)[0]
    short_name = full_name.split('|')[-1]
    return  full_name, short_name


def get_obj_type(obj):
    obj_shapes = pm.listRelatives(obj, shapes=True)
    if obj_shapes:
        obj_shape = obj_shapes[0]
        obj_type = pm.nodeType(obj_shape)
    else:
        obj_type = pm.nodeType(obj)

    return obj_type


def get_world_translation(obj):
    translation = pm.xform(obj, q=True, ws=True, t=True)
    return translation
