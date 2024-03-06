import numpy as np

# Define the input and output values 
width_height_max = [16, 18, 20, 21, 25, 28, 33, 40, 48, 54, 58, 64, 69, 74, 85]
ball_distance = [310, 280, 250, 230, 200, 180, 150, 125, 100, 90, 80, 70, 60, 50, 40] 

# Define a function to interpolate the output values based on the input values
def interpolate(input_value):
    if input_value <= width_height_max[-1]:
        return np.interp(input_value, width_height_max, ball_distance)
    else:
        return width_height_max[-1]

# Test the interpolation for some input values
test_ball_distance = [33, 25, 10, 80, 20, 50]
for input_value in test_ball_distance:
    output_value = interpolate(input_value)
    print(f"For input value {input_value}, output value is approximately {output_value}")
