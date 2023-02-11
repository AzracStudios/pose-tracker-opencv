def draw_face(mp_drawing, mp_holistic, tracking_img, results):
    mp_drawing.draw_landmarks(
        tracking_img, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
        mp_drawing.DrawingSpec(color=(255, 255, 255),
                               thickness=1,
                               circle_radius=0),
        mp_drawing.DrawingSpec(color=(255, 255, 255),
                               thickness=1,
                               circle_radius=2))