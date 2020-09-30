N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    note = {'до': 'до-о', 'ре': 'ре-э', 'ми': 'ми-и',
            'фа': 'фа-а', 'соль': 'со-оль', 'ля': 'ля-а', 'си': 'си-и'}

    def __init__(self, name, is_long=False):
        self.n = name
        if is_long:
            self.name = Note.note[name]
        else:
            self.name = name
        self.il = is_long

    def play(self):
        print(self.name)

    def __str__(self):
        return self.name

    # def __lshift__(self, other):
    #     return Note(PITCHES[(PITCHES.index(self.n) - other) % N], self.il)
    #
    # def __rshift__(self, other):
    #     return Note(PITCHES[(PITCHES.index(self.n) + other) % N], self.il)
    #
    # def __lt__(self, other):
    #     return PITCHES.index(self.n) < PITCHES.index(other.n)
    #
    # def __gt__(self, other):
    #     return PITCHES.index(self.n) > PITCHES.index(other.n)
    #
    # def __le__(self, other):
    #     return PITCHES.index(self.n) <= PITCHES.index(other.n)
    #
    # def __ge__(self, other):
    #     return PITCHES.index(self.n) >= PITCHES.index(other.n)
    #
    # def __eq__(self, other):
    #     return PITCHES.index(self.n) == PITCHES.index(other.n)
    #
    # def __ne__(self, other):
    #     return PITCHES.index(self.n) != PITCHES.index(other.n)
    #
    # def get_interval(self, other):
    #     return INTERVALS[abs(PITCHES.index(self.n) - PITCHES.index(other.n))]

    def nn(self):
        return str(self.name)


class Melody:
    def __init__(self, arr=''):
        if arr == '':
            arr = []
        self.arr = arr

    def __str__(self):
        res = ''
        for i in self.arr:
            if type(i) != str:
                res += i.nn() + ', '
            else:
                res += i + ', '
        res = res[:-2].capitalize()
        return res

    def append(self, note):
        self.arr.append(note)

    def replace_last(self, note):
        del self.arr[-1]
        self.arr.append(note)

    def remove_last(self):
        del self.arr[-1]

    def clear(self):
        self.arr.clear()

    def new_list(self, arr):
        a = []
        for i in arr:
            b = False
            if len(i) > 2 and i != 'соль':
                i = PITCHES[LONG_PITCHES.index(i)]
                b = True
            a.append(Note(i, b))
        return a

    def __lshift__(self, other):
        arr1 = self.arr.copy()
        for i in range(len(self.arr)):
            a = PITCHES.index(self.arr[i].name) if self.arr[i].name in PITCHES \
                else LONG_PITCHES.index(self.arr[i].name)
            b = PITCHES if arr1[i].name in PITCHES else LONG_PITCHES
            if a - other < 0:
                return Melody(self.arr.copy())
            else:
                arr1[i] = b[abs(a - other) % 7]
        return Melody(self.new_list(arr1))

    def __rshift__(self, other):
        arr1 = self.arr.copy()
        for i in range(len(self.arr)):
            a = PITCHES.index(self.arr[i].name) if self.arr[i].name in PITCHES \
                else LONG_PITCHES.index(self.arr[i].name)
            b = PITCHES if self.arr[i].name in PITCHES else LONG_PITCHES
            if a + other > 6:
                return Melody(self.arr.copy())
            else:
                arr1[i] = b[abs(a + other) % 7]
        return Melody(self.new_list(arr1))

    def __len__(self):
        return len(self.arr)



melody = Melody([Note('ля'), Note('соль'), Note('ми'),  Note('до', True)])
print(melody)
print(Melody() >> 2)
melody_up = melody >> 1
melody_down = melody << 1
melody.replace_last(Note('соль'))
print('>> 1:', melody_up)
print('<< 1:', melody_down)
print(melody)

# class LoudNote(Note):
#     def __init__(self, name, is_long=False):
#         super().__init__(name, is_long)
#
#     def __str__(self):
#         return self.name.upper()
#
#
# class DefaultNote(Note):
#     def __init__(self, name='до', is_long=False):
#         super().__init__(name, is_long)
#
#     def __str__(self):
#         return self.name
#
#
# class NoteWithOctave(Note):
#     def __init__(self, name, octv, is_long=False):
#         super().__init__(name, is_long)
#         self.octv = octv
#
#     def __str__(self):
#         return f'{self.name} ({self.octv})'
#
#
#
# print(Note("соль"))
#
# print(LoudNote(PITCHES[4]))
# print(LoudNote("си", is_long=True))
#
# print(DefaultNote("ми"))
# print(DefaultNote())
# print(DefaultNote(is_long=True))
#
# print(NoteWithOctave("ре", "первая октава"))
# print(NoteWithOctave("ля", "малая октава", is_long=True))
