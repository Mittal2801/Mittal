class TrafficLight:
    def __init__(self,color):
        self.color = color
        
    def action(self):
        if self.color == 'red':
            print('Stop and wait')
        elif self.color == 'yellow':
            print('Prepare to stop')
        elif self.color == 'green':
            print('Go')
        else:
            print('Stop dancing')
            
y = TrafficLight('yellow')
y.action()