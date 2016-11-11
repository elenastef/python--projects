import turtle

class Runner:
    #"""class used to instantiate immutable code for assignments """

    student_name = "Elena Stefanova"
    storeRandom = []

    def __init__(self, new_value):
       # """ Add an value to Runner,  the value in a list """

        self.storeRandom.append(new_value)

    
    def run(self):
        #""" returns a tuple : the second value from the storeRandom list """

        aTurtle = turtle.Turtle()
        aTurtle.shape("turtle")
        aTurtle.pensize(5)

        aTuple = (self.storeRandom[1], aTurtle, self.student_name)

        return aTuple
