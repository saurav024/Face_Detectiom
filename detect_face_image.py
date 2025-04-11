import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def process_image():
    # Read the input image
    img = cv2.imread('test.jpg')

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_video():
    # Capture video from webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read the frame
        ret, img = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the output
        cv2.imshow('Video', img)

        # Stop if escape key is pressed
        if cv2.waitKey(30) & 0xFF == 27:
            break

    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()

def main():
    print("Choose an option:")
    print("1. Process Image")
    print("2. Process Video")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        process_image()
    elif choice == '2':
        process_video()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
