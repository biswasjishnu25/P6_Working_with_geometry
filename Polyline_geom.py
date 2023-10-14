import os
import arcpy

gdb_path = r"C:\Users\jishn\OneDrive\Documents\ArcGIS\Projects\programming3_prac6"

output_fc_name = "BVP to Mumbai"
fc_path = os.path.join(gdb_path, output_fc_name)

x_bvp = 73.85355678663343
y_bvp = 18.458988705183273

x_mumbai = 72.87636128602651
y_mumbai = 19.09645305736285

# Point object
point_bvp_obj = arcpy.Point(x_bvp,y_bvp)
point_mumbai_obj = arcpy.Point(x_mumbai,y_mumbai)

spatial_ref = arcpy.SpatialReference("WGS 1984")

polyline_array = arcpy.Array()

polyline_array.add(point_bvp_obj)
polyline_array.add(point_mumbai_obj)

polylines_geom = arcpy.Polyline(polyline_array, spatial_ref)
arcpy.CopyFeatures_management(polylines_geom,fc_path)
print("process complete")

