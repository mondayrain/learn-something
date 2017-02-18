# GIF
 
 Stands for Graphics Interchange Format; originally called 87a.                                     3 There is also a 89a version now.

 Is a way to compress images, like JPEG, TIFF, and PNG.
 Specifically, it is a bitmap image format developed by Steve Wilhite.

 Unlike the above, however, it allows you to store more than one image
 in the file itself, allowing for the never-ending loop of images/video clips
 we see today. Basically, it stores multiple images accompanied by control data.

 GIFs only support 8 bits per pixel, or 256 colours per frame.
 
#### File Format

 Start with a fixed-length header ("GIF87a" or "GIF89a").
 Followed by fixed-length Logical Screen Descriptor (size + other characteristics of logical scree    n)

 Then, the file is divided into segments, each introduced by 1 byte containing:
 - An image (Introduced by 0x2C, a comma ',')
 - An extension block (Introduced by 0x21, an exclamation point '!')
 - The trailer (a single byte value 0x3B, a semi-colon ';'), which should be the last byte of the file.

  The full specification can be found [here](https://www.w3.org/Graphics/GIF/spec-gif89a.txt)

