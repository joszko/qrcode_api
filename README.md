# qrcode_api
simple api for encoding and decoding QR codes
created using Flask RESTful 

 ## Endpoints
 
 - GET /create/< string > - returns an image with QR code
 - POST /decode - returns a text from QR code - *curl -X POST localhost:5000/decode -F "file=@filepath" -i*
