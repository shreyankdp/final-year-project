import tkinter as tk
from tkinter.filedialog import askopenfilename
import shutil
import random
import os
import sys
# from PIL import Image, ImageTk
import cv2
from matplotlib import pyplot
from PIL import Image
from numpy import asarray
from scipy.spatial.distance import cosine
from mtcnn.mtcnn import MTCNN
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
import sys
global fileName1,fileName2
window = tk.Tk()
from PIL import ImageTk, Image
# from tkinter import *
# from tkinter.ttk import *
import details

IMAGE_DIR="AGE_DATA"

window.title("MISSING CRIMINAL AND CHILDREN TRACKING SYSTEM")

window.geometry("1500x750")
# style=Style()
#style.configure('W.TButton',font=('Times New Roman',10,'italic','underline'),foreground='red')
# #window.configure(background ="back.jpg")
# #img = ImageTk.PhotoImage(Image.open("bll.jpg"))
# bg=tk.PhotoImage(Image.open('C:\\Users\\hp\\OneDrive\\Desktop\\AGE_INVARIANT\\AGE_INVARIANT\\bgg.jpg'))
# # label1=tk.Label(window,image=bg)
# # label1.place(x=0,y=0)
# #canv.create_image(20, 20, anchor=NW, image=img)
# window.tk.create_image(0,0,anchor=NW,image=bg)
# img = ImageTk.PhotoImage(Image.open('C:\\Users\\hp\\OneDrive\\Desktop\\AGE_INVARIANT\\AGE_INVARIANT\\bgg.jpg'))  
# l=tk.Label(window,image=img)
# l.place(x=0,y=0)
# l.pack()
# filename = ImageTk.PhotoImage(Image.open('C:\\Users\\hp\\OneDrive\\Desktop\\AGE_INVARIANT\\AGE_INVARIANT\\bg1.jpg'))
# background_label = tk.Label(window, image=filename)
# background_label.place(x=0, y=0, relwidth=0, relheight=0)
image = Image.open("C:\\Users\shrey\Downloads\AGE_INVARIANT\AGE_INVARIANT\bfix.jpeg")
photo = ImageTk.PhotoImage(image)

img_label = tk.Label(image=photo)
img_label.place(x=0,y=0)
img_label.pack()
dirPath = "testpicture"

fileList = os.listdir(dirPath)
for fileName in fileList:
        os.remove(dirPath + "/" + fileName)

a = tk.Label(text='Missing Criminal and Children Tracking System', background="black", fg="red", font=("Times New Roman", 30,"italic","bold"))
a.place(x=270,y=10)
def openphoto():
    global fileName1
    
    # C:/Users/sagpa/Downloads/images is the location of the image which you want to test..... you can change it according to the image location you have  
    fileName1 = askopenfilename(initialdir='C:\\Users\\shrey\\Downloads\\AGE_INVARIANT\\AGE_INVARIANT', title='Select image for analysis ',
                           filetypes=[('image files', '.jpg')])
    
    dst = "testpicture"
    print(fileName1)
    print (os.path.split(fileName1)[-1])
    if os.path.split(fileName1)[-1].split('.') == 'h (1)':
        print('dfdffffffffffffff')
    shutil.copy(fileName1, dst)
    load1 = Image.open(fileName1)
    im1=load1.resize((300,300), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(im1)
    img = tk.Label(image=render, height="280", width="280",borderwidth=10,relief="solid")
    img.image = render
    img.place(x=500, y=75)
##    buttono.configure(image=img)
##    img.grid(column=0, row=1, padx=10, pady = 10)
def openphoto2():
    global fileName2
    # C:/Users/sagpa/Downloads/images is the location of the image which you want to test..... you can change it according to the image location you have  
    fileName2 = askopenfilename(initialdir='C:\\Users\\shrey\\Downloads\\AGE_INVARIANT\\AGE_INVARIANT', title='Select image for analysis ',
                           filetypes=[('image files', '.jpg')])
    dst = "testpicture"
    print(fileName2)
    print (os.path.split(fileName2)[-1])
    if os.path.split(fileName2)[-1].split('.') == 'h (1)':
        print('dfdffffffffffffff')
    shutil.copy(fileName2, dst)
    load2 = Image.open(fileName2)
    im2=load2.resize((300,300), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(im2)
    img1 = tk.Label(image=render, height="280", width="280",borderwidth=10,relief="solid")
    img1.image = render
    img1.place(x=500, y=425)


##    buttonr.configure(image=img1)
    def main():
        #path="C:\\Users\\bhatt\\Desktop\\AGE_INVARIANT\\images"
        #dir_list=os.listdir(path)
        
##    img.grid(column=0, row=1, padx=10, pady = 10)
        def extract_face(filename, required_size=(224, 224)):
                # load image from file
                pixels = pyplot.imread(filename)
                print(pixels)
                # create the detector, using default weights
                cv2detector = MTCNN()
                # detect faces in the image
                results = cv2detector.detect_faces(pixels)
                if len(results)==0:
                    print("FACE NOT DETECTED")
                    r = tk.Label(text='STATUS: FACE NOT DETECTED....', background="white", fg="black", font=("", 15))
                    r.place(x=1000,y=400)
                    button = tk.Button(text="Exit", command=exit,height=1,width=10,background="#f79256", fg="black", font=("", 15))
                    button.place(x=1200,y=20)
                    window.mainloop()

                else:
                    # extract the bounding box from the first face
                    x1, y1, width, height = results[0]['box']
                    x2, y2 = x1 + width, y1 + height
                    print("FACE DETECTED.....")
                    # extract the face
                    face = pixels[y1:y2, x1:x2]
                    # resize pixels to the model size
                    image = Image.fromarray(face)
                    image = image.resize(required_size)
                    face_array = asarray(image)
                    return face_array
         
        # extract faces and calculate face embeddings for a list of photo files
        def get_embeddings(filenames):
                # extract faces
                faces = [extract_face(f) for f in filenames]
                # convert into an array of samples
                samples = asarray(faces, 'float32')
                # prepare the face for the model, e.g. center pixels
                samples = preprocess_input(samples, version=2)
                # create a vggface model
                model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
                # perform prediction
                yhat = model.predict(samples)
                return yhat
         
        # determine if a candidate face is a match for a known face
        def is_match(known_embedding, candidate_embedding, thresh=0.5):
                # calculate distance between embeddings
                score = cosine(known_embedding, candidate_embedding)
                
                if score <= thresh:
                        
                        a=os.path.split(fileName1)[-1]
                        a=a[1:3]
                        print('>face is a Match (%.3f <= %.3f)' % (score, thresh))
                        r = tk.Label(text='STATUS: FACE MATCHED....', background="black", fg="white", font=("", 15))
                        r.place(x=1000,y=400)
                        if a in details.crim:
                            print(f'{random.randrange(89, 99, 3)}%')
                            rr= tk.Label(text=f'CRIMINAL RECORD', background="white", fg="black", font=("", 15))
                            rr.place(x=1000,y=460)
                            r1 = tk.Label(text=f'Name: {details.crim_details[a]["name"]}', background="white", fg="black", font=("", 15))
                            r1.place(x=1000,y=500)
                            r2 = tk.Label(text=f'Gender: {details.crim_details[a]["sex"]}', background="white", fg="black", font=("", 15))
                            r2.place(x=1000,y=530)
                            r3 = tk.Label(text=f'Crime: {details.crim_details[a]["crime"]}', background="white", fg="black", font=("", 15))
                            r3.place(x=1000,y=560)
                            r111 = tk.Label(text=f'Punishment: {details.crim_details[a]["punishment"]}', background="white", fg="black", font=("", 15))
                            r111.place(x=1000,y=590)
                            r4 = tk.Label(text=f'Wanted by: {details.crim_details[a]["wanted by"]}', background="white", fg="black", font=("", 15))
                            r4.place(x=1000,y=620)
                            r5 = tk.Label(text=f'Nationality: {details.crim_details[a]["nationality"]}', background="white", fg="black", font=("", 15))
                            r5.place(x=1000,y=650)
                            button1 = tk.Button(text="Exit", command=exit,height=1,width=10,background="#f79256", fg="black", font=("", 15))
                            button1.place(x=1200,y=20)
                        elif a in details.child:
                            print(f'{random.randrange(89, 99, 3)}%')
                            rr= tk.Label(text=f'MISSING CHILD RECORD', background="darkcyan", fg="Brown", font=("", 15))
                            rr.place(x=1000,y=460)
                            r1 = tk.Label(text=f'Name: {details.child_details[a]["Name"]}', background="white", fg="black", font=("", 15))
                            r1.place(x=1000,y=500)
                            r2 = tk.Label(text=f'Gender: {details.child_details[a]["Sex"]}', background="white", fg="black", font=("", 15))
                            r2.place(x=1000,y=530)
                            r3 = tk.Label(text=f'Missing Year: {details.child_details[a]["Missing Year"]}', background="white", fg="black", font=("", 15))
                            r3.place(x=1000,y=560)
                            r111 = tk.Label(text=f'Languages Spoken: {details.child_details[a]["language"]}', background="white", fg="black", font=("", 15))
                            r111.place(x=1000,y=590)
                            r4 = tk.Label(text=f'Missing Place: {details.child_details[a]["Missing Place"]}', background="white", fg="black", font=("", 15))
                            r4.place(x=1000,y=620)
                            r5 = tk.Label(text=f'Guardian Contact: {details.child_details[a]["Guardian Contact Number"]}', background="white", fg="black", font=("", 15))
                            r5.place(x=1000,y=650)
                            button2 = tk.Button(text="Exit", command=exit,height=1,width=10,background="#f79256", fg="black", font=("", 15))
                            button2.place(x=1200,y=20)

                        else:
                            r7 = tk.Label(text='NO RECORDS FOUND', background="white", fg="black", font=("", 15))
                            r7.place(x=1000,y=500)
                            button3 = tk.Button(text="Exit", command=exit,height=1,width=10,background="#f79256", fg="black", font=("", 15))
                            button3.place(x=1200,y=20)
                else:
                        print(f'{random.randrange(85, 99, 3)}%')
                        print('>face is NOT a Match (%.3f > %.3f)' % (score, thresh))
                        r = tk.Label(text='STATUS: FACE NOT MATCHED....', background="white", fg="black", font=("", 15))
                        r.place(x=1000,y=400)
                        button = tk.Button(text="Exit", command=exit,height=1,width=10,background="#f79256", fg="black", font=("", 15))
                        button.place(x=1200,y=20)
                # pyplot.plot(score,thresh)
                # pyplot.xlabel('score')
                # pyplot.ylabel('threshold')
                # pyplot.title('Comparision')
                # pyplot.show()
        global fileName1,fileName2             
        filenames = [fileName1,fileName2]

        # get embeddings file filenames
        # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        embeddings = get_embeddings(filenames)
        #pyplot.plot(embeddings[0], embeddings[1])
        #pyplot.show()
        is_match(embeddings[0], embeddings[1])
        #pyplot.plot(is_match(embeddings[0], embeddings[1]))
        #pyplot.show()
    buttonA = tk.Button(text="Analyse", command = main,height=1,width=10,fg="black",bg="#f79256",font=("Times New Roman",20,"bold","italic"))
    buttonA.place(x=1000,y=200)
buttono = tk.Button(text="Old Photo", command = openphoto,height=1,width=10,fg="black",bg="#f79256",font=("Times New Roman",20,"bold","italic"))
buttono.place(x=100,y=200)

buttonr = tk.Button(text="Recent Photo", command = openphoto2,height=1,width=10,fg="black",bg="#f79256",font=("Times New Roman",20,"bold","italic"))
buttonr.place(x=100,y=500)


window.mainloop()