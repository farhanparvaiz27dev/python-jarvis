import cv2

def AuthenticateFace():
    # Local Binary Patterns Histograms recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('engine\\auth\\trainer\\trainer.yml')  # load trained model
    cascadePath = "engine\\auth\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX
    names = ['', 'Farhan']  # leave index 0 empty

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to read from camera.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        flag = 0  # reset each loop

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, accuracy = recognizer.predict(gray[y:y + h, x:x + w])

            if accuracy < 100:
                id = names[id]
                accuracy_text = f"{round(100 - accuracy)}%"
                flag = 1
            else:
                id = "unknown"
                accuracy_text = f"{round(100 - accuracy)}%"

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy_text), (x + 5, y + h - 5),
                        font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:  # ESC pressed
            print("ESC pressed. Retrying face authentication...")
            continue  # retry authentication

        if flag == 1:
            cam.release()
            cv2.destroyAllWindows()
            return 1  # recognized

    cam.release()
    cv2.destroyAllWindows()
    return 0  # not recognized
