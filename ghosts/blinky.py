from ghosts.ghost import *


class Blinky(Ghost):
    def __init__(self, location, name="blinky"):
        super().__init__(location, name)

    def action(self, state, self_idx):
        blinky = state[self_idx]
        state.pop(self_idx)
        pac, a1, a2, a3 = state
        non_backwards = filter(lambda x: x != tuple([-i for i in blinky['last']]), COMPASS_ROSE)
        options = [((blinky['loc'][0] + dirc[0]) % W, (blinky['loc'][1] + dirc[1]) % H) for dirc in non_backwards]
        valids = list(filter(valid_point, options))
        if len(valids) == 1:
            return tuple([valids[0][i] - blinky['loc'][i] for i in [0,1]])
        scoring = {}
        for option in valids:
            score = -dist(option, pac['loc'])
            scoring[option] = score
        return tuple([max(scoring, key=scoring.get)[i]-blinky['loc'][i] for i in [0, 1]])
