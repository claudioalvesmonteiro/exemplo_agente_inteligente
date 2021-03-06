# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class

class Vehicle():

    def __init__(self, x, y, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 3
        self.maxforce = 0.2
        self.bucho = 0

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):

        # A vector pointing from the location to the target
        desired = target - self.position

        # Scale to maximum speed
        desired.setMag(self.maxspeed)
        
        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)

    def bucho_update(self, food_position):

        # A vector pointing from the location to the target
        distancy = food_position - self.position
        
        # verifies if vehicle near food
        if distancy[0] <= 2 and distancy[1] <= 2:
            self.bucho += 1
            return 1
        else:
            return 0

    def display(self):
        # shows n of food acquired
        text('CUME: '+str(self.bucho), 50, 50)
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2
        fill(127)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
