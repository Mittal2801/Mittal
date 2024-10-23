class TrafficLight:
    
    def __init__(self,color):
        self.color = color
        
    def action(self):
        if self.color == 'red':
            self.next_color = 'yellow'
            print('stop and wait')
        elif self.color == 'yellow':
            self.next_color = 'green'
            print('prepare to stop')
        elif self.color == 'green':
            self.next_color = 'red'
            print('Go')
        else:
            self.next_color = 'orange'
            print('Stop')
            
for list1 in['red','yellow','green']:
    c = TrafficLight(list1)
    print(c.color)
    c.action()
    print(c.next_color)
    print('\n')