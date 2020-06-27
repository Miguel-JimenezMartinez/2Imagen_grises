import cv2                                #Importando OpenCv

imagen=cv2.imread('poeta_halley.jpg',0)   #El codigo será similar al anterior, pero al añadirle un 0 cambiara a escala de grises        
                                          
#cv2.imshow('Hola soy una imagen en escala de grises', imagen)                                 

print("Hola soy una imagen en escala de grises")

#Comentario hecho desde el server

cv2.waitKey(0)                            

cv2.destroyAllWindows()                   
