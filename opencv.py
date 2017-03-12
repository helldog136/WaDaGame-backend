import cv2
import numpy as np
import math


def scaleRectangle(rect, scale):
    output = []
    for point in rect:
        output.append(np.array([point[0][0] * scale, point[0][1] * scale]))
    return output


def findRectangle(src):
    ratio = 600.0 / max(src.shape[1], src.shape[0])
    downscaledSize = int(src.shape[1] * ratio), int(src.shape[0] * ratio)
    downscaled = cv2.resize(src, downscaledSize)

    rectangles = findRectangles(downscaled)

    if len(rectangles) == 0:
        return

    rectangles = sorted(rectangles, key=cv2.contourArea, reverse=True)
    largestRectangle = rectangles[0]

    result = scaleRectangle(largestRectangle, 1 / ratio);
    return np.array(result)


def findRectangles(src):
    N = 5  # 11 in the original sample.
    CANNY_PARAM1 = 0
    CANNY_PARAM2 = 50
    rectangles = []
    blurred = cv2.medianBlur(src, 9)
    gray0 = np.zeros(blurred.shape[0:2], dtype=np.uint8)
    srcArea = src.shape[0] * src.shape[1]
    for c in range(3):
        cv2.mixChannels([blurred], [gray0], [c, 0])
        for l in range(N):
            if l == 0:
                gray = cv2.Canny(gray0, CANNY_PARAM1, CANNY_PARAM2);
                # Dilate Canny output to remove potential holes between edge segments.
                gray = cv2.dilate(gray, np.ones((3, 3)))
            else:
                threshold = int((l + 1) * 255 / N);
                _, gray = cv2.threshold(gray0, threshold, 255, cv2.THRESH_BINARY)
            val = cv2.findContours(gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if len(val) == 2:
                contours, hierarchy = val
            else:
                im2, contours, hierarchy = val

            for contour in contours:
                arcLen = cv2.arcLength(contour, True) * 0.02
                # Approximate polygonal curves.
                approx = cv2.approxPolyDP(contour, arcLen, True)

                if (isRectangle(approx, srcArea)):
                    rectangles.append(approx)
    return rectangles


# ~ def angle(p1, p2, p0):
# ~ print(p1, p2, p0)
# ~ dx1 = p1[0][0] - p0[0][0]
# ~ dy1 = p1[0][1] - p0[0][1]
# ~ dx2 = p2[0][0] - p0[0][0]
# ~ dy2 = p2[0][1] - p0[0][1]
# ~ sqr = (dx1 * dx1 + dy1 * dy1) * (dx2 * dx2 + dy2 * dy2) + 1e-10
# ~ print(sqr)
# ~ return (dx1 * dx2 + dy1 * dy2) / math.sqrt(sqr)

def isRectangle(polygon, srcArea):
    if len(polygon) != 4:
        return False

    area = abs(cv2.contourArea(polygon))

    if area < srcArea * 0.10 or area > srcArea * 0.95:
        return False

    if not cv2.isContourConvex(polygon):
        return False

    # Check if the all angles are more than 72.54 degrees (cos 0.3).
    maxCosine = 0

    # ~ for i in range(2, 5) :
    # ~ cosine = abs(angle(polygon[i % 4], polygon[i - 2], polygon[i - 1]))
    # ~ maxCosine = max(cosine, maxCosine)

    # ~ if (maxCosine >= 0.3):
    # ~ return False

    return True


def sortRect(rectangle):
    """
    :param rectangle: the rectangle (box points) from which we will sort the corners
    :type rectangle: np.array
    :return: the sorted corners of the rectangle ( [NW, NE, SW, SE] )
    :rtype: list
    """
    ordered_corners = []
    rect = rectangle.reshape(4, 2)
    rect = rect[
        np.lexsort((rect[:, 0], rect[:, 1]))]  # The contours are now ordered following the y-axis
    # We take the two topmost points and we order it following the x-axis
    ordered_corners.extend(rect[0:2][np.lexsort((rect[0:2][:, 1], rect[0:2][:, 0]))])
    # Now we take the two other points and we order it following the x-axis
    ordered_corners.extend(rect[-2:][np.lexsort((rect[-2:][:, 1], rect[-2:][:, 0]))])
    # At this point, ordered contains [NW, NE, SW, SE]
    return ordered_corners


def extractScreen(imgPath):
    img = cv2.imread(imgPath)
    img = cv2.resize(img, (img.shape[1] // 4, img.shape[0] // 4))

    rect = findRectangle(img)
    rect = np.array(rect).reshape((-1, 1, 2)).astype(np.int32)

    rect = sortRect(rect)
    diff_x = rect[1][0] - rect[0][0]
    diff_y = rect[3][1] - rect[1][1]

    pts1 = np.float32(rect)
    pts2 = np.float32([[0, 0], [diff_x, 0], [0, diff_y], [diff_x, diff_y]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (diff_x, diff_y))
    cv2.imwrite(imgPath, dst)
    print "Screen Extracted!"

