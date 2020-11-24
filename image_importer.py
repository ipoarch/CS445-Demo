from PIL import Image, ImageOps
import numpy as np

def decompose_img(filename):
    with Image.open(filename, 'r') as f:
        picture_rgb = np.asarray(list(f.getdata()))
        # print(picture_rgb)
        return np.array([picture_rgb, f.size[0], f.size[1]], dtype='object')

def make_image(filename, W, H, width, height, mode="reconstructed", l1r=False, model="NMF"):
    if (mode == "parts"):
        new_pixels = np.empty([1, 3])
        count = 0
        for w in W:
            count = count + 1
            if (w[0] > w[1]):
                new_pixels = np.append(new_pixels, [np.array([0, 0, 250])], axis=0)
            else:
                new_pixels = np.append(new_pixels, [np.array([250, 0, 0])], axis=0)
        new_pixels = new_pixels[1:].astype('i')
        itr = tuple(map(tuple, new_pixels))
    elif (mode == "parts2"):
        new_pixels = np.empty([1, 3])
        count = 0
        for w in W:
            count = count + 1
            if (w[0] > w[1]):
                new_pixels = np.append(new_pixels, [H[0] * 250 / max(H[0])], axis=0)
            else:
                new_pixels = np.append(new_pixels, [H[1] * 250 / max(H[1])], axis=0)
        new_pixels = new_pixels[1:].astype('i')
        itr = tuple(map(tuple, new_pixels))
    else:
        itr = tuple(map(tuple, np.matmul(W, H).astype('i')))

    if l1r:
        prefix = "l1"
    else:
        prefix = ""

    # print(len(new_pixels))
    # print(width * height)

    count = 0
    with Image.new('RGB', (height, width), "white") as f:
        pixels = f.load()
        for i in range(height):
            for j in range(width):
                # print(itr[count])
                pixels[i, j] = itr[count]
                count = count + 1

        # f.show()
        f = f.rotate(-90, expand=True)
        f = ImageOps.mirror(f)
        f.save("generated/" + model + "_" + prefix + "_" + mode + "_" + filename, "JPEG")