# Inserting multiple new records in Attribute table

import arcpy
import os

gdb_path = r"D:\1_BVIEER\3rd_sem\Programming for GIS- III Mr. Ronit Jadhav\Practical_6\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME","ESTAB", "ADDR"]

# This is a Tuple, We can not change the values after editing
records_list = [("NEWATTRACTION", 2023, "STREET123"), ("Circus", 2021, "Wasington DC"), ("PlayGround", 2022, "NewYork")]

i_cursor = arcpy.da.InsertCursor(fc_path, fields_list)

for record in records_list:
    i_cursor.insertRow(record)

print("Process Completed")
