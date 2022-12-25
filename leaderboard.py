<<<<<<< Updated upstream

=======
import ac
import acsys

# Create a new app instance
app = ac.newApp("Lap Time Display")

# Initialize lap time label
lap_time_label = ac.addLabel(app, "")

# Set label position and size
ac.setPosition(lap_time_label, 0, 0, 100, 100)

# Set label font and color
ac.setFontAlignment(lap_time_label, "center")
ac.setFontColor(lap_time_label, 1, 1, 1, 1)

# Set label font size
ac.setFontSize(lap_time_label, 32)

# Set label font type
ac.setFont(lap_time_label, "Roboto-Regular")

# Set label to display lap time
ac.setText(lap_time_label, "Lap Time: 00:00:00")

# Define update function
def update(deltaT):
    # Get lap time for player's car
    lap_time = ac.getCarState(0, acsys.CS.LapTime)
    # Format lap time as a string
    lap_time_str = "{:02d}:{:02d}:{:06.3f}".format(int(lap_time / 60000), int(lap_time / 1000) % 60, lap_time % 1000)
    # Update label text
    ac.setText(lap_time_label, "Lap Time: " + lap_time_str)

# Register update function to be called every frame
ac.addRenderCallback(update)
>>>>>>> Stashed changes
