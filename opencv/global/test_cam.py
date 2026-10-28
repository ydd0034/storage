import cv2

# DSHOW 백엔드로 0번 카메라 시도
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("DSHOW로 0번 카메라를 열 수 없습니다.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FPS, 30)

width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps    = cap.get(cv2.CAP_PROP_FPS)
print(f"Actual resolution (DSHOW): {width} x {height}, FPS: {fps}")

while True:
    ret, frame = cap.read()
    if not ret:
        print("DSHOW: 프레임을 읽을 수 없습니다.")
        break

    cv2.imshow("Camera Test DSHOW (press q to quit)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()