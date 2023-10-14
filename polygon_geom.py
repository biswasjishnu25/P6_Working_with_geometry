import os
import arcpy

gdb_path = r"C:\Users\jishn\OneDrive\Documents\ArcGIS\Projects\programming3_prac6"

output_fc_name = "BVP to Mumbai_Barmuda_new"
fc_path = os.path.join(gdb_path, output_fc_name)

x_bvp = 73.85355678663343
y_bvp = 18.458988705183273

x_mumbai = 72.87636128602651
y_mumbai = 19.09645305736285

X_Barmuda = 73.06399511650912
y_Barmuda = 18.532327928993187

# Point object
point_bvp_obj = arcpy.Point(x_bvp,y_bvp)
point_mumbai_obj = arcpy.Point(x_mumbai,y_mumbai)
point_barmuda_obj = arcpy.Point(X_Barmuda, y_Barmuda)

spatial_ref = arcpy.SpatialReference("WGS 1984")

polygon_array = arcpy.Array()

polygon_array.add(point_bvp_obj)
polygon_array.add(point_mumbai_obj)
polygon_array.add(point_barmuda_obj)

polygon_geom = arcpy.Polygon(polygon_array,spatial_ref)

arcpy.CopyFeatures_management(polygon_geom, fc_path)

print("process complete")

