## **Image To Text**
Image-To-Text is the example to convert the image to string with the help of existing library `pytesseract` and In this example I have just used the Flask Framework to create a API `image_to_text`. This API will accept the path of image in JSON structure and return the text.

### Steps to run:
1. Install required libraries using requirements.txt file `pip install -r requirements.txt`
2. Start you server using command `python image_to_text.py` *(This will start your development server)*
3.  Then you can use below CURL: 
```
curl --location --request GET 'http://localhost:3000/image_to_text' \
--header 'Content-Type: application/json' \
--data-raw '{
	"image_path":"https://66.media.tumblr.com/e446af7574605ab09e82cb4f009aee71/tumblr_p5copl828f1ujenmzo1_400.jpg"
}'
```
