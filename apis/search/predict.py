import numpy as np
import tensorflow as tf
import cv2

model = tf.keras.models.load_model("apis/search/custom_model/21classes.h5")
# class_names = ["Mudshake", "Limoncello", "Campari", "Jose Cuervo", "Bacardi Carta Blanca", "Gilbeys Vodka", "Smirnoff", "Blue Curacao", "Jack Daniel's", "Peach Tree", "Vermouth", "Kahlua", 'Tanqueray', 'Baileys', 'Malibu Coconut Rum', '818 Tequila', 'Bombay Sapphire', "Gordon's Gin", 'Johnnie Walker', 'Amaretto', 'Absolute']

def predict_liquor(path):
    img = cv2.imdecode(np.fromfile(path, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_LINEAR)
    img = np.array(img)/255.0
    img = img.reshape(1,224,224,3)
    
    prediction = model.predict(img)
    print(np.max(prediction))
    if np.max(prediction) < 0.8:
        return -1
    else:
        return np.argmax(prediction)+1


