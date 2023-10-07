# Update the value of HISTORIC field to "YES" if ESTAB is greator than 1960 and less than 1980 or else update to "NO"

import arcpy
import os

gdb_path = r"D:\1_BVIEER\3rd_sem\Programming for GIS- III Mr. Ronit Jadhav\Practical_6\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME","ESTAB", "HISTORIC"]

with arcpy.da.UpdateCursor(fc_path, fields_list) as u_cursor:
    for row in u_cursor:
        establishYear=row[1]

        if establishYear >1960 and establishYear <1980:
            row[2] = "YES"
        else:
            row[2] = "NO"

        u_cursor.updateRow(row)

print("Process Completed")
