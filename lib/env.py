"""
This file defines an Env, which is a collection
of agents that share a timeline and a Space.
"""
import json
import os
import traceback

from lib.agent import Agent, AgentEncoder
import lib.display_methods as disp
from lib.space import Space
from lib.user import TEST, TestUser
from lib.user import TermUser, TERMINAL, API
from lib.utils import agent_by_name

DEBUG = False
DEBUG2 = False
DEF_USER = "User"

UNLIMITED = 1000

SEP_STR = "==================\n"

X = 0
Y = 1


POP_HIST_HDR = "PopHist for "
POP_SEP = ", "

color_num = 0


class PopHist:
    """
        Data structure to record the fluctuating numbers of various agent
        types.
    """

    def __init__(self, serial_pops=None):
        self.pops = {}
        self.periods = 0
        if serial_pops is not None:
            self.from_json(serial_pops)

    def __str__(self):
        s = POP_HIST_HDR
        for mbr in self.pops:
            s += mbr + POP_SEP
        return s

    def __repr__(self):
        return str(self)  # for now!

    def __iter__(self):
        return iter(self.pops)

    def __getitem__(self, key):
        return self.pops[key]

    def add_period(self):
        self.periods += 1

    def record_pop(self, mbr, count):
        if mbr not in self.pops:
            self.pops[mbr] = []
        self.pops[mbr].append(count)

    def from_json(self, pop_data):
        self.periods = pop_data['periods']
        self.pops = pop_data['pops']

    def to_json(self):
        return {"periods": self.periods, "pops": self.pops}


