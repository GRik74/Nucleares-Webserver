# NUCLEARES GAME WEB SERVER LISTENER
# ==================================
#
# Made by @CypeFox on Discord
# Version 1
#
# Permission hereby given to be used for any purpose. I put a bit of work into this,
# so I'd be grateful if you include me in the credits, if you make something cool of it! ^^
#
# This code includes all existing veriables that the built-in server provides.
# It only runs once each time the script is ran, so you'd have to run it again to get updates.
# This is however very simple to change.
#
# Ideas on where to go next with the code:
# - Merge multiple conditions into single status texts for more simplified information display
# - Make a dashboard showing you the status of your reactor
#
# Feel free to ping me with any ideas or for any collaboration proposals. :)
#
# Have fun!
# ~Cype

from ReactorData import ReactorData

reactor = ReactorData("http://localhost:8785/")






# List of variables to query from Nucleares' web server
# variables = [
#     "TIME", "TIME_STAMP", "CORE_TEMP", "CORE_TEMP_OPERATIVE", "CORE_TEMP_MAX",
#     "CORE_TEMP_MIN", "CORE_TEMP_RESIDUAL", "CORE_PRESSURE", "CORE_PRESSURE_MAX",
#     "CORE_PRESSURE_OPERATIVE", "CORE_INTEGRITY", "CORE_WEAR", "CORE_STATE",
#     "CORE_STATE_CRITICALITY", "CORE_CRITICAL_MASS_REACHED",
#     "CORE_CRITICAL_MASS_REACHED_COUNTER", "CORE_IMMINENT_FUSION",
#     "CORE_READY_FOR_START", "CORE_STEAM_PRESENT", "CORE_HIGH_STEAM_PRESENT",
#     "COOLANT_CORE_STATE", "COOLANT_CORE_PRESSURE", "COOLANT_CORE_MAX_PRESSURE",
#     "COOLANT_CORE_VESSEL_TEMPERATURE", "COOLANT_CORE_QUANTITY_IN_VESSEL",
#     "COOLANT_CORE_PRIMARY_LOOP_LEVEL", "COOLANT_CORE_FLOW_SPEED",
#     "COOLANT_CORE_FLOW_ORDERED_SPEED", "COOLANT_CORE_FLOW_REACHED_SPEED",
#     "COOLANT_CORE_QUANTITY_CIRCULATION_PUMPS_PRESENT",
#     "COOLANT_CORE_QUANTITY_FREIGHT_PUMPS_PRESENT",
#     "COOLANT_CORE_CIRCULATION_PUMP_0_STATUS",
#     "COOLANT_CORE_CIRCULATION_PUMP_1_STATUS",
#     "COOLANT_CORE_CIRCULATION_PUMP_2_STATUS",
#     "COOLANT_CORE_CIRCULATION_PUMP_0_DRY_STATUS",
#     "COOLANT_CORE_CIRCULATION_PUMP_1_DRY_STATUS",
#     "COOLANT_CORE_CIRCULATION_PUMP_2_DRY_STATUS",
#     "COOLANT_CORE_CIRCULATION_PUMP_0_OVERLOAD_STATUS",
#     "COOLANT_CORE_CIRCULATION_PUMP_1_OVERLOAD_STATUS",
#     "COOLANT_CORE_CIRCULATION_PUMP_2_OVERLOAD_STATUS",
#     "COOLANT_CORE_CIRCULATION_PUMP_0_ORDERED_SPEED",
#     "COOLANT_CORE_CIRCULATION_PUMP_1_ORDERED_SPEED",
#     "COOLANT_CORE_CIRCULATION_PUMP_2_ORDERED_SPEED",
#     "COOLANT_CORE_CIRCULATION_PUMP_0_SPEED",
#     "COOLANT_CORE_CIRCULATION_PUMP_1_SPEED",
#     "COOLANT_CORE_CIRCULATION_PUMP_2_SPEED",
#     "RODS_STATUS", "RODS_MOVEMENT_SPEED",
#     "RODS_MOVEMENT_SPEED_DECREASED_HIGH_TEMPERATURE",
#     "RODS_DEFORMED", "RODS_TEMPERATURE", "RODS_MAX_TEMPERATURE",
#     "RODS_POS_ORDERED", "RODS_POS_ACTUAL", "RODS_POS_REACHED",
#     "RODS_QUANTITY", "RODS_ALIGNED"
# ]
#
# # The URL of Nucleares' web server (make sure to enable it in Tablet first, under "Status")
# url = "http://localhost:8080/"
#
#
# # Function to make a GET request for each variable
# def get_variable(variable):
#     try:
#         response = requests.get(url, params={'variable': variable})
#         if response.status_code == 200:
#             return f"{variable}: {response.text}"
#         else:
#             return f"{variable}: Error - Server responded with status code {response.status_code}"
#     except requests.RequestException as e:
#         return f"{variable}: Request Error - {e}"
#
#
# # Function to translate output lines
# def translate_output_line(line):
#     parts = line.split(": ")
#     if len(parts) != 2:
#         return line  # Return the original line if it's not in 'variable: value' format
#
#     variable, value = parts[0], parts[1].strip()
#     return f"{variable}: {translate_to_english(variable, value)}"
#
#
# # Translation function
# def translate_to_english(variable, value):
#     translations = {
#         "CORE_STATE": {
#             "NOREACTIVO": "NOT_REACTIVE",
#             "REACTIVO": "REACTIVE"
#         },
#         "CORE_STATE_CRITICALITY": {
#             "SUBCRITICO": "SUBCRITICAL",
#             "CRITICO": "CRITICAL"
#         },
#         "COOLANT_CORE_STATE": {
#             "INMOVIL": "IMMOBILE",
#             "CIRCULANDO": "CIRCULATING"
#         },
#         "COOLANT_CORE_CIRCULATION_PUMP_0_STATUS": {
#             "0": "NOT_ACTIVE",
#             "1": "ACTIVE_AND_NOT_REACHED_SET_VELOCITY",
#             "2": "ACTIVE_AND_REACHED_SET_VELOCITY",
#             "3": "ACTIVE_AND_REQUIRES_MAINTENANCE",
#             "4": "INACTIVE_OR_NOT_OPERATIONAL",
#             "5": "ACTIVATION_REQUESTED_BUT_INSUFFICIENT_POWER"
#         },
#         "COOLANT_CORE_CIRCULATION_PUMP_1_STATUS": {
#             "0": "NOT_ACTIVE",
#             "1": "ACTIVE_AND_NOT_REACHED_SET_VELOCITY",
#             "2": "ACTIVE_AND_REACHED_SET_VELOCITY",
#             "3": "ACTIVE_AND_REQUIRES_MAINTENANCE",
#             "4": "INACTIVE_OR_NOT_OPERATIONAL",
#             "5": "ACTIVATION_REQUESTED_BUT_INSUFFICIENT_POWER"
#         },
#         "COOLANT_CORE_CIRCULATION_PUMP_2_STATUS": {
#             "0": "NOT_ACTIVE",
#             "1": "ACTIVE_AND_NOT_REACHED_SET_VELOCITY",
#             "2": "ACTIVE_AND_REACHED_SET_VELOCITY",
#             "3": "ACTIVE_AND_REQUIRES_MAINTENANCE",
#             "4": "INACTIVE_OR_NOT_OPERATIONAL",
#             "5": "ACTIVATION_REQUESTED_BUT_INSUFFICIENT_POWER"
#         },
#         "COOLANT_CORE_CIRCULATION_PUMP_0_DRY_STATUS": {
#             "1": "ACTIVE_AND_DRY",
#             "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
#         },
#         "COOLANT_CORE_CIRCULATION_PUMP_1_DRY_STATUS": {
#             "1": "ACTIVE_AND_DRY",
#             "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
#         },
#         "COOLANT_CORE_CIRCULATION_PUMP_2_DRY_STATUS": {
#             "1": "ACTIVE_AND_DRY",
#             "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
#         },
#         "COOLANT_CORE_CIRCULATION_PUMP_0_OVERLOAD_STATUS": {
#             "1": "ACTIVE_AND_OVERLOADED",
#             "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
#         },
#         "COOLANT_CORE_CIRCULATION_PUMP_1_OVERLOAD_STATUS": {
#             "1": "ACTIVE_AND_OVERLOADED",
#             "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
#         },
#         "COOLANT_CORE_CIRCULATION_PUMP_2_OVERLOAD_STATUS": {
#             "1": "ACTIVE_AND_OVERLOADED",
#             "4": "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED"
#         },
#         "RODS_STATUS": {
#             "INMOVIL": "IMMOBILE",
#             "AJUSTANDO": "ADJUSTING"
#         },
#     }
#
#     # Translate if the variable and value are found in the dictionary
#     if variable in translations and value in translations[variable]:
#         return translations[variable][value]
#     else:
#         return value  # Return the original value if no translation is found
#
#
# # Requesting each variable and storing the responses
# output_lines = [get_variable(var) for var in variables]
#
# ## [old code] Translating each line and printing
# # for line in output_lines:
# #    print(translate_output_line(line))
#
# # Initialize an empty dictionary to store the reactor data
# reactor_data = {}
#
# # Iterate over each line in the output
# for line in output_lines:
#     # Translate the line (e.g., translate status codes to readable text)
#     translated_line = translate_output_line(line)
#
#     # Split the translated line into variable name and value
#     # Expecting the format "VARIABLE_NAME: value"
#     parts = translated_line.split(": ")
#     if len(parts) == 2:
#         # Extract the variable name and value from the parts
#         variable_name, variable_value = parts
#
#         # Strip any leading/trailing whitespace from the value
#         variable_value = variable_value.strip()
#
#         # Store the variable and its value in the reactor_data dictionary
#         reactor_data[variable_name] = variable_value
#
#
# # At this point, reactor_data contains all variables with their corresponding values
# # Do remember that all values are STRINGS, even those that look like INTS!
# # You can now use this dictionary for further analysis
#
#
# # Function to print reactor data
# def print_reactor_data(reactor_data):
#     print("Reactor Data:")
#     for key, value in reactor_data.items():
#         print(f"{key}: {value}")
#
#
# # Call the function to print the data
# print_reactor_data(reactor_data)
#
#
# # For example, let's make an analyze_reactor_status function, and pass it the reactor data
#
# def analyze_reactor_status(data):
#     print(f"Test: {type(data['CORE_INTEGRITY'])}")
#
#     # Check if the reactor is shut down
#     is_shutdown = data["CORE_STATE"] == "NOT_REACTIVE" and \
#                   data["CORE_PRESSURE"] == "1" and \
#                   all(pump_status == "INACTIVE_OR_NOT_OPERATIONAL" for pump_status in [
#                       data["COOLANT_CORE_CIRCULATION_PUMP_0_STATUS"],
#                       data["COOLANT_CORE_CIRCULATION_PUMP_1_STATUS"],
#                       data["COOLANT_CORE_CIRCULATION_PUMP_2_STATUS"]
#                   ])
#
#     # Check if the reactor is ready for start
#     is_ready_for_start = data["CORE_READY_FOR_START"] == "TRUE" and \
#                          data["CORE_INTEGRITY"] == "100" and \
#                          data["COOLANT_CORE_CIRCULATION_PUMP_2_STATUS"] == "NOT_ACTIVE"
#
#     # Check if there are any critical issues
#     has_critical_issues = data["CORE_CRITICAL_MASS_REACHED"] == "TRUE" or \
#                           data["CORE_IMMINENT_FUSION"] == "TRUE"
#
#     # Check if maintenance is required
#     requires_maintenance = any(pump_status == "INACTIVE_OR_NOT_OPERATIONAL_OR_MAINTENANCE_REQUIRED" for pump_status in [
#         data["COOLANT_CORE_CIRCULATION_PUMP_0_STATUS"],
#         data["COOLANT_CORE_CIRCULATION_PUMP_1_STATUS"],
#         data["COOLANT_CORE_CIRCULATION_PUMP_2_STATUS"]
#     ])
#
#     # Print out conclusions
#     print()
#     print("Reactor Status Analysis:")
#     print("------------------------")
#     print(f" - Reactor Shutdown: {'Yes' if is_shutdown else 'No'}")
#     print(f" - Ready for Start: {'Yes' if is_ready_for_start else 'No'}")
#     print(f" - Critical Issues: {'Yes' if has_critical_issues else 'No'}")
#     print(f" - Maintenance Required: {'Yes' if requires_maintenance else 'No'}")
#
#
# analyze_reactor_status(reactor_data)