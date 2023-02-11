import mediapipe as mp
import numpy as np
import cv2

from face import draw_face
from hands import draw_hands
from pose import draw_pose

# MEDIAPIPE MODELS
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
mp_drawing.draw_landmarks

# OPENCV
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 360)

to_display = int(input("Track [0=face, 1=hand, 2=pose, 3=all]: "))


def main():
    # INITIATE MODEL
    with mp_holistic.Holistic(min_detection_confidence=0.7,
                              min_tracking_confidence=0.7) as holistic:

        # START CAPTURE
        while cap.isOpened():
            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, c = image.shape
            tracking_img = np.zeros((h, w, 3), np.uint8)

            results = holistic.process(image)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            to_call = []

            # Face
            if to_display == 0 or to_display == 3:
                to_call.append(lambda: draw_face(mp_drawing, mp_holistic,
                                                 tracking_img, results))

            # Hand
            if to_display == 1 or to_display == 3:
                to_call.append(lambda: draw_hands(mp_drawing, mp_holistic,
                                                  tracking_img, results))

            # Pose
            if to_display == 2 or to_display == 3:
                to_call.append(lambda: draw_pose(mp_drawing, mp_holistic,
                                                 tracking_img, results))

            # Call
            for function in to_call:
                function()

            cv2.imshow('Raw', image)
            cv2.imshow('Tracking', tracking_img)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()