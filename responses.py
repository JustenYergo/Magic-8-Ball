from console_colors import CColors


class Responses:

    def __init__(self, filename):
        self.filename = filename
        self._responses = {}

    def get_file(self):
        self.filename = str(input(CColors.MENU + "Please enter a file name: " + CColors.ENDC))
        return self.filename

    def read(self):
        self._responses = {}
        with open(self.filename) as f:
            for line in f:
                key, val = line.split(':')
                self._responses[key] = val

    def sort_cat(self):
        for key, value in (sorted(self._responses.items(), key=lambda kv: (kv[1], kv[0]))):
            print(CColors.YELLOW)
            print(key + ':' + value)
            print(CColors.ENDC)

    def sort(self):
        txt_file = open(self.filename, 'r')
        arr = txt_file.read().split('\n')
        length = len(arr) - 1
        unsorted = True
        while unsorted:
            unsorted = False
            for element in range(0, length):
                if arr[element] > arr[element + 1]:
                    hold = arr[element + 1]
                    arr[element + 1] = arr[element]
                    arr[element] = hold
                    unsorted = True
        for elem in arr:
            print(CColors.YELLOW)
            print(elem + '\n')
            print(CColors.ENDC)

    def write(self):
        self.outfileName = str(input(CColors.MENU + "Where do you want the responses to go: " + CColors.ENDC))
        self.outfile = open(self.outfileName, 'w')

        Responses.read(self)

        self.outfile.write(str(self._responses))
        self.outfile.close()

    def get_responses(self):
        return Responses.read(self)
        return Responses.sort(self)

    def print(self, user=''):

        self.print_response = (
            input(CColors.MENU + "Do you want the responses in Alphabetical order? Y/N: " + CColors.ENDC))
        print('\n')
        if self.print_response == ("Y") or self.print_response == ("y"):
            Responses.get_responses(self)
            Responses.sort(self)

        elif self.print_response == ("N") or self.print_response == ("n"):
            Responses.get_responses(self)
            Responses.read(self)
            for key, value in self._responses.items():
                print(CColors.YELLOW)
                print(key + ':' + value)
                print(CColors.ENDC)

    def set_update(self):
        error = True
        while error:
            self.set_update = (input(
                CColors.MENU + "Please input the response you want to add and it category separared by a ':': " + CColors.ENDC))
            self.set_split = self.set_update.split(':')
            if self.set_split[0] != self.set_update:
                error = False
            else:
                error = True

        self.infile = open(self.filename, "r")
        self.infile = open(self.filename, "a")
        self.infile.write('\n' + self.set_update)
        self.infile.close()
