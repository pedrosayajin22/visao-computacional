Projeto de Reconhecimento Facial com OpenCV e Face Recognition
Este projeto consiste em dois scripts Python para reconhecimento facial utilizando as bibliotecas face_recognition e OpenCV. O objetivo é registrar e reconhecer faces em tempo real usando uma webcam.

Requisitos
Python 3.x
OpenCV
face_recognition
pickle

pip install opencv-python face_recognition



Uso
Registro de Faces
Este script captura descritores faciais e os salva em um arquivo chamado face_encodings.pkl.

Execute o script de registro de faces:

sh
Copiar código
python SalvaCara.py
Posicione seu rosto na frente da webcam. O script capturará e salvará os descritores faciais.

Pressione 'q' para finalizar o registro.

Reconhecimento de Faces
Este script usa os descritores faciais salvos para reconhecer faces em tempo real.

Execute o script de reconhecimento de faces:

sh
Copiar código
python main.py
Posicione seu rosto na frente da webcam. O script tentará reconhecer a face e mostrará uma mensagem se a face for reconhecida.

Pressione 'q' para sair.