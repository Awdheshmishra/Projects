import cv2
import mediapipe as mp
import numpy as np
import math
import winsound   # 🔊 Windows sound

# ---------------- CONFIG ----------------
DOWN_ANGLE = 95
UP_ANGLE = 165
SHOULDER_MOVE = 0.012
HIP_ALIGN = 0.30
BEEP_FREQ = 1200      # sound frequency
BEEP_TIME = 400       # milliseconds
# ----------------------------------------

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

count = 0
stage = "up"
down_shoulder_y = 0


def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    angle = math.degrees(
        math.atan2(c[1]-b[1], c[0]-b[0]) -
        math.atan2(a[1]-b[1], a[0]-b[0])
    )
    angle = abs(angle)
    if angle > 180:
        angle = 360 - angle
    return angle


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)

    if result.pose_landmarks:
        lm = result.pose_landmarks.landmark

        shoulder = [lm[mp_pose.PoseLandmark.LEFT_SHOULDER].x,
                    lm[mp_pose.PoseLandmark.LEFT_SHOULDER].y]
        elbow = [lm[mp_pose.PoseLandmark.LEFT_ELBOW].x,
                 lm[mp_pose.PoseLandmark.LEFT_ELBOW].y]
        wrist = [lm[mp_pose.PoseLandmark.LEFT_WRIST].x,
                 lm[mp_pose.PoseLandmark.LEFT_WRIST].y]
        hip = [lm[mp_pose.PoseLandmark.LEFT_HIP].x,
               lm[mp_pose.PoseLandmark.LEFT_HIP].y]

        elbow_angle = calculate_angle(shoulder, elbow, wrist)

        # ---------- DOWN ----------
        if elbow_angle < DOWN_ANGLE and stage == "up":
            down_shoulder_y = shoulder[1]
            stage = "down"

        # ---------- UP + CHECK ----------
        if elbow_angle > UP_ANGLE and stage == "down":
            shoulder_movement = down_shoulder_y - shoulder[1]
            body_straight = abs(shoulder[1] - hip[1])

            # ✅ VALID PUSH-UP
            if shoulder_movement > SHOULDER_MOVE and body_straight < HIP_ALIGN:
                count += 1

            # ❌ WRONG FORM → SOUND
            else:
                winsound.Beep(BEEP_FREQ, BEEP_TIME)

            stage = "up"

        # DEBUG TEXT
        cv2.putText(frame, f"Angle: {int(elbow_angle)}",
                    (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
        cv2.putText(frame, f"Move: {round(down_shoulder_y - shoulder[1], 3)}",
                    (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

        mp_draw.draw_landmarks(frame, result.pose_landmarks,
                               mp_pose.POSE_CONNECTIONS)

    cv2.putText(frame, f"Push-ups: {count}",
                (30, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0,255,0), 3)

    cv2.imshow("Smart Push-up Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
