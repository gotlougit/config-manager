# config-manager
Small script to be used to easily create a .JSON file for configuration of programs

## Usage
Place the ```config.py``` file in your project and then change the values of variables ```fname``` (this variable is the path of the file you will use) and ```default_data```, which is a dictionary full of all of your default values of the variables.

Then, use ```import config``` in your program and just use ```config.loadData()``` to get a dictionary full of the configuration values. Once you do this, you can easily get all of the values you want from the dictionary.

Don't forget to convert all of the values into proper types!

If the file is not created when you load the config file, a default one will be created and a message will also be printed to the console. You can tweak this behaviour yourself in the ```config.py``` file.
