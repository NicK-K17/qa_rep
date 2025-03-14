class Group:
    pupils = True
    school_name = 42
    director = 'Marivanna'

    def study(self):
        print('st down and read')

    def move(self):
        pass

    def __init__(self, title, pupils_count, group_leader):
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader


class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = 'left'

    def move(self):
        print('run fast')

    def __init__(self, title, pupils_count, group_leader, class_room):
        super().__init__(title, pupils_count, group_leader)
        self.class_room = class_room



class HighSchool(Group):
    max_age = 18
    min_age = 14

    def move(self):
        print('go slowly')


first_a = PrimaryGroup('1A', 18, 'MF', 55)
eleven_a = HighSchool('f1', 22, 'MD')


print(first_a.class_room)