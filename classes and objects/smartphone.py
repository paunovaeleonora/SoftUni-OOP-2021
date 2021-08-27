class Smartphone:

    def __init__(self, memory):
        # TODO: create memory, apps and is_on attributes
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app_name, memory):
        if self.memory - memory <= 0:
            return f"Not enough memory to install {app_name}"
        if not self.is_on:
            return f"Turn on your phone to install {app_name}"

        # TODO: add the new app and decrease the memory
        self.apps.append(app_name)
        self.memory -= memory
        return f"Installing {app_name}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install('Facebook', 60))
smartphone.power()
print(smartphone.install('Facebook', 60))
print(smartphone.install('Messenger', 20))
print(smartphone.install('Instagram', 40))
print(smartphone.status())
