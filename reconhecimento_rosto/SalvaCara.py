import cv2
import face_recognition
import pickle

def save_face_encodings(encodings, filename='face_encodings.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(encodings, f)

def main():
    cap = cv2.VideoCapture(0)
    encodings = []

    print("Prepare to register your face. Press 'q' to finish.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        if face_encodings:
            encodings.extend(face_encodings)

        # Mostrar o frame
        cv2.imshow('Frame', frame)

        # Salvar descritores faciais ao pressionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if encodings:
        save_face_encodings(encodings)
        print("Face encodings saved.")
    else:
        print("No face encodings found.")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
