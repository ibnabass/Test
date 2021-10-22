# Image Reader Example
#
# USE THIS EXAMPLE WITH A USD CARD!
#
# This example shows how to use the Image Reader object to replay snapshots of what your
# OpenMV Cam saw saved by the Image Writer object for testing machine vision algorithms.

# Altered to allow full speed reading from SD card for extraction of sequences to the network etc. 
# Set the new pause parameter to false

import sensor, image, time

snapshot_source = False # Set to true once finished to pull data from sensor.

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

stream = None
if snapshot_source == False:
    stream = image.ImageIO("D:/Test/files_for_test_pratique/raw_images.bin", "r")

while(True):
    clock.tick()
    if snapshot_source:
        img = sensor.snapshot() 
    else:
        img = stream.read(copy_to_fb=True, loop=True, pause=True)
    # Do machine vision algorithms on the image here.
    # Binary conversion to RGB image
        img_rgb = image.binary_to_rgb(img)

        #Compression JPEG
        img_jpeg = image.compressed(quality = 50)

        #save on the disk
        path = 'D:/Test/image'+ str(img_jpeg)
        image.save(path)
        
    
    print(clock.fps())
