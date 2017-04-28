from javax.swing import JFrame, JButton

frame = JFrame("Title screen", size=(300, 100), defaultCloseOperation=JFrame.EXIT_ON_CLOSE)

def on_click(event):
    print "You click me"

boton = JButton("click me", actionPerformed=on_click)
frame.add(boton)
frame.visible = True

