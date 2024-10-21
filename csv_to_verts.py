# Adds vertices to the selected object

import bpy
import csv
import bmesh

file = r'C:\Users\ppmpr\OneDrive\Documents\Blender\df_train.csv'

with open(file, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    columns = []

    for row in reader:
        columns.append([row[1], row[2], row[3]])

obj = bpy.context.active_object

if obj and obj.type == 'MESH':
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Get the BMesh from the object
    bm = bmesh.from_edit_mesh(obj.data)

    # Add a new vertex at a specified location
    for column in columns:
        try:
             bm.verts.new((float(column[0])/10,float(column[1])/10,float(column[2])/10))
        except ValueError as e:
            print(f"Error adding vertex: {e}")
            
    # Optional: Update the mesh to reflect the changes
    bmesh.update_edit_mesh(obj.data)
    
    # Switch back to Object Mode
    bpy.ops.object.mode_set(mode='OBJECT')

else:
    print("Selected object is not a mesh.")
