from pyzbar.pyzbar import decode

def read_web_cam():
    import cv2.cv2
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        data = 'Nothing Found'
        try:
            obj = decode(frame)
            data = str(obj[0].data)[2:-1]
        except Exception as e: 
            print(e)

        cv2.putText(frame, data, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2)
        cv2.imshow('Show QR', frame)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()

def read_img():
    from PIL import Image
    fileName = input('Enter file path: ')

    obj = decode(Image.open(fileName))
    data = str(obj[0].data)[2:-1]

    print(data)
    input('\nPress any key to exit...')

read_img()
