import gc
import sys
from time import sleep

import bitmaptools
import board
import busio
import digitalio
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_ov7670 import OV7670
from adafruit_st7735r import ST7735R




# Function to convert RGB565_SWAPPED to grayscale

def find_mode(arr):
    # Dictionary to store the count of each element
    count_dict = {}

    # Iterate through the array and count occurrences
    for rgb565_value in arr:
        # Extract the red, green, and blue components from RGB565
        red = (rgb565_value >> 11) & 0x1F
        green = (rgb565_value >> 5) & 0x3F
        blue = rgb565_value & 0x1F

        # Convert to a tuple for comparison
        color_tuple = (red, green, blue)

        if color_tuple in count_dict:
            count_dict[color_tuple] += 1
        else:
            count_dict[color_tuple] = 1

    # Find the maximum count
    max_count = max(count_dict.values())

    # Find the elements with the maximum count (modes)
    modes = [color_tuple for color_tuple, count in count_dict.items() if count == max_count]

    # If there are multiple modes, return the first one
    return modes[0]



cam_width = 80
cam_height = 60
cam_size = 3 #80x60 resolution

camera_image = displayio.Bitmap(cam_width, cam_height, 65536)
camera_image_tile = displayio.TileGrid(
    camera_image ,
    pixel_shader=displayio.ColorConverter(
        input_colorspace=displayio.Colorspace.RGB565
    ),
    x=30,
    y=30,
)

camera_image_tile.transpose_xy=True

inference_image = displayio.Bitmap(12,12, 65536)

#Setting up the camera
cam_bus = busio.I2C(board.GP9, board.GP8)

cam = OV7670(
    cam_bus,
    data_pins=[
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
        board.GP16,
        board.GP17,
        board.GP18,
        board.GP19,
    ],
    clock=board.GP11,
    vsync=board.GP7,
    href=board.GP21,
    mclk=board.GP20,
#shutdown=None,
    reset=board.GP10,
)
cam.size =  cam_size
cam.flip_y = True

ctr = 0
ans=[]

def color_decide(x):
    if x==(9,47,29):
        print("RED")
    elif x==(27,43,12):
        print("BLUE")
    elif x==(30,46,5):
        print("GREEN")
    elif x==(8,1,17):
        print("BLACK")
    elif x==(31,47,29):
        print("WHITE")
    elif x==(31,7,29):
        print("YELLOW")
    else:
        print("UNABLE TO DETECT COLOUR")
while True:
    cam.capture(camera_image)
    sleep(0.1)
    temp_bmp = displayio.Bitmap(cam_height, cam_height, 65536)
    for i in range(0,cam_height):
        for j in range(0,cam_height):
            temp_bmp[i,j] =  camera_image[i,j]
            ans.append(temp_bmp[i,j])
#             print(temp_bmp[i,j])
          
    
    color_decide(find_mode(ans))
    
    ans=[]