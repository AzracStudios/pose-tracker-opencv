def draw_hands(mp_drawing, mp_holistic, tracking_img, results):
    # RIGHT
    mp_drawing.draw_landmarks(
        tracking_img, results.right_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(255, 255, 255),
                               thickness=2,
                               circle_radius=4),
        mp_drawing.DrawingSpec(color=(255, 255, 255),
                               thickness=2,
                               circle_radius=2))

    # LEFT
    mp_drawing.draw_landmarks(
        tracking_img, results.left_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(255, 255, 255),
                               thickness=2,
                               circle_radius=4),
        mp_drawing.DrawingSpec(color=(255, 255, 255),
                               thickness=2,
                               circle_radius=2))