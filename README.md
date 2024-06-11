# MRCVolume viewer
Preview mrc volume in a simple viewer!

![](https://github.com/dzyla/MRCVolume_viewer/blob/master/7OwD44WAc61.gif)

## Prerequisite
```
conda create -n mrcviewer python=3.12
conda activate mrcviewer
conda install -c conda-forge numpy vedo mrcfile easygui
```

## How to
run the script via command line or double click the file (windows). 

    python3 MRCVolume_viewer.py --path /path/to/file.mrc

Script should automatically guess the starting threshold value of the volume to create the isosurface. It can be changed with the slider at the botton and the color with one at the top. For more functionality coming from VTKplotter click h:

![](https://github.com/dzyla/MRCVolume_viewer/blob/master/Capture.JPG)

## Limitations
Depending on the system setup, huge maps (300px+) might open very slowly and threshold level update might be not as smooth. I would suggest to not use low threshold values in those cases!
