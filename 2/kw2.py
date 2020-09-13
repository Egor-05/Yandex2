class Note:
    note = {'до': 'до-о', 'ре': 'ре-э', 'ми': 'ми-и',
            'фа': 'фа-а', 'соль': 'со-оль', 'ля': 'ля-а', 'си': 'си-и'}

    def __init__(self, name, lst=False):
        if lst:
            self.name = Note.note[name]
        else:
            self.name = name

    def play(self):
        print(self.name)

    def __str__(self):
        return self.name


do = Note("до", True)
re = Note("ре", True)
mi = Note("ми", True)
fa = Note("фа", True)
sol = Note("соль", True)
la = Note("ля", True)
si = Note("си", True)
print(do)
print(re)
print(mi)
print(fa)
print(sol)
print(la)
print(si)

