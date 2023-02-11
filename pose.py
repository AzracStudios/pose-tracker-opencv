def draw_pose(mp_drawing, mp_holistic, tracking_img, results):
    mp_drawing.draw_landmarks(
        tracking_img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(255, 255, 255),
                               thickness=2,
                               circle_radius=4),
        mp_drawing.DrawingSpec(color=(255, 255, 255),
                               thickness=2,
                               circle_radius=2))
