class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True
    

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player): 
        player_value = getattr(player, self._attr)

        return player_value < self._value
    

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        return any(matcher.test(player) for matcher in self._matchers)
    
    
class QueryBuilder:
    def __init__(self, query=All()):
        self._query_object = query

    def build(self):
        return self._query_object

    def plays_in(self, team):
        return QueryBuilder(And(self._query_object, (PlaysIn(team))))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._query_object, HasAtLeast(value, attr)))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._query_object, HasFewerThan(value, attr)))
    
    def one_of(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))

