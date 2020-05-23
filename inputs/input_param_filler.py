import yaml

def fill_input(inputs_path, param_list_path):
	with open(inputs_path, 'r') as inputs_file:
		inputs = yaml.safe_load(inputs_file.read())

	with open(param_list_path, 'r') as param_list_file:
		param_list = param_list_file.readlines()

	inputs["param_cards"] = ['param_cards/' + i.strip() for i in param_list]

	with open(inputs_path, 'w') as inputs_file:
		yaml.dump(inputs, inputs_file)

if __name__ == "__main__":
	fill_input('input.yml', 'param_card_list.dat')