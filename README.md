# Auto Renaming Tool for Maya

A Python-based naming utility for Autodesk Maya designed to make repetitive scene-renaming tasks faster and more consistent.

The tool provides a simple Maya UI for renaming objects using **search & replace**, **custom prefixes**, and **position-based prefixes**, with the ability to apply operations to selected objects, their hierarchies, or the scene.

Built as part of a VFX rigging workflow, where consistent naming is important for rig organization, automation, and production handoff.

## Features

### Search & Replace

Replace matching text across object names.

**Example:**

`hero_geo` → `hero_mesh`

### Custom Prefix

Add a user-defined prefix to object names.

**Example:**

`hand_ctrl` → `char_hand_ctrl`

### Prefix by Position

Automatically assign a prefix based on an object's world-space X position:

| Position | Prefix |
| -------- | ------ |
| X > 0    | `LT`   |
| X < 0    | `RT`   |
| X = 0    | `CT`   |

This is useful for quickly applying left/right/center naming conventions to scene objects.

### Flexible Targeting

Operations can be applied to:

* **Selected** — currently selected objects
* **Hierarchy** — selected objects and their descendants
* **All** — objects across the scene

## Workflow

1. Select the target objects or hierarchy.
2. Choose the desired operation.
3. Enter the naming rule.
4. Apply the operation.
5. The tool updates the Maya scene with the new names.

## Technical Implementation

The tool is written in **Python** and runs directly inside Autodesk Maya.

* **`maya.cmds`** — Maya UI and scene interaction
* **PyMEL** — scene queries and object manipulation
* Modular structure separating UI, scene queries, and rename operations
* Rule-based naming operations
* Maya DAG hierarchy and transform queries

### Project Structure

```text
Renaming_Tool/
├── main.py
├── core/
│   └── base.py
├── ui/
│   └── gui.py
└── utils/
    └── methods.py
```

## Example

Given:

```text
L_arm_geo
L_hand_geo
L_arm_ctrl
```

Using **Search & Replace**:

```text
Search:  L_
Replace: left_
```

Produces:

```text
left_arm_geo
left_hand_geo
left_arm_ctrl
```

Using **Custom Prefix**:

```text
Prefix: char
```

Produces:

```text
char_L_arm_geo
char_L_hand_geo
char_L_arm_ctrl
```

## Why I Built It

In a production VFX environment, naming is more than organization. Consistent names make scene structures easier to understand and allow other tools and scripts to interact with them reliably.

This tool was built to reduce repetitive manual renaming and provide a more consistent naming workflow inside Maya.

## Status

**Version 1.0 — Prototype**

The core search/replace and prefix functionality is implemented. Additional naming operations shown in the UI are planned for future development.

## Future Improvements

* Rename preview before applying changes
* Collision detection and validation
* Undo/dry-run workflow
* Numbered renaming
* Suffix operations
* Configurable naming conventions
* Rename history / change log
* Automated tests
