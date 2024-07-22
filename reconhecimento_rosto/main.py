import cv2
import face_recognition
import pickle

def load_face_encodings(filename='face_encodings.pkl'):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def main():
    cap = cv2.VideoCapture(0)
    known_encodings = load_face_encodings()
    print("Loaded face encodings.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"

            if True in matches:
                name = "Face recognized!"

            # Desenhar o retângulo e o texto
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Mostrar o frame
        cv2.imshow('Frame', frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
