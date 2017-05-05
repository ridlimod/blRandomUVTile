import bpy
import bmesh
from random import randint

def randomUVTile(mesh, HTiles, VTiles):
    bm = bmesh.new()
    bm.from_mesh(mesh)
    
    uv_lay = bm.loops.layers.uv.active
    
    for f in bm.faces:
        cx = float(randint(0,HTiles-1))/HTiles
        cy = float(randint(0,VTiles-1))/VTiles
        cx1 = cx + 1 / HTiles
        cy1 = cy + 1 / VTiles
        
        f.loops[0][uv_lay].uv = (cx,cy)
        f.loops[1][uv_lay].uv = (cx1,cy)
        f.loops[2][uv_lay].uv = (cx1,cy1)
        f.loops[3][uv_lay].uv = (cx,cy1)
                
    bm.to_mesh(data)
    bm.free()
    data.update()

obj = bpy.context.active_object
data = obj.data

randomUVTile(data,1,1)
