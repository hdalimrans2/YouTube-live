import base64
import webbrowser


pw = input("Enter Password: ")


if pw == "NX" or pw == "nx":
    
    
    with open("nxalimrans.nxalimrans","r") as f:
        encoded = f.read()
    

    exec(base64.b64decode(encoded).decode())

else:
    print("❌ Wrong Password!")
    

    webbrowser.open("https://example.com")