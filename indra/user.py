"""
This file defines User, which represents a user in our system.
"""
import json
import os
import sys

from IPython import embed

from indra.agent import Agent

TERMINAL = "terminal"
TEST = "test"
API = "api"
GUI = "gui"
NOT_IMPL = "Choice not yet implemented."
CANT_ASK_TEST = "Can't ask anything of a scripted test"
DEF_STEPS = 1
DEFAULT_CHOICE = '1'
USER_EXIT = -999

menu_dir = os.getenv("INDRA_HOME", "/home/indrasnet/indras_net") + "/indra"
menu_file = "menu.json"
menu_src = menu_dir + "/" + menu_file


def not_impl(user):
    return user.tell(NOT_IMPL)


def run(user, test_run=False):
    steps = 0
    acts = 0
    if not test_run:
        steps = user.ask("How many periods?")
        if steps is None or steps == "" or steps.isspace():
            steps = DEF_STEPS
        else:
            steps = int(steps)
            user.tell("Steps = " + str(steps))
    else:
        steps = DEF_STEPS

    acts = user.env.runN(periods=steps)
    return acts


def leave(user):
    user.tell("Goodbye, " + user.name + ", I will miss you!")
    return USER_EXIT


def scatter_plot(user, update=False):
    return user.env.scatter_graph()


def line_graph(user, update=False):
    if update:
        user.tell("Updating the line graph.")
    else:
        user.tell("Drawing a line graph.")
    return user.env.line_graph()


def debug(user):
    embed()
    return 0


def tell_debug(msg, end='\n'):
    print("DEBUG: " + msg, file=sys.stderr, end=end)


menu_functions = {
    "run": run,
    "leave": leave,
    "scatter_plot": scatter_plot,
    "line_graph": line_graph,
    "debug": debug,
}


def get_menu_json():
    menu_json = None
    try:
        with open(menu_src, 'r') as f:
            menu_db = json.load(f)
            menu_json = menu_db["menu_database"]
    except FileNotFoundError:
        print("Could not open menu file.")
    return menu_json


class User(Agent):
    """
    A representation of the user in the system.
    """

    def __init__(self, name, env, **kwargs):
        super().__init__(name, **kwargs)
        self.env = env  # this class needs this all the time, we think
        self.menu = get_menu_json()
        self.user_msgs = ''
        self.error_message = {}

    def to_json(self):
        return {"user_msgs": self.user_msgs,
                "name": self.name}

    def from_json(self):
        """
        This must be written!
        """
        pass

    def exclude_menu_item(self, to_exclude):
        """
        This will immediately remove an item from the menu.
        """
        to_del = -1  # just some invalid index!
        for index, item in enumerate(self.menu):
            if item["func"] == to_exclude:
                to_del = index
        if to_del >= 0:
            del self.menu[to_del]

    def tell(self, msg, end='\n'):
        """
        How to tell the user something.
        """
        pass

    def ask(self, msg, default=None):
        """
        How to ask the user something.
        """
        pass

    def tell_err(self, msg, end='\n'):
        self.tell("ERROR: " + msg, end)

    def tell_warn(self, msg, end='\n'):
        self.tell("WARNING: " + msg, end)


class TermUser(User):
    """
    A representation of the user on a terminal.
    """

    def __init__(self, name, env, **kwargs):
        super().__init__(name, env, **kwargs)
        self.menu_title = "Menu of Actions"
        self.stars = "*" * len(self.menu_title)
        self.exclude_menu_item("source")
        self.show_line_graph = False
        self.show_scatter_plot = False

    def tell(self, msg, end='\n'):
        """
        How to tell the user something.
        """
        print(msg, end=end)
        return msg

    def ask(self, msg, default=None):
        """
        How to ask the user something.
        """
        self.tell(msg, end=' ')
        choice = input()
        if not choice:
            return default
        else:
            return choice

    def log(self, msg, end='\n'):
        """
        How to log something for this type of user.
        Our default is going to be the same as tell, for now!
        """
        return self.user.tell(msg, end)

    def is_number(self, c):
        """
        Check if it is a numeric number.
        """
        try:
            int(c)
            return True
        except ValueError:
            return False

    def __call__(self):
        self.tell('\n' + self.stars + '\n' + self.menu_title + '\n'
                  + self.stars)
        for item in self.menu:
            print(str(item["id"]) + ". ", item["question"])
        if self.show_line_graph:
            line_graph(self, update=True)
        if self.show_scatter_plot:
            scatter_plot(self, update=True)
        self.tell("Please choose a number from the menu above:")
        c = input()
        if not c or c.isspace():
            c = DEFAULT_CHOICE
        if self.is_number(c):
            choice = int(c)
            if choice >= 0:
                for item in self.menu:
                    if item["id"] == choice:
                        if item["func"] == "line_graph":
                            self.show_line_graph = True
                            self.show_scatter_plot = False
                        if item["func"] == "scatter_plot":
                            self.show_scatter_plot = True
                            self.show_line_graph = False
                        return menu_functions[item["func"]](self)
            self.tell_err(str(c) + " is an invalid option. "
                          + "Please enter a valid option.")
        else:
            self.tell_err(str(c) + " is an invalid option. "
                          + "Please enter a valid option.")


class TestUser(TermUser):
    """
        This is our test user, who has some characteristics different from the
        terminal user, such as overriding ask() and __call__().
    """

    def ask(self, msg, default=None):
        """
            Can't ask anything of a scripted test!
        """
        return self.tell(CANT_ASK_TEST, end=' ')

    def __call__(self):
        """
            Can't present menu to a scripted test!
        """
        run(self)  # noqa: W391


class APIUser(User):
    """
    This is our web user, who is expected to communicate with a web page
    frontend.
    """

    def __init__(self, name, env, **kwargs):
        super().__init__(name, env, **kwargs)

    def tell(self, msg, end='\n'):
        """
        Tell the user something by showing it on the web page
        The below code is just a possible way to implement this!
        """
        self.user_msgs += (msg + end)

    def ask(self, msg, default=None):
        """
        Ask the user something and present it to the web page
        """
        # Some json thing
        pass

    def __call__(self, menuid=None):
        menu_id = menuid
        menu = get_menu_json()
        if menu_id is None:
            return menu
        else:
            return menu_functions[menu[menu_id]["func"]](self)

    def to_json(self):
        return {"user_msgs": self.user_msgs,
                "name": self.name}
