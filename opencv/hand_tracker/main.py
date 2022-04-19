"""
Source https://tproger.ru/articles/pishem-sistemu-raspoznavanija-ladoni-na-python-opencv/

NOTE: not properly work under wayland
"""
import cv2
import mediapipe as mp

def main():
    camera = cv2.VideoCapture(0)
    hands = mp.solutions.hands.Hands(max_num_hands=1)
    draw = mp.solutions.drawing_utils

    while True:
        # If ESC key is pressed
        #if cv2.cvWaitKey(1) & 0xFF == 27:
        #    break

        ok, image = camera.read()
        #image = cv2.flip(image, -1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        resuls = hands.process(image_rgb)

        if resuls.multi_hand_landmarks:
            for hand_landmarks in resuls.multi_hand_landmarks:
                #for _id, landmark in enumerate(hand_landmarks.landmark):
                #    h, w, c = image.shape
                #    cx, cy = int(landmark.x * w), int(lm.y * h)
                draw.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            cv2.imshow("Hand", image)


if __name__ == "__main__":
    main()
