from .ABC import SQLType


class INTEGER(SQLType):
    @property
    def name(self):
        return 'INT'

    def parse(self, value):
        return f'{int(value)}'

    @property
    def default(self):
        return 0

    def cast(self, value):
        return int(value)


class STRING(SQLType):
    def __init__(self, size: int = 255):
        self.size = size

    @property
    def name(self):
        return f'VARCHAR({self.size})'

    def parse(self, value):
        return f"'{str(value)}'"

    @property
    def default(self):
        return ''

    def cast(self, value):
        return str(value)


class BIT(SQLType):
    def __init__(self, size: int = 1):
        self.size = size

    @property
    def name(self):
        return f'BIT({self.size})'

    def parse(self, value):
        return f'{int(value)}'

    @property
    def default(self):
        return 0

    def cast(self, value):
        return int(value)


class FLOAT(SQLType):
    @property
    def name(self):
        return 'FLOAT'

    def parse(self, value):
        return f'{float(value)}'

    @property
    def default(self):
        return 0

    def cast(self, value):
        return float(value)


class DOUBLE(SQLType):
    def __init__(self, size: int = 12, dec: int = 6):
        self.size = size
        self.dec = dec

    @property
    def name(self):
        return f'DOUBLE({self.size},{self.dec})'

    def parse(self, value):
        return f'{float(value)}'

    @property
    def default(self):
        return 0

    def cast(self, value):
        return float(value)


class DECIMAL(SQLType):
    def __init__(self, size: int = 12, dec: int = 6):
        self.size = size
        self.dec = dec

    @property
    def name(self):
        return f'DECIMAL({self.size},{self.dec})'

    def parse(self, value):
        return f'{float(value)}'

    @property
    def default(self):
        return 0

    def cast(self, value):
        return float(value)


class BOOL(SQLType):
    @property
    def name(self):
        return f'BIT(1)'

    def parse(self, value):
        return f'1' if value else f'0'

    @property
    def default(self):
        return False

    def cast(self, value):
        return True if value else False


INT = INTEGER
DEC = DECIMAL
VARCHAR = STRING
CHAR = STRING
