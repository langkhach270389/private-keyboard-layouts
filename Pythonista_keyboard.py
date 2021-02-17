import ui
import keyboard

class KeyboardView (ui.View):
	def __init__(self, *args, **kwargs):
		self.label = ui.Label(frame = self.bounds, flex = 'wh', background_color = '#0987b4', alignment = ui.ALIGN_CENTER)
		self.add_subview(self.label)
		self.label.text = 'Private Mode Enabled'
		super().__init__(*args, **kwargs)
	
	def kb_should_insert(self, text):
		before, after = keyboard.get_input_context()
		if before[-1] == 'a':
			keyboard.backspace(1)
			keyboard.insert_text('\u0430')
		elif before[-1] == 'c':
			keyboard.backspace(1)
			keyboard.insert_text('\u0441')
		elif before[-1] == 'e':
			keyboard.backspace(1)
			keyboard.insert_text('\u0435')
		elif before[-1] == 'i':
			keyboard.backspace(1)
			keyboard.insert_text('\u0456')
		elif before[-1] == 'j':
			keyboard.backspace(1)
			keyboard.insert_text('\u0458')
		elif before[-1] == 'o':
			keyboard.backspace(1)
			keyboard.insert_text('\u043e')
		elif before[-1] == 'p':
			keyboard.backspace(1)
			keyboard.insert_text('\u0440')
		elif before[-1] == 'x':
			keyboard.backspace(1)
			keyboard.insert_text('\u0445')
		elif before[-1] == 'y':
			keyboard.backspace(1)
			keyboard.insert_text('\u0443')
			
		elif before[-1] == 'A':
			keyboard.backspace(1)
			keyboard.insert_text('\u0391')
		elif before[-1] == 'B':
			keyboard.backspace(1)
			keyboard.insert_text('\u0392')
		elif before[-1] == 'C':
			keyboard.backspace(1)
			keyboard.insert_text('\u0421')
		elif before[-1] == 'E':
			keyboard.backspace(1)
			keyboard.insert_text('\u0395')
		elif before[-1] == 'H':
			keyboard.backspace(1)
			keyboard.insert_text('\u041d')
		elif before[-1] == 'I':
			keyboard.backspace(1)
			keyboard.insert_text('\u0399')
		elif before[-1] == 'J':
			keyboard.backspace(1)
			keyboard.insert_text('\u0408')
		elif before[-1] == 'K':
			keyboard.backspace(1)
			keyboard.insert_text('\u039a')
		elif before[-1] == 'M':
			keyboard.backspace(1)
			keyboard.insert_text('\u039c')
		elif before[-1] == 'N':
			keyboard.backspace(1)
			keyboard.insert_text('\u039d')
		elif before[-1] == 'O':
			keyboard.backspace(1)
			keyboard.insert_text('\u039f')
		elif before[-1] == 'P':
			keyboard.backspace(1)
			keyboard.insert_text('\u03a1')
		elif before[-1] == 'T':
			keyboard.backspace(1)
			keyboard.insert_text('\u03a4')
		elif before[-1] == 'X':
			keyboard.backspace(1)
			keyboard.insert_text('\u03a7')
		elif before[-1] == 'Y':
			keyboard.backspace(1)
			keyboard.insert_text('\u04ae')
		return text

v = KeyboardView()
keyboard.set_view(v)
