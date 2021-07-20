import glob
import os

for f in glob.glob('downsampled/*.jpg'):
  new_filename = f.replace(".jpg", "_downsampled.jpg")
  os.rename(f,new_filename)
