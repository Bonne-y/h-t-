from tkinter import *
from tkinter import ttk

# ������ ������� ���������. �������� ��������, ��� � feet � meters �� ���������� ��� � ���������� ����������, � ����� ������ ��� ������ ��������
# *args ��������, ��� ������� ����� ��������� ����� ���������� ����������. ����� ��� �� ������������, ������� ��� �������� �������� ���
def calculate(*args):
    try:
        value = float(feet.get()) # ���������� ������ ��� ������� StringVal
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0) # ���������� ������ ��� ������� StringVal
        
    except ValueError:
        pass

# �������� �������� ���� ����������
root = Tk()
root.title("Feet to Meters")


#������� ������ Frame � ��������� mainframe, ������� ����� ��������� �������� ������ ����������.
#����� ����, ��� �� ������� ���, grid() �������� ��� � ���� ����������. 
#columnconfigure/rowconfigure ������� ��� mainframe ������ ����� �����������
#� �������� ��� ��������� ����� ��� ��������� �������� ����

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


#������ ������ Entry ������ ��������� ���������� �����.

#����� �� ������� ������, ��� ����� ������� ��� ��������.
#��� ������, ������ �������� ����� �������� ����� ������.
#���� ������ � ������ �������, ������� �� ������ ��������, ��������� ��������� ���������� mainframe.
#������������ ������� ���������� � �������� ������� ��������� ��� �������� ���������� ������� �������.

#����� �� ������, ��� ���� ���� ����� ������ ����� ������ ��� 7 ��������.

#����� �� ������� ���������� ���������� feet ��� textvariable ��� Entry. ���� ����� ����������� ���� � ���� ����� feet_entry.
#����� ���� ����������, Tkinter ������������� ������� feet. 
#��� ������� feet ������������ ����������� �� ��������� ��� ����� ���������� -- StringVar()

#Tkinter ������ ����� ���� �� ������ ��������� ������� ������������ ���� �����. 
#�� ��� �������� ������� grid. ��� �������� ���������� � column (1, 2, or 3) � row (also 1, 2, or 3) ����.
#sticky �������� �� ��, �� ����� ������� ����� ������������. W (west) �������� �����, �� ���� ����� ������� ������
#W,E (west-east) �������� � ����� � ������ ������� ������������, �� ���� ������������ ����������.
#� Python ���������� ��������� ��� ����������� �������, ������� �� ������ ������ ������ W ��� (W, E).

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))


#������ ������� ���� ������. 

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))


#�� ������� �� ������ ����� ��������� ������� calculate. ��������� � ��� ��� ��������� �������� �������� � feet � meters,
#�� ��� �� ����� �������� �����-���� ���������, ������� ������������� ������� ������ �������� � meters � �������� � 
#������������ ���� Label ���������.

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ������������� �������, �������� �������� �� ������������
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# ���� ���� ��������� "����������" �������� �������� ���� �� �����
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# ����� �������� ������ ����� � ���� feet_entry
feet_entry.focus()
# ������ ���, ����� ��� ������� �� Enter (���������� ������� Return) ���� ����������� calculate
root.bind("<Return>", calculate)

# ������ ���� ����
root.mainloop()
