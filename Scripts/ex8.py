# -----------------------------------------------------------------------------
# Name:        GS2110_Cursor.py
# Purpose:     script for GS2110
# Author:      Malik Awan
# Created:     16/01/2023
# -----------------------------------------------------------------------------
# 2. Use a SearchCursor and the triple quoting method to create a where clause to print NAME, FIPS
# and SHAPE_AREA of Counties that start with a C.


# Import Modules and classes as required
import arcpy


# Main Function
def main():
    #################################
    # Step 1
    # Environment settings
    #################################
    # Set the Workspace for inputs
    # Remove unused paths
    arcpy.env.workspace = "../GDB/Florida.gdb"
    # Set overwriteOutput = True if required for GeoProcessing
    arcpy.env.overwriteOutput = True
    
    ##############################
    # Step 2
    ##############################
    # Copy and paste function/tool syntax as a comment
    # arcpy.management.AddField(in_table, field_name, field_type, {field_precision}, {field_scale}, {field_length},
    # {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain})
    #arcpy.da.SearchCursor(in_table, field_names, {where_clause},
    # {spatial_reference}, {explode_to_points}, {sql_clause})

    ##############################
    # Step 3
    ##############################
    # For each required parameter set a variable

    ##############################
    # Step 4
    ##############################
    # fcList = arcpy.ListFeatureClasses()
    # for fc in fcList:
    #     print(fc)

    in_table = "StParks"
    field_names = ['Shape_Area','HECTARES']
    #arcpy.management.AddField("StParks","HECTARES", "DOUBLE")
    with arcpy.da.UpdateCursor(in_table, field_names ) as cursor:
        for row in cursor:
            row[1] = row[0]/10000
            cursor.updateRow(row)
            print(f"{row[0]}{row[1]}")





main()
