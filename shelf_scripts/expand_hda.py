import hou
import os

nodes = hou.selectedNodes()
if not nodes:
    # hou.ui.displayMessage("Select a node that belongs to an HDA.")
    raise hou.Error("No node selected.")

node = nodes[0]
hda_def = node.type().definition()

if hda_def is None:
    # hou.ui.displayMessage("Selected node is not part of an HDA.")
    raise hou.Error("Selected node is not part of an HDA.")

hda_path = hda_def.libraryFilePath()

if not os.path.isfile(hda_path):
    # hou.ui.displayMessage(f"HDA file not found on disk:\n{hda_path}")
    raise hou.Error(f"HDA file missing.\n{hda_path}")

hda_dir = os.path.dirname(hda_path)
hda_name = os.path.splitext(os.path.basename(hda_path))[0]
dest_dir = os.path.join(hda_dir, "src")

os.makedirs(dest_dir, exist_ok=True)

hou.hda.expandToDirectory(hda_path, dest_dir)

hou.ui.displayMessage(f"Extracted HDA to:\n{dest_dir}")
