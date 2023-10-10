import pandas
import arcpy
import os

csv_path = r"D:\1_BVIEER\3rd_sem\Programming for GIS- III Mr. Ronit Jadhav\Practical_6\estab_years.csv"
years_dict = {}

csv_df = pandas.read_csv(csv_path)
# for index, row in csv_df.iterrows():
#     print(row)

for index, row in csv_df.iterrows():
    years_dict[row.NAME] = row.ESTAB

gdb_path = r"D:\1_BVIEER\3rd_sem\Programming for GIS- III Mr. Ronit Jadhav\Practical_6\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME","ESTAB", "ADDR"]

# Checking Major Attractions name in CSV file. if any name are not present in CSV print the name

with arcpy.da.UpdateCursor(fc_path, fields_list) as u_cursor:
    for row in u_cursor:
        if row[0] in years_dict:
            print(row[0])
        else:
            print("Major Attraction: {} not in CSV".format(row[0]))

        u_cursor.updateRow(row)

print("process Completed")
