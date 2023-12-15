import board,busio
from time import sleep
from adafruit_st7735r import ST7735R
import displayio
import terminalio
from adafruit_display_text import label

mosi_pin = board.GP3
clk_pin = board.GP6
reset_pin = board.GP1
cs_pin = board.GP2
dc_pin = board.GP0

displayio.release_displays()
spi = busio.SPI(clock=clk_pin,MOSI=mosi_pin)
display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)
display=ST7735R(display_bus, width=128, height=160, bgr = True)
splash=displayio.Group()
display.show(splash)
color_bitmap = displayio.Bitmap(128,150,1)

color_palette=displayio.Palette(1)

color_palette[0]= 0x00FF00 #Bright Green

bg_sprite=displayio.TileGrid(color_bitmap,pixel_shader=color_palette,x=0,y=0)
splash.append(bg_sprite)

#Draw a smaller Inner rectangle

inner_bitmap=displayio.Bitmap(118,150,1)

inner_palette=displayio.Palette(1)
inner_palette[0] =0x000000 

inner_sprite=displayio.TileGrid(inner_bitmap,pixel_shader=inner_palette,x=5,y=5)
splash.append(inner_sprite)

text_group=displayio.Group(scale=1, x=11, y=24)

text ="LOKESH PRAKASAM!\n\nThis is a sample\ntext!\n\nEverything is \nusking fine."
text_area=label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_group.append(text_area)
splash.append(text_group)