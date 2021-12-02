
import cv2 as cv
import numpy as np
# define the list of boundaries
boundaries = [
	([0, 10, 0], [255, 70, 255]),#red
	([0, 0, 0], [255, 255, 25]),#blue
	([65, 200, 220], [90, 235, 245]),#yellow
	([80, 140, 250], [130, 190, 255]),#orange
    ([110, 150, 25], [175, 210, 75])#green
]
color=['Red','Blue','Yellow','Orange','Green']
img=cv.imread("/Users/mansi/PycharmProjects/pythonProject1/venv/lib/A1.png")

cv.imshow('Image',img)
u=0
font=cv.FONT_HERSHEY_COMPLEX
for (lower,upper) in boundaries:
    blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
    lower=np.array(lower,dtype='uint8')
    upper=np.array(upper,dtype='uint8')
    mask=cv.inRange(blur,lower,upper)
    output=cv.bitwise_and(blur,blur,mask=mask)
    u=u+1

    print("hello")
    gray = cv.cvtColor(np.hstack([output]), cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
    _, threshold = cv.threshold(blur, 90, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    canny = cv.Canny(blur, 125, 175)
    jk = np.hstack([output])
    for cnt in contours:
        rough = cv.approxPolyDP(cnt, 0.01 * cv.arcLength(cnt, True), True)
        x = rough.ravel()[0]-10
        y = rough.ravel()[1]-10

        if len(rough)==3:
            cv.putText(jk,"Triangle",(x,y),font,0.7,(130, 190, 255),1,cv.LINE_AA)
            print("fount triangle!")
            cv.imshow("{} coloured objects".format(color[u-1]), jk)

        if len(rough)==4:
            cv.putText(jk,"Quadrilateral",(x,y),font,0.7,(130, 190, 255),1,cv.LINE_AA)
            cv.imshow("{} coloured objects".format(color[u-1]), jk)

        if len(rough)<=7and len(rough)>4:
            cv.putText(jk,"Pentagon",(x,y),font,0.7,(130, 190, 255),1,cv.LINE_AA)
            cv.imshow("{} coloured objects".format(color[u-1]), jk)

        if len(rough)>7:
            cv.putText(jk,"Circle",(x,y),font,0.7,(130, 190, 255),1,cv.LINE_AA)
            cv.imshow("{} coloured objects".format(color[u-1]), jk)
        jk=jk


        print(len(rough))
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imshow('Orignal Image', img)


    print(' ')



