import sys
import ac
import acsys

# Create a label to display the lap time
lap_time_label = ac.addLabel(f"lap_time_label")

# Set the initial lap time to 0
lap_time = 0

def acMain(ac_version):
    appWindow = ac.newApp("RougeRacingManager")
    ac.setSize(appWindow, 200, 200)
    return "RougeRacingManager"

def acUpdate(deltaT):
    global lap_time
    
    # Get the current lap time from the game
    lap_time = ac.getCarState(0, acsys.CS.LapTime)
    
    # Update the lap time label with the current lap time
    ac.setText(lap_time_label, f"Lap Time: {lap_time:.2f}")

# Register the acUpdate function to be called every frame
ac.setUpdateCallback(acUpdate)
