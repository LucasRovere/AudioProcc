
import os

command = ''
inputs = []

def main():
	global command, inputs

	OnOpen()
	quit = False

	while command != 'quit':
		GetCmd()
		HandleCmd()

def HandleCmd():
	if command

def GetCmd():
	global command, inputs

	inputString = input("VsGod$ ")

	split = inputString.split('>')
	print(split[0])

	if len(split) == 1:
		command = split[0].strip()
	else:
		command = split[1].strip()
		inputs.clear()
		for s in split[0].split('+'):
			inputs.append(s.strip())

def OnOpen():
	os.system("clear")
		
if __name__ == "__main__":
	main() 
