import numpy as np
import matplotlib.pyplot as plt
import os
 
class ImageSlicer(object):
    
    def __init__(self, source, size, strides=[None, None], BATCH = False, PADDING=False):
        self.source = source
        self.size = size
        self.strides = strides
        self.BATCH = BATCH
        self.PADDING = PADDING
        
    def __read_images(self):
        Images = []
        image_names = sorted(os.listdir(self.source))
        for im in image_names:
            image = plt.imread(os.path.join(dir_path,im))
            Images.append(image)
        return Images

    def __offset_op(self, input_length, output_length, stride):
        offset = (input_length) - (stride*((input_length - output_length)//stride)+output_length)
        return offset
    
    def __padding_op(self, Image):
        if self.offset_x > 0:
            padding_x = self.strides[0] - self.offset_x
        else:
            padding_x = 0
        if self.offset_y > 0:
            padding_y = self.strides[1] - self.offset_y
        else:
            padding_y = 0
        Padded_Image = np.zeros(shape=(Image.shape[0]+padding_x, Image.shape[1]+padding_y, Image.shape[2]),dtype=Image.dtype)
        Padded_Image[padding_x//2:(padding_x//2)+(Image.shape[0]),padding_y//2:(padding_y//2)+Image.shape[1],:] = Image    
        return Padded_Image

    def __convolution_op(self, Image):
        start_x = 0
        start_y = 0
        n_rows = Image.shape[0]//self.strides[0] + 1
        n_columns = Image.shape[1]//self.strides[1] + 1
        small_images = []
        for i in range(n_rows-1):
            for j in range(n_columns-1):
                new_start_x = start_x+i*self.strides[0]
                new_start_y= start_y+j*self.strides[1]
                small_images.append(Image[new_start_x:new_start_x+self.size[0],new_start_y:new_start_y+self.size[1],:])
        return small_images

    def transform(self):
        
        if not(os.path.exists(self.source)):
            raise Exception("Path does not exist!")
            
        else:
            if self.source and not(self.BATCH):
                Image = plt.imread(self.source)
                Images = [Image]
            else: 
                Images = self.__read_images()

            im_size = Images[0].shape
            num_images = len(Images)
            transformed_images = dict()
            Images = np.array(Images)
            
            if self.PADDING:
                
                padded_images = []

                if self.strides[0]==None and self.strides[1]==None:
                    self.strides[0] = self.size[0]
                    self.strides[1] = self.size[1]
                    self.offset_x = Images.shape[1]%self.size[0]
                    self.offset_y = Images.shape[2]%self.size[1]
                    padded_images = list(map(self.__padding_op, Images))
                                         
                elif self.strides[0]==None and self.strides[1]!=None:   
                    self.strides[0] = self.size[0]
                    self.offset_x = Images.shape[1]%self.size[0]
                    if self.strides[1] <= Images.shape[2]:
                        self.offset_y = self.__offset_op(Images.shape[2], self.size[1], self.strides[1])
                    else:
                        raise Exception("stride_y must be between {0} and {1}".format(1,Images.shape[2]))
                    padded_images = list(map(self.__padding_op, Images))

                elif self.strides[0]!=None and self.strides[1]==None:   
                    self.strides[1] = self.size[1]
                    self.offset_y = Images.shape[2]%self.size[1]
                    if self.strides[0] <=Images.shape[1]:
                        self.offset_x = self.__offset_op(Images.shape[1], self.size[0], self.strides[0])
                    else:
                        raise Exception("stride_x must be between {0} and {1}".format(1,Images.shape[1]))
                    padded_images = list(map(self.__padding_op, Images))
                                         
                else:
                    if self.strides[0] > Images.shape[1]:
                        raise Exception("stride_x must be between {0} and {1}".format(1,Images.shape[1]))
                    
                    elif self.strides[1] > Images.shape[2]:
                        raise Exception("stride_y must be between {0} and {1}".format(1,Images.shape[2]))
                        
                    else:
                        self.offset_x = self.__offset_op(Images.shape[1], self.size[0], self.strides[0])
                        self.offset_y = self.__offset_op(Images.shape[2], self.size[1], self.strides[1])
                        padded_images = list(map(self.__padding_op, Images))

                for i, Image in enumerate(padded_images):
                    transformed_images[str(i)] = self.__convolution_op(Image)

            else:
                if self.strides[0]==None and self.strides[1]==None:
                    self.strides[0] = self.size[0]
                    self.strides[1] = self.size[1]

                elif self.strides[0]==None and self.strides[1]!=None:
                    if self.strides[1] > Images.shape[2]:
                        raise Exception("stride_y must be between {0} and {1}".format(1,Images.shape[2]))                 
                    self.strides[0] = self.size[0]

                elif self.strides[0]!=None and self.strides[1]==None:
                    if self.strides[0] > Images.shape[1]:
                        raise Exception("stride_x must be between {0} and {1}".format(1,Images.shape[1]))              
                    self.strides[1] = self.size[1]
                else:
                    if self.strides[0] > Images.shape[1]:
                        raise Exception("stride_x must be between {0} and {1}".format(1,Images.shape[1]))                    
                    elif self.strides[1] > Images.shape[2]:
                        raise Exception("stride_y must be between {0} and {1}".format(1,Images.shape[2]))
                                         
                for i, Image in enumerate(Images):
                    transformed_images[str(i)] = self.__convolution_op(Image)

            return transformed_images
        
    def save_images(self,transformed, save_dir):
        if not(os.path.exists(save_dir)):
            raise Exception("Path does not exist!")
        else:
            for key, val in transformed.items():
                path = os.path.join(save_dir, key)
                os.mkdir(path)
                for i, j in enumerate(val):
                    plt.imsave(os.path.join(path, str(i+1)+'.png'), j)