class Env(Space):
    """
    A collection of entities that share a space and time.
    An env *is* a space and *has* a timeline (PopHist).
    That makes the inheritance work out as we want it to.
    """

    def __init__(self, name, action=None, random_placing=True,
                 serial_obj=None,
                 exclude_member=None,
                 members=None,
                 pop_hist_setup=None,
                 **kwargs):
        super().__init__(name, action=action,
                         random_placing=random_placing, serial_obj=serial_obj,
                         members=members, **kwargs)
        self.type = type(self).__name__
        self.user_type = os.getenv("user_type", TERMINAL)
        self.pop_hist_setup = pop_hist_setup

        # might not need this here since we already create this in model
        if self.user_type == TERMINAL:
            self.user = TermUser(**kwargs)
        elif self.user_type == TEST:
            self.user = TestUser(**kwargs)

        if serial_obj is not None:
            # are we restoring env from json?
            self.restore_env(serial_obj)
        else:
            self.construct_anew(exclude_member)

    def construct_anew(self, exclude_member=None):
        self.pop_hist = PopHist()  # this will record pops across time
        # Make sure varieties are present in the history
        if self.pop_hist_setup is not None:
            self.pop_hist_setup(self.pop_hist)
        else:
            for mbr in self.members:
                self.pop_hist.record_pop(mbr, self.pop_count(mbr))

        self.plot_title = self.name
        # these funcs will be stored as attrs...
        # but only if they're really funcs!
        # cause we're gonna try to call them
        self.exclude_member = exclude_member
        self.womb = []  # for agents waiting to be born

    def from_json(self, serial_obj):
        super().from_json(serial_obj)
        self.pop_hist = PopHist(serial_pops=serial_obj["pop_hist"])
        self.name = serial_obj["name"]

    def to_json(self):
        rep = super().to_json()
        rep["type"] = self.type
        rep["pop_hist"] = self.pop_hist.to_json()
        return rep

    def __repr__(self):
        return json.dumps(self.to_json(), cls=AgentEncoder, indent=4,
                          sort_keys=True)

    def restore_env(self, serial_obj):
        self.from_json(serial_obj)

    def get_periods(self):
        return self.pop_hist.periods

    def add_child(self, group):
        """
        Put a child agent in the womb.
        group: which group will add new agent
        """
        if isinstance(group, str):
            grp_nm = group
        else:
            grp_nm = agent_by_name(group)
        self.womb.append(grp_nm)

    def handle_womb(self):
        """
        The womb just contains group names -- they will be repeated
        as many times as that group needs to add members.
        We name the new members in the `member_creator()` method.
        This should be re-written as dict with:
            {"group_name": #agents_to_create}
        """
        pass

    def handle_pop_hist(self):
        self.pop_hist.add_period()
        for mbr in self.pop_hist.pops:
            if mbr in self.members and self.is_mbr_comp(mbr):
                self.pop_hist.record_pop(mbr, self.pop_count(mbr))
            else:
                self.pop_hist.record_pop(mbr, 0)

    def get_census(self, num_moves, num_switches):
        """
        Gets the census data for all the agents stored
        in the member dictionary.

        Takes in how many agent has moved from one place to another
        and how many agent has switched groups and returns
        a string of these census data.
        """
        census_str = (f"\n{SEP_STR}Census for period {self.get_periods()}\n"
                      + f"{SEP_STR}Group census:\n{SEP_STR}")
        for name in self.members:
            grp = self.members[name]
            census_str += f"  {name} (members: {len(grp)})\n"
        census_str += (f"{SEP_STR} Agent census:\n{SEP_STR}"
                       + f"  Agents who moved: {num_moves}\n"
                       + f"  Agents who switched groups: {num_switches}")
        return census_str

    def has_disp(self):
        if not disp.plt_present:
            self.user.tell("ERROR: Graphing package encounters a problem: "
                           + disp.plt_present_error_message)
            return False
        else:
            return True

    def line_graph(self):
        """
        Show agent populations.
        """
        if self.has_disp():
            try:
                # TODO: improve implementation of the iterator of composite?
                period, data = self.line_data()
                if period is None:
                    self.user.tell("No data to display.")
                    return None

                line_plot = disp.LineGraph(self.plot_title,
                                           data, period,
                                           is_headless=self.headless(),
                                           attrs=self.attrs)
                line_plot.show()
                return line_plot
            except Exception as e:
                self.user.tell("Error when drawing line graph: " + str(e))
        else:
            return None

    def bar_graph(self):
        """
        show the movements of population
        """
        if self.has_disp():
            try:
                # TODO: improve implementation of the iterator of composite?
                periods, data = self.bar_data()
                if periods is None:
                    self.user.tell("No data to display.")
                    return None

                bar_graph = disp.BarGraph(self.plot_title,
                                          data, periods,
                                          is_headless=self.headless())
                bar_graph.show()
                return bar_graph
            except Exception as e:
                self.user.tell("Error when drawing bar graph:" + str(e))
        else:
            return None

    def scatter_plot(self):
        """
        Show agent locations.
        """
        if self.has_disp():
            try:
                scatter_plot = disp.ScatterPlot(
                    self.plot_title,
                    self.get_plot_data(),
                    int(self.width), int(self.height),
                    anim=True, data_func=self.get_plot_data,
                    is_headless=self.headless(),
                    attrs=self.attrs)
                scatter_plot.show()
                return scatter_plot
            except ValueError as e:  # Exception as e:
                self.user.tell("Error when drawing scatter plot: " + str(e))
                traceback.print_stack()
        else:
            return None

    def get_color(self, variety):
        if variety in self.members and self.members[variety].has_color():
            return self.members[variety].get_color()
        else:
            global color_num
            color_num += 1
            return disp.get_color(variety, color_num)

    def get_marker(self, variety):
        if variety in self.members:
            return self.members[variety].get_marker()
        else:
            return None

    def line_data(self):
        period = None
        data = {}
        for var in self.pop_hist.pops:
            if var != self.exclude_member:
                data[var] = {}
                data[var]["data"] = self.pop_hist.pops[var]
                data[var]["color"] = self.get_color(var)
                if not period:
                    period = len(data[var]["data"])
        return period, data

    def bar_data(self):
        """
        This is the data for our scatter plot.
        This code assumes the env holds groups, and the groups
        hold agents with positions.
        This assumption is dangerous, and we should address it.
        """
        period = None
        data = {}
        for var in self.pop_hist.pops:
            if var != self.exclude_member:
                data[var] = {}
                data[var]["data"] = self.pop_hist.pops[var]
                data[var]["color"] = self.get_color(var)
                if not period:
                    period = len(data[var]["data"])
        return period, data

    def get_plot_data(self):
        """
        This is the data for our scatter plot.
        We have to draw it out of groups into a format for our graphs.
        This code assumes the env holds groups, and the groups
        hold agents with positions.
        This assumption is dangerous, and we should address it.
        """
        if not disp.plt_present:
            self.user.tell("ERROR: Graphing package encountered a problem: "
                           + disp.plt_present_error_message)
            return

        data = {}
        for group in self.members:
            data[group] = {}
            # matplotlib wants a list of x coordinates, and a list of y
            # coordinates:
            data[group][X] = []
            data[group][Y] = []
            data[group]["color"] = self.members[group].get_color()
            data[group]["marker"] = self.members[group].get_marker()
            current_group = self.members[group]
            for agent_nm in current_group:
                # temp fix for one of the dangers mentioned above:
                # we might not be at the level of agents!
                if isinstance(current_group[agent_nm], Agent):
                    current_agent_pos = current_group[agent_nm].pos
                    if current_agent_pos is not None:
                        (x, y) = current_agent_pos
                        data[group][X].append(x)
                        data[group][Y].append(y)
        return data

    def headless(self):
        return (self.user_type == API) or (self.user_type == TEST)
