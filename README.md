# qrcode_api
simple api for creating and decoding QR codes

 ## Endpoints
 
 - GET /create/< string > - returns an image with QR code
 - POST /decode - returns a text from QR code - *curl -X POST localhost:5000/decode -F "file=@filepath" -i*