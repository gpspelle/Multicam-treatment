import os
import cv2
import glob
import numpy as np

g = np.zeros((24, 2), dtype='int32')

g[0] = [1080, 1108]
g[1] = [375, 399]
g[2] = [591, 625]
g[3] = [288, 314]
g[4] = [311, 336]
g[5] = [583, 629]
g[6] = [476, 507]
g[7] = [271, 298]
g[8] = [628, 651]
g[9] = [512, 530]
g[10] = [464, 489]
g[11] = [605, 653]
g[12] = [823, 863]
g[13] = [989, 1023]
g[14] = [755, 787]
g[15] = [891, 940]
g[16] = [730, 770]
g[17] = [571, 601]
g[18] = [499, 600]
g[19] = [545, 672]
g[20] = [864, 901]
g[21] = [767, 808]
g[22] = [-1, -1]
g[23] = [-1, -1]

i = np.zeros((24, 2), dtype='int32')

i[0] = [874, 1285]
i[1] = [308, 600]
i[2] = [380, 784]
i[3] = [230, 780]
i[4] = [288, 450]
i[5] = [325, 750]
i[6] = [330, 680]
i[7] = [144, 380]
i[8] = [310, 760]
i[9] = [315, 680]
i[10] = [378, 600]
i[11] = [355, 770]
i[12] = [301, 960]
i[13] = [372, 1115]
i[14] = [363, 870]
i[15] = [380, 1000]
i[16] = [251, 860]
i[17] = [301, 740]
i[18] = [255, 770]
i[19] = [301, 800]
i[20] = [408, 1040]
i[21] = [317, 930]
i[22] = [393, 5200]
i[23] = [350, 3500]

scenarios = ['./chute{:02}'.format(i) for i in range(1,25)]
scenarios.sort()
for s in range(len(scenarios)):
    print(s)
    videos = glob.glob(scenarios[s] + '/*.avi')

    videos.sort()
    for v in range(len(videos)):

        new_v = videos[v].replace("/", "")
        new_v = new_v.replace(".", "")
        new_v = new_v[:-3]
        os.makedirs('Falls/' + new_v)
        os.makedirs('NotFalls/' + new_v + '_00')
        os.makedirs('NotFalls/' + new_v + '_01')

        os.rename(videos[v], 'trash.avi')
        cap = cv2.VideoCapture('trash.avi')
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        fall = cv2.VideoWriter('Falls/' + new_v + '/' + new_v + '.avi', cv2.VideoWriter_fourcc('X','V','I','D'), fps, (width, height))
        not_fall_0 = cv2.VideoWriter('NotFalls/' + new_v + '_00/' + new_v + '_00.avi', cv2.VideoWriter_fourcc('X','V','I','D'), fps, (width, height))
        not_fall_1 = cv2.VideoWriter('NotFalls/' + new_v + '_01/' + new_v + '_01.avi', cv2.VideoWriter_fourcc('X','V','I','D'), fps, (width, height))
        count = 0
        while True:

            ret, frame = cap.read()

            if not ret:
    #            print("TERMINEI UM VIDEO")
                break

            if count < i[s][0]:
     #           print("AINDA NAO COMECEI")
                count += 1 
                continue
            
            if count > i[s][1]:
      #          print("ACABOU O VIDEO")
                count += 1
                break
            
            if count < g[s][0]: 
       #         print("ADL ANTES DE FALL")
                not_fall_0.write(frame)
            elif count > g[s][1]:
        #        print("ADL DEPOIS DE FALL")
                not_fall_1.write(frame)
            else:
         #       print("FALL")
                fall.write(frame)

            count += 1 

        cap.release()
        not_fall_1.release()
        not_fall_0.release()
        fall.release()
