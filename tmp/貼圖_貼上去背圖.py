from PIL import Image
 
background = Image.open("d:/18.jpg")
foreground = Image.open("d:/22.png")
 
background.paste(foreground, (0, 0), foreground)
background.show()