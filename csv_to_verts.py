# Convert your CSV file to vertices in Blender

import bpy
import csv
import bmesh

file = r'path\to\your\file\here'

with open(file, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    columns = []

    for row in reader:
        columns.append([row[1], row[2], row[3]])

mesh = bpy.data.meshes.new("Point Cloud")

new_object = bpy.data.objects.new("Point Cloud", mesh)

bpy.context.collection.objects.link(new_object)

bpy.context.view_layer.objects.active = new_object

if bpy.context.active_object.mode != 'OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')

bm = bmesh.new()

for column in columns:
    try:
        bm.verts.new((float(column[0]), float(column[1]), float(column[2])))
    except ValueError as e:
        print(f"Error adding vertex: {e}")

bm.to_mesh(mesh)
bm.free()

bpy.ops.object.mode_set(mode='OBJECT')

print("New object created and vertices added.")
