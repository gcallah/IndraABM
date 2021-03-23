

class Prop:
    """
    Container for prop attributes.

    Attributes include:
        val - the value of the prop
        question - a question prompt for the user's input for the prop value
        atype - the user's answer type (INT, DBL, BOOL, STR, etc.)
        lowval - the lowest value val can take on
        hival - the highest value val can take on
    """

    def __init__(self, val=None, question=None, atype=None,
                 lowval=None, hival=None):
        self.val = val
        self.question = question
        self.atype = atype
        self.lowval = lowval
        self.hival = hival

    def to_json(self):
        return {"val": self.val,
                "question": self.question,
                "atype": self.atype,
                "lowval": self.lowval,
                "hival": self.hival}

    def __str__(self):
        return str(self.val)
