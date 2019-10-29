import face_recognition
import PIL.Image
import PIL.ImageDraw

# Load the image to get the faces 
image = face_recognition.load_image_file("faces.png")

#Get all faces
fLocations = face_recognition.face_locations(image)

