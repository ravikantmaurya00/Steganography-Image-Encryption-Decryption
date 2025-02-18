# Steganography-Image-Encryption-Decryption
🤫  Whisper Secrets in Pixels 🤫  Ever wanted to hide a message where no one would look? This Python project lets you embed text within images using steganography.  With an easy-to-use GUI, you can encrypt and decrypt messages seamlessly.  Give it a try and discover the art of hiding in plain sight!

## Introduction
This project implements Image Steganography using Python, allowing users to hide a secret message inside an image and retrieve it later. It provides a Graphical User Interface (GUI) built using Tkinter and TtkBootstrap, while image processing is handled using OpenCV.

## Need for this Project
With the increasing need for secure communication, traditional encryption methods alone may not be sufficient to protect sensitive data from cyber threats. Steganography offers a solution by concealing information within digital images, ensuring covert data transmission. This application aims to implement a robust steganographic technique to securely hide and retrieve data in images while maintaining their visual integrity. It will enhance data security, prevent unauthorized access, and provide a reliable method for confidential communication.

## Features
- **Encode Text into Image:** Hide secret messages inside an image.
- **Decode Text from Image:** Extract hidden messages from an image.
- **User-Friendly GUI:** Built with Tkinter and TtkBootstrap for an enhanced UI experience.
- **Supports Various Image Formats:** Works with PNG, JPG, and BMP.
- **Efficient and Secure:** Uses bit manipulation techniques to store data without noticeable distortion.
  
## Technologies Used
- Python (Core Programming Language)
- OpenCV (Image Processing)
- Tkinter & TtkBootstrap (GUI Development)

## Installation
To run this project, follow these steps
- **Install Dependencies**
  - (1.) Installing Opencv Library
        ```pip install opencv-python```
  - (2.) Installing Numpy library
        ```pip install numpy```
  - (3.) Installing tkinter library as tk
        ```pip install tkinter```
  - (4.) Installing ttkbootstrap library as ttk
        ``` pip install ttkbootstrap```
- **Run the Application**
  ```python main.py```

## Usage
- **Encoding a Message:**
  - Click  on **Open Image** to select  an image.
  - Enter the secret message.
  - Enter the passcode.
  - Click the **Encrypt button**.
- **Decoding a Message:**
  - Enter the Passcode to decrypt the secret message.
  - Click the **Decrypt button**.
  - The hidden message will be displayed.

## Screenshots
- **Main Interface**
  ![](https://github.com/ravikantmaurya00/Steganography-Image-Encryption-Decryption/blob/main/ScreenShot/Main%20interface.png)
  
- **Selecting Image and writing the secret message**
  ![](https://github.com/ravikantmaurya00/Steganography-Image-Encryption-Decryption/blob/main/ScreenShot/Selecting%20image%20and%20writing%20secret%20message.png)

- **Encrypting secret message**
  ![](https://github.com/ravikantmaurya00/Steganography-Image-Encryption-Decryption/blob/main/ScreenShot/Encrypting%20message.png)

- **Decrypting the secret message and final output**
  ![](https://github.com/ravikantmaurya00/Steganography-Image-Encryption-Decryption/blob/main/ScreenShot/Decrypting%20message%20and%20final%20output.png)

## Conclusion
- The Image Steganography project successfully implements the technique of hiding secret messages within images using LSB (Least Significant Bit) encoding. By leveraging 
   Python, OpenCV, Tkinter, and TtkBootstrap, the project provides a user-friendly GUI for encoding and decoding hidden text within images.
- This tool enhances data security by allowing covert communication while maintaining the original image’s visual integrity. The integration of OpenCV ensures efficient 
   image processing, while Tkinter and TtkBootstrap improve usability with an intuitive interface.
- Future improvements may include adding encryption for additional security, supporting multiple image formats, and implementing adaptive steganography techniques to further 
   enhance robustness. This project demonstrates a practical application of steganography in the field of cybersecurity and secure communication.

## Future Scope
- **Enhanced Security with Encryption :-**  Integrate AES or RSA encryption to encrypt the message before embedding it in the image. This ensures that even if extracted, the 
   hidden data remains unreadable without a decryption key.
- **Support for Multiple Image Formats :-** Extend support to JPEG, BMP, and GIF for better usability. Implement lossless techniques for JPEG, which uses lossy compression.
- **Advanced Steganography Techniques :-** Use Edge-Based or DCT/DWT frequency-domain steganography for improved invisibility.  Apply AI/ML-based approaches to enhance the 
   robustness of hidden data.
- **Higher Data Capacity & Optimization :-**  Optimize encoding efficiency to store more data without noticeable changes in image quality.   Implement dynamic LSB techniques 
   to adapt encoding depth based on the image’s structure.
- **Mobile & Web-Based Implementation :-**  Develop a mobile app using Kivy (Python) or Flutter for secure on-the-go usage.   Create a web-based tool (Flask/Django + 
   JavaScript) for online steganography.
- **Expansion to Audio & Video Steganography :-**  Implement audio steganography to embed messages within sound waves. Develop video steganography, spreading hidden data 
    across multiple frames.
- **Steganalysis Resistance :-**  Apply randomized bit encoding instead of simple LSB to avoid detection. Use anti-detection algorithms to counter steganalysis tools.

## Author
### Ravikant Maurya
**GitHub:** @ravikantmaurya00


