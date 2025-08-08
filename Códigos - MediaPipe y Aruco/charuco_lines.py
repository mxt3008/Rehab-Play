

import cv2

ARUCO_DICT = cv2.aruco.DICT_6X6_250

cap = cv2.VideoCapture(0)

def detect_markers(image):
    dictionary = cv2.aruco.getPredefinedDictionary(ARUCO_DICT)
    params = cv2.aruco.DetectorParameters()
    marker_corners, marker_ids, _ = cv2.aruco.detectMarkers(
        image, 
        dictionary, 
        parameters=params)

    if marker_ids is not None:
        for i, corner in enumerate(marker_corners):
            cv2.polylines(image, [corner.astype(int)], 
                          isClosed=True, 
                          color=(0, 255, 0), 
                          thickness=2)
            cX, cY = int(corner[0][:, 0].mean()), int(corner[0][:, 1].mean())
            cv2.putText(image, str(marker_ids[i][0]), 
                        (cX, cY), 
                        cv2.FONT_HERSHEY_SIMPLEX,
                          2, (0, 0, 255), 4)
    return image

while True:
    ret, frame = cap.read()
    if not ret:
        break

    marker_image = detect_markers(frame)
    cv2.imshow('Markers', marker_image)

    if cv2.waitKey(13) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




