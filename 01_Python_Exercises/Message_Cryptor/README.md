# Message Cryptor (Python Exercise)

**Date:** 2025/20/08  
**Level:** Beginner / Practice  

## Project Description
This is a simple **image-based text encoder and decoder** written in Python using the **PIL (Pillow) library**.  

The project contains two programs:  
1. **Encoder** – Hide a text message inside an image:  
   - You provide the image path and the secret text.  
   - The program encodes the text into the image pixels using a simple formula.  
   - Saves the encoded image to a new file.  

2. **Decoder** – Retrieve the hidden message from the encoded image:  
   - You provide the encoded image path.  
   - The program decodes and prints the hidden message.  

This project is a beginner-friendly implementation of **steganography**.  

## Skills & Concepts Used
- Python basics  
- Lists  
- Loops (`for`)  
- Conditional statements (`if-elif-else`)  
- User input (`input()`)  
- Image manipulation using `Pillow` (`getpixel`, `putpixel`)  
- Simple encoding/decoding algorithms  

## How to Run
### Encoder
1. Make sure you have Python and Pillow installed:
```bash
pip install pillow
