import numpy as np
from vedo import *
import mrcfile
import argparse


def open_mrcs_file(file_path):
    with mrcfile.open(file_path) as mrc_stack:
        return mrc_stack.data


def slider(widget, event):
    # get the slider position and calculate the value based on the volume scalar data
    value = widget.GetRepresentation().GetValue()
    value = value / 100 * (np.max(data0) - np.min(data0))

    '''
    # update the volume based on the raw volume, used for volume view
    # can be activated if someone would like to

    import vtk
    from vtk.util.numpy_support import numpy_to_vtk
    varr = numpy_to_vtk(data0.ravel(), deep=True, array_type=vtk.VTK_FLOAT)
    varr.SetName('input_scalars')
    img = vtk.vtkImageData()
    img.SetDimensions(data0.shape)
    img.GetPointData().SetScalars(varr)
    vol._updateVolume(img)
    vol.threshold(value)
    '''

    iso.update_dataset(vol.isosurface(value=value).dataset)
    print('Volume threshold: {}'.format(round(value, 4)))


def slider_color(widget, event):
    value = widget.GetRepresentation().GetValue()
    iso.color(value)


# Look for the file location
parser = argparse.ArgumentParser(description='Open MRC Volume file and change the threshold')
parser.add_argument('--path', metavar='path', type=str, help='MRC volume path')
args = parser.parse_args()
file_path = args.path

if file_path == None:
    import easygui
    file_path = easygui.fileopenbox()

# open MRC volume and calculate density distribution
data0 = np.array(open_mrcs_file(file_path))
print('Volume shape is: {}'.format(data0.shape))
print('Press h for help and windows commands!')
ini_threshold = (2 * np.min(data0) + np.max(data0)) / 3.0

# change numpy object to vlt volume and set the threshold
vol = Volume(data0).mode(0)
iso = vol.isosurface(value=ini_threshold).color('gray')

# Add actors to the Plotter
vp2 = Plotter(shape=[1, 1], size=(800, 800), bg='white')
# Volume threshold in % because the raw values does not look "nice" on the slider
vp2.add_slider(slider, xmin=0, xmax=100, title="volume threshold, %", show_value=True, value=ini_threshold* 100/(np.max(data0) - np.min(data0)))
vp2.add_slider(slider_color, xmin=1, xmax=100, title="color", show_value=True, pos=2)
vp2.show(iso)
vp2.show(interactive=True)
