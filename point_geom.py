import arcpy
import os

x_bvp = 73.85355678663343
y_bvp = 18.458988705183273

# point object
pnt_obj = arcpy.Point(x_bvp, y_bvp)

# spatial reference
spatial_ref = arcpy.SpatialReference("WGS 1984")

# point geometry
pnt_geom = arcpy.PointGeometry(pnt_obj, spatial_ref)

gdb_path = r"C:\Users\jishn\OneDrive\Documents\ArcGIS\Projects\programming3_prac6\programming3_prac6.gdb"

fc_name = "bvp_katraj"
fc_path = os.path.join(gdb_path)

arcpy.CopyFeatures_management(pnt_geom, fc_path)
print("Process complete")