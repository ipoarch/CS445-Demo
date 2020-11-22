from sklearn.decomposition import NMF
# import song_importer as s
import image_importer as i
import numpy as np
import os

# s.decompose_song('sounds/test.wav')

for filename in os.listdir('european-flood-2013_imgs_small/imgs_small/')[:]:
    every_pixel = np.empty([1, 3])
    decomp = i.decompose_img(os.path.join('european-flood-2013_imgs_small/imgs_small/', filename))
    every_pixel = np.append(every_pixel, decomp[0], axis=0)

    model = NMF(n_components=2, init='random', random_state=0)
    # model = NMF(n_components=2, init='random', random_state=0, l1_ratio=1)
    l1 = False
    W = model.fit_transform(every_pixel[1:])
    H = model.components_

    print(W)
    print(H)
    # print(decomp[0])
    # print(decomp[1])
    # print(decomp[2])
    # print(filename)

    # i.make_image(filename, W, H, decomp[1], decomp[2], mode="parts", l1r=l1)
    i.make_image(filename, W, H, decomp[1], decomp[2], mode="parts2", l1r=l1)
    # i.make_image(filename, W, H, decomp[1], decomp[2], l1r=l1)