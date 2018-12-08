# Image Slicer (from scratch)

This blog will explain the code and equations mentioned in the code. Give it a read before going ahead.<br>
Blog - https://codeitplease.wordpress.com/2018/02/26/striding-and-slicing-images/

Slice an image (padded or unpadded) into smaller images (overlapping or non-overlapping). This is a custom built script without the use of any wrapper modules (other than numpy). 

## Use Case:

<li> Biomedical Images are High Definition. They can be sliced into smaller images, which may contain informative data. This also increases the training data for Machine Learning Algorithms. (Please visit the Blog for more details)<br>

<li> Going through Image Slicer code and the associated Blog post, image analysis enthusiast can understand the working behind striding, padding and convolution operations.

## About the Module

The module contains ImageSlicer class, which contains a 'transform' method. This method is the heart of the class - one of the two callable methods. Other one is 'save_images' method, specially tailored to save the 'transform' method's returned object. 

## Running the Module

While initialising the class object, you have to provide 'source' and 'size' parameters. Other parameters, viz. 'strides', 'PADDING' and 'BATCH' are optional. After initialising the object, call the 'transform' function. Now use the 'save_images' function to save the object returned by the 'transform' function.

<b>Run this Code</b><br>
<code>
import ImageSclicer as im</code>
<code>from str import ImageSlicer</code>
<code>slicer = ImageSlicer('xyz.jpg', (50,50)) #Provide image path and slice size you desire</code>
<code>transformed_image = slicer.transform()</code>
<code>slicer.save_images('/Folder', transformed_image) #Provide the directory where you want to save the sliced images</code>

## transform:
<br><b>Parameters</b><br>

'source' - Can be a directory path to a single image (default) or a directory path to a directory containg multiple images.<br>

'size' - tuple of desired height and width e.g. (100,100)<br>

'strides' - tuple of desired stride along height and stride along width, e.g. (100,100)<br>

'BATCH' - (default False) If source is a directory of images, then BATCH = True, else BATCH = False<br>

'PADDING' - (default False) If set True, will calculate appropriate padding that will give you complete images with respect to the given strides.<br>

<b>Returns</b><br>

Returns a dictionary with key - string of count starting from 1 e.g '1','2' and value - list of np.ndarray types of output images.

## save:

<br><b>About</b><br>

To save the output images in a file, the script also provides a 'save_images' method that will take the result of 'transform' method and 'source_dir' as input, and save all the images according to their respective main images with respective serial number as folder name.
