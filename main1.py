#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines
"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade #importing libraries

SCREEN_WIDTH = 640 #setting the width, height, and title of the window
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Mouse Example"


class Ball: #Defining a new class 'Ball'
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self): #Draws that instance of the ball
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class MyGame(arcade.Window): #Defining the 'MyGame' class which exists in arcade.Window

    def __init__(self, width, height, title): #Defining the initialization code

        # Call the parent class's init function
        super().__init__(width, height, title)  

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY) #Sets the color of the arcade background to grey

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self): #Whenever the instance is drawn
        """ Called whenever we need to draw the window. """
        arcade.start_render() #Start rendering the scene
        self.ball.draw() #Draw the ball

    def on_mouse_motion(self, x, y, dx, dy): #When the mouse moves, do the following code
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x    #Sets the position of the ball to the position of the mouse
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers): #When a mouse button is pressed, run the following code
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}") #Prints the button that was clicked
        if button == arcade.MOUSE_BUTTON_LEFT: #If the button is the left mouse button, the ball's color is set to black
            self.ball.color = arcade.color.BLACK

    def on_mouse_release(self, x, y, button, modifiers): #When a mouse button is released, run the following code
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT: #If the released button is the left mouse button, set the ball's color to auburn
            self.ball.color = arcade.color.AUBURN


def main(): #defining function main
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #setting a new instance of the MyGame class
    arcade.run() #Running the arcade module


if __name__ == "__main__": #Runs main if the file that is using this code is this file.
    main()