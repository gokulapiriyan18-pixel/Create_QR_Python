import qrcode

def create_QR():
    url = input("Enter your website's URL : ").strip()
    if not url:
        print("URL can't be empty")
        return 
    
    file_name = input("Enter the file name (without extension) : ")
    if not file_name:
        file_name = 'QR'
    file_path = f"{file_name}.jpg"


    try:
        qr = qrcode.QRCode(version = None, box_size = 15, border = 5)       #Creating the qr object
        qr.add_data(url)                                                    #add the data to qr object
        qr.make(fit=True)                                                   #Build the QR pattern

        img = qr.make_image(fill_color = 'darkgreen', back_color = '#E6E6FA')     #Convert it into an image
        img.save(file_path)                                                   #Saving the image

        print("QR created successfully!")
        print(f"QR saved as : {file_path}")
    except Exception as e:
        print("Something went wrong : ",e)

create_QR()