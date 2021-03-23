import matplotlib.pyplot as plt
from   matplotlib.widgets import Slider, Button
import tkinter
from   tkinter import filedialog, messagebox
from   cv2 import cv2

#membuat window
wx = 12.5     # lebar
wy = 5      # tinggi
wr = wx/wy  # aspect ratio

fig = plt.figure(figsize=(wx, wy))
fig.canvas.set_window_title('Belajar GUI')

# buat area gambar original
a = 0.1/wr ; b = 0.25 ; w = 0.7/wr; h = 0.6
axImg = fig.add_axes([a, b, w, h])
axImg.set_title("Gambar Asli")

# buat area gambar hasil grayscale
axGray = fig.add_axes([w+2*a, b, w, h])
axGray.set_title("Gambar Grayscale")

# buat area gambar hasil threshold
axThr = fig.add_axes([2*w+3*a, b, w, h])
axThr.set_title("Gambar Binary")

# buat tombol buka gambar
openax = plt.axes([a+w/2-0.15/2, 0.1, 0.15, 0.05])
btnop = Button(openax, 'Open Image', color="lightgoldenrodyellow", hovercolor='0.975')

# buat tombol convert gambar
convax = plt.axes([1.5*w+2*a-0.15/2, 0.1, 0.15, 0.05])
btncon = Button(convax, 'Convert Image', color="lightgoldenrodyellow", hovercolor='0.975')

# buat slider
sldax = plt.axes([2.5*w + 3*a - 0.1, 0.1, 0.2, 0.05])
sldthr = Slider(sldax, 'Threshold', 0, 255, 125, color="blue")

#buat fungsi untuk buka gambar

def openimage(event):
    global img
    axImg.axis("off")
    imgFile = filedialog.askopenfilename(initialfile = 'Rover.png')
    img = cv2.cvtColor(cv2.imread(imgFile), cv2.COLOR_BGR2RGB)
    axImg.imshow(img, cmap='gray')
    plt.pause(.001)

#buat fungsi untuk buka gambar
thr_val = sldthr.val

def convimage(event):
    global img0
    try:
        # -- grayscale
        img0 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        axGray.imshow(img0, cmap='gray')
        axGray.axis("off")
        # -- binary
        img1 = cv2.threshold(img0, 128, 255, cv2.THRESH_BINARY)[1]
        axThr.imshow(img1, cmap='gray')
        axThr.axis("off")
        plt.pause(.001)
        print(img1)

    except NameError:
        messagebox.showerror("Error!", "Buka gambar dulu!")

# buat fungsi untuk slider
def update(event):
    thr_val = sldthr.val
    try:
        # -- grayscale
        img1 = cv2.threshold(img0, thr_val, 255, cv2.THRESH_BINARY)[1]
        axThr.imshow(img1, cmap='gray')
        axThr.axis("off")
        plt.pause(.001)
        
    except NameError:
        messagebox.showerror("Error!", "Gray image not found!")


# buat event pada tombol btnop
btnop.on_clicked(openimage)
# buat event pada tombol btncon
btncon.on_clicked(convimage)
# buat event pada slider
sldthr.on_changed(update)

plt.show()
