import turtle
import csv



def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map
    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

'''Red for Category 5 >= 157
Orange for Category 4 >= 130
Yellow for Category 3 >= 111
Green for Category 2 >= 96
Blue for Category 1 >= 74
White if not hurricane strength'''
def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()


    # your code to animate Irma here
    xVal, yVal, speed, amt = get_values()



    t.setposition( float(xVal[1]), float(yVal[1]) )
    if (int(speed[1]) >= 157):
        t.color('red')
        t.width(10)
    elif (int(speed[1]) >= 130):
        t.color('orange')
        t.width(8)
    elif (int(speed[1]) >= 111):
        t.color('yellow')
        t.width(6)
    elif (int(speed[1]) >= 96):
        t.color('green')
        t.width(3)
    elif (int(speed[1]) >= 74):
        t.color('blue')
        t.width(2)
    elif(int(speed[1]) <= 73):
        t.color('white')
        t.width(1)


    for i in range(1,amt):
        print(xVal[i],',', yVal[i],',', speed[i])
        print(t.pos())
        if(int(speed[i]) >= 157): t.color('red'), t.width(10)
        elif(int(speed[i]) >= 130): t.color('orange'), t.width(8)
        elif(int(speed[i]) >= 111): t.color('yellow'), t.width(6)
        elif(int(speed[i]) >= 96): t.color('green'), t.width(3)
        elif(int(speed[i]) >= 74): t.color('blue'), t.width(2)
        elif (int(speed[1]) <= 73):
            t.color('white')
            t.width(1)

        t.goto(float(xVal[i]),float(yVal[i]))


    wn.exitonclick()
    return 0



def get_values():
    xVals = []
    yVals = []
    speed = []
    amt = 0
    with open('irma.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            xVals.append(row[3])
            yVals.append(row[2])
            speed.append(row[4])
            amt += 1
    return xVals, yVals, speed, amt





irma()
