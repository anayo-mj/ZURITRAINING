class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age =  age
        self.tracks = tracks
        self.score = score
        
    def change_name(self, change_name):
        self.name = str(self.name)
        #print (self.change_name)
        print ("Student name is ", self.name)
        
    def change_age (self, change_age):
        self.age = int(self.age)
        #print (self.change_age)
        print ("your age is ", self.age)
            
    def add_track(self, add_track):
        self.tracks = add_track
        #print (self.track)
        print ("your track is", self.tracks)
        
    def get_score(self, get_score):
        self.score = float(get_score)
        #return (self.score)
        print("your score is", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(60.0)
