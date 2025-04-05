import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error: Unable to access webcam")
    exit()

# Adjusted HSV ranges
colors = {
    "Pink": ([140, 50, 100], [170, 255, 255], (180, 105, 255)),      # Pink (hot pink)
    "Yellow": ([20, 120, 120], [35, 255, 255], (0, 255, 255)),       # Bright yellow
    "Orange": ([5, 140, 140], [18, 255, 255], (0, 140, 255))  # Refined orange hue         # True orange
}
kernel = np.ones((5, 5), "uint8")

def bgr_to_hex(bgr):
    return '#{:02x}{:02x}{:02x}'.format(bgr[2], bgr[1], bgr[0])

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame")
        break
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    hsvFrame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    color_counts = {color: 0 for color in colors}
    total_count = 0

    for color_name, (lower, upper, bgr_color) in colors.items():
        lower = np.array(lower, np.uint8)
        upper = np.array(upper, np.uint8)
        mask = cv2.inRange(hsvFrame, lower, upper)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.dilate(mask, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)
            circularity = 4 * np.pi * (area / (perimeter ** 2 + 1e-6))

            if area > 250 and 0.6 <= circularity <= 1.3:
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)
                cv2.circle(frame, center, radius, bgr_color, 2)

                hex_color = bgr_to_hex(bgr_color)
                label = f"{color_name} ({hex_color})"
                cv2.putText(frame, label, (center[0] - 50, center[1] - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, bgr_color, 2)

                color_counts[color_name] += 1
                total_count += 1

    # Top right count display
    y_offset = 30
    for color_name, count in color_counts.items():
        bgr_color = colors[color_name][2]
        text = f"{color_name}: {count}"
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
        cv2.putText(frame, text, (frame.shape[1] - text_size[0] - 10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, bgr_color, 2)
        y_offset += 25

    total_text = f"Total: {total_count}"
    total_size = cv2.getTextSize(total_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
    cv2.putText(frame, total_text, (frame.shape[1] - total_size[0] - 10, y_offset + 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow('Enhanced Ball Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
