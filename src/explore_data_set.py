# To enable this script to connect to Tecplot 360:
# In Tecplot 360, go to "Scripting" -> "PyTecplot Connections..." -> "Accept connections"
import tecplot
import time

start_time = time.time()

# Connect to Tecplot 360 session
tecplot.session.connect()

frame = tecplot.active_frame()
dataset = frame.dataset if frame is not None else None

if dataset is None:
    print("No dataset loaded in the active frame.")
else:
    # Print all variable names
    print("Variables:")
    for var in list(dataset.variables()):
        print(f"- {var.name}")

    # Print all zone names and their aux data
    print("Zones:")
    for zone in list(dataset.zones()):
        print(f"- {zone.name}")
        aux_data_names = list(zone.aux_data)
        if aux_data_names:
            print("  Aux Data:")
            for aux_name in aux_data_names:
                value = zone.aux_data[aux_name]
                print(f"    - {aux_name}: {value}")
        else:
            print("  (No aux data)")

end_time = time.time()
print(f"\nElapsed time: {end_time - start_time:.3f} seconds")
