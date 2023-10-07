
# Update the value to 1998 of ESTAB if the existing value is 0 using update cursor
import arcpy
import os

gdb_path = r"D:\1_BVIEER\3rd_sem\Programming for GIS- III Mr. Ronit Jadhav\Practical_6\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["ESTAB", "NAME"]

with arcpy.da.UpdateCursor(fc_path, fields_list) as u_cursor:
    for row in u_cursor:
        print(row[0])
        print(row[1])

print("Process Completed")

