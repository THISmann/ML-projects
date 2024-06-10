def read_gcode_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def convert_gcode_to_fanuc(gcode_lines):
    fanuc_program = "/PROG EGOROV\n"
    fanuc_program += "/ATTR\n"
    fanuc_program += "OWNER\t\t= MNEDITOR;\n"
    fanuc_program += "COMMENT\t\t= \"\";\n"
    fanuc_program += "PROG_SIZE\t= 2847;\n"
    fanuc_program += "CREATE\t\t= DATE 21-10-18  TIME 19:03:40;\n"
    fanuc_program += "MODIFIED\t= DATE 21-10-27  TIME 17:17:30;\n"
    fanuc_program += "FILE_NAME\t= ;\n"
    fanuc_program += "VERSION\t\t= 0;\n"
    fanuc_program += "LINE_COUNT\t= " + str(len(gcode_lines)) + ";\n"
    fanuc_program += "MEMORY_SIZE\t= 3167;\n"
    fanuc_program += "PROTECT\t\t= READ_WRITE;\n"
    fanuc_program += "TCD:  STACK_SIZE\t= 0,\n"
    fanuc_program += "      TASK_PRIORITY\t= 50,\n"
    fanuc_program += "      TIME_SLICE\t= 0,\n"
    fanuc_program += "      BUSY_LAMP_OFF\t= 0,\n"
    fanuc_program += "      ABORT_REQUEST\t= 0,\n"
    fanuc_program += "      PAUSE_REQUEST\t= 0;\n"
    fanuc_program += "DEFAULT_GROUP\t= 1,*,*,*,*;\n"
    fanuc_program += "CONTROL_CODE\t= 00000000 00000000;\n"
    fanuc_program += "/APPL\n"
    fanuc_program += "/APPL\n"
    
    fanuc_program += "LINE_TRACK;\n"
    fanuc_program += "  LINE_TRACK_SCHEDULE_NUMBER      : 0;\n"
    fanuc_program += "  LINE_TRACK_BOUNDARY_NUMBER      : 0;\n"
    fanuc_program += "  CONTINUE_TRACK_AT_PROG_END      : TRUE;\n\n"
    
    fanuc_program += "/MN\n"

    fanuc_positions = {}
    current_position_id = 1

    for line in gcode_lines:
        line = line.strip()
        if line.startswith("G00"):
            parts = line.split()
            coords = {part[0]: float(part[1:]) for part in parts[1:] if part.startswith(('X', 'Y', 'Z'))}
            if 'X' not in coords or 'Y' not in coords:
                continue
            if 'Z' not in coords:
                coords['Z'] = 0.0  # Default Z to 0 if not specified
            
            x, y, z = coords['X'], coords['Y'], coords['Z']
            position_key = f"P[{current_position_id}]"
            
            if position_key not in fanuc_positions:
                fanuc_positions[position_key] = {
                    "X": x,
                    "Y": y,
                    "Z": z
                }
                current_position_id += 1
                
            fanuc_program += f"   {current_position_id - 1}:J P[{current_position_id}] 50% FINE    ;\n"

    fanuc_program += "/POS\n"

    for key, value in fanuc_positions.items():
        fanuc_program += f"{key}{{\n"
        fanuc_program += "   GP1:\n"
        fanuc_program += f"\tUF : 8, UT : 8,\t\tCONFIG : 'N U T, 0, 0, 0',\n"
        fanuc_program += f"\tX = {value['X']:.3f} mm,\tY = {value['Y']:.3f} mm,\tZ = {value['Z']:.3f} mm,\n" 
        fanuc_program += "};\n"

    fanuc_program += "/END\n"
    
    return fanuc_program

# Path to your G-code file
file_path = 'output.gcode'
gcode_lines = read_gcode_file(file_path)

fanuc_program = convert_gcode_to_fanuc(gcode_lines)
output_file_name = 'converted_fanuc_program.txt'

# Write the Fanuc program to a file
with open(output_file_name, 'w') as file:
    file.write(fanuc_program)

print(f"Converted Fanuc program has been written to {output_file_name}.")
