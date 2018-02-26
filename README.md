# Stride-and-Slice-Images

This blog will explain the code and equations mentioned in the code. Give it a read before going ahead.
Blog - https://codeitplease.wordpress.com/2018/02/26/striding-and-slicing-images/

Slice an image into smaller images (overlapping or non-overlapping). This is a custom built script without the use of any predefined function. The algorithm that will help an image analysis enthusiast to understand how striding, padding and convolution works.

The script contains a 'transform' function that takes 'source_dir', 'size', 'strides', 'PADDING' as variables and then returns a dictionary with key - string of count starting from 1 e.g '1','2' and value - list of np.ndarray types of output images e.g. [np.ndarray(size),]

'source_dir' - Can be a directory path to a single image or a directory path to a directory containg multiple images.

'size' - tuple of desired height and width e.g. (100,100)

'strides' - tuple of desired stride along height and stride along width, e.g. (100,100)

'PADDING' - (default False) If set True will calculate appropriate padding that will give you complete images with respect to the given strides.

To save the output images in a file, the script also provides a 'save_images' method that will take the result of 'transform' method as input and save all the images according to their respective main images with respective serial number as folder name.

How to run the script?
-->Run the scipt using idle-
  - Run the script in idle.
    - transform()
-->Import the script in python shell-
  - Run python shell in the directory where the script is stored
    - import strideslice as ss
    - ss.transform()
 
