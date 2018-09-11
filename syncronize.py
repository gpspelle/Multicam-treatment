import os
import cv2
import glob
scenarios = ['./chute{:02}'.format(i) for i in range(1,25)]
scenarios.sort()

for s in scenarios:
    print(s)
    videos = glob.glob(s + '/*.avi')

    videos.sort()
    videos_len = [0] * len(videos)
    for v in range(len(videos)):
        print(v)
        cap = cv2.VideoCapture(videos[v])
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        videos_len[v] = length
        cap.release()

    print(videos_len)
    minimo = min(videos_len)

    for v in range(len(videos_len)):
        videos_len[v] -= minimo

    print(videos_len)

    for v in range(len(videos)):
        print(v)
        os.rename(videos[v], 'trash.avi')
        cap = cv2.VideoCapture('trash.avi')
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        out = cv2.VideoWriter(videos[v], cv2.VideoWriter_fourcc('X','V','I','D'), fps, (width, height))
        count = 0
        while True:

            ret, frame = cap.read()

            if not ret:
                break

            if count < videos_len[v]:
                count += 1 
                continue
            
            out.write(frame)
            count += 1 

        cap.release()
        out.release()
