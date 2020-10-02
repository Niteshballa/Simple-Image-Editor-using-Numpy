#import numpy and pillow
from PIL import Image
import numpy as np

#read image path
file=None
img=input("Enter the image path : (Just enter name if it is in same folder) ")
folders=img.split('\\')
fn=folders[-1][:-4]
try:
    file=Image.open(img)
except (OSError, IOError) as e:
    print("File not Found in the given path")
if file:
    choice=0
    ext=img[-3:]
#open image with numpy and PIL
    im=np.array(file)
    while choice!=6:
        print("\nEnter the choice : \n Rotate right --> 1\n Rotate left --> 2\n Flip --> 3\n Positive inversion --> 4\n Increase brightness --> 5\n Save and exit 6")
        choice=int(input())
        if choice == 1 :
            im=np.rot90(im,1)
        elif choice == 2 :
            im=np.rot90(im,3)
        elif choice == 3 :
            im=np.flipud(im)
        elif choice == 4 :
            mask=np.full(im.shape,255)
            im=mask-im
        elif choice == 5 :
            mask=np.full(im.shape,255)
            im=255.0 * (im / 255.0)**2.2
        elif choice == 6 :
            op = Image.fromarray((im).astype(np.uint8))        
            op.save('{}_edited.{}'.format(fn,ext))
            op.show()

    
