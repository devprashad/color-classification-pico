<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Color Classification Project</h1>
    <h2>Objective</h2>
    <p>The goal of this project is to create a color classification system using a Raspberry Pi Pico, a ST7735 based 128x160 pixel TFT SPI display interface, and an OV7670 camera module. The system captures an image, analyzes its pixels, identifies the dominant color, and displays the result on the LCD.</p>
    <h2>Components Used</h2>
    <ul>
        <li>Raspberry Pi Pico</li>
        <li>ST7735 based 128x160 pixel TFT SPI display</li>
        <li>OV7670 Camera Module</li>
        <li>Jumper Wires</li>
        <li>Resistors (4.7kohm recommended) </li>
    </ul>
    <h2>Workflow</h2>
    <ol>
        <li><strong>Image Capture:</strong> The OV7670 camera module captures an image.</li>
        <li><strong>Pixel Analysis:</strong> The image is processed, and the pixel data is extracted.</li>
        <li><strong>Color Identification:</strong> The system identifies the dominant color by analyzing the pixel values.</li>
        <li><strong>Display Output:</strong> The result, indicating the dominant color, is displayed on the TFT Display.</li>
    </ol>
    <h2>Dependencies</h2>
    <ul>
        <li><strong>Thonny:</strong> Integrated Development Environment (IDE) used for Python programming on the Raspberry Pi Pico.</li>
        <li><strong>Camera Library:</strong> Libraries for interfacing with the OV7670 camera module.</li>
        <li><strong>TFT Library:</strong> Libraries for communication with the TFT using the I2C protocol.</li>
    </ul>
    <h2>Setup and Usage</h2>
    <ol>
        <li><strong>Hardware Connections:</strong> Connect the OV7670 camera module and the TFT display to the Raspberry Pi Pico according to the provided schematic.</li>
        <li><strong>Software Setup:</strong> Install the necessary libraries and dependencies on the Pico using Thonny.</li>
        <li><strong>Run the Code:</strong> Upload the code to the Pico and run the system.</li>
        <li><strong>View Results:</strong> Check the TFT display for the color classification results.</li>
        <li>Below is the final connected and working project of pico with camera module and TFT display.</li>
    </ol>
    <h1>Hardware Connections</h1>
    <p>Connect the following components to set up the hardware for the color classification project:</p>
    <h2>Raspberry Pi Pico Connections</h2>
    <ul>
        <li>Connect GPIO pins to OV7670 camera module for communication.</li>
        <li>Connect GPIO pins to ST7735 based 128x160 pixel TFT SPI display.</li>
        <li>Below is the image of the connected pico with camera and tft</li>
        !
        <img src="https://github.com/devprashad/ColorClassification/assets/110773439/e588e1f2-565d-4a4d-8cb3-344da70b5aa1"/>
    </ul>
    <h2>OV7670 Camera Module Connections</h2>
    <ul>
        <li>Connect OV7670 camera module to Raspberry Pi Pico GPIO pins.</li>
        <li>Check the conncectionofcamera.jpg image for the connection of Pico and 0v7670 Camera Module </li>
        <li>Image camera.jpg is the camera that is connected to the pico</li>
    </ul> 
    <h2>16x2 LCD Connections</h2>
    <ul>
        <li>Connect 16x2 LCD with I2C interface to Raspberry Pi Pico GPIO pins.</li>
        <li>Check the connectionoflcd.jpg image  for the connection of pico and 16*2 lcd with i2c</li>
        <li>Below image is the connection of LCD with Pico</li>
    </ul>
    <h2>Conclusion</h2>
    <p>This project demonstrates a practical application of image processing and color classification using affordable and accessible components. It can be extended for various applications, such as object recognition or sorting based on color.</p>
    <h2>Note</h2>
    <p>Ensure that you have the required libraries installed and the Thonny properly set up before running the code. Refer to the documentation for any additional information or troubleshooting.</p>
    <h2>Contributors</h2>
        <li>Dev Prashad K -> kdpdev2004@gmail.com </li>
        <li>Jagath Vishwa K  -> jagathvishwa08@gmail.com </li>
        <li>Karthick Prasanna ->  karthickprasannaj@gmail.com </li>   
        <li>Prasanth S ->  prasanth1612004@gmail.com </li>
        <li>Nagarjun Krishna ->  nagaarjunkrishna11@gmail.com </li>
</body>
</html>
