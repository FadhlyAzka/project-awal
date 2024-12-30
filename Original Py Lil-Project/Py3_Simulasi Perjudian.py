import numpy as np
import random as rm

'''Reference: Sheldon Ross. (2010). Introduction to Probability Models Tenth Edition'''
'''The Parameter that you changed:
(main) -> Simulation, Plays
(class Phase) -> total_state, bet
(class Probability_Steps) -> winning
(class Gambler_Ruin) -> state_now
'''
class Phase:
    def __init__(self):
        self.total_state = 11
        self.bet = 5

    def States(self):
        MATRIX_STATES = []
        for i in range(self.total_state):
            pattern = self.bet * i
            MATRIX_STATES.append("$" + str(pattern))
            i += 1
        return MATRIX_STATES

class Steps(Phase):
    def __init__(self):
        super().__init__()

    def Transition_States(self):
        MATRIX_TRANSITION_STATES = []
        for i in range(self.total_state):
            subMATRIX_TRANSITION_STATE = []
            for j in range(self.total_state):
                subMATRIX_TRANSITION_STATE.append("P" + str(i) + str(j))
                j += 1
            MATRIX_TRANSITION_STATES.append(subMATRIX_TRANSITION_STATE)
            i += 1
        return MATRIX_TRANSITION_STATES

class Probability_Steps(Phase):
    def __init__(self):
        super().__init__()
        self.winning = 0.55
        self.losing = 1 - self.winning

    def Matrix_Prob(self):
        N = self.total_state
        p = self.winning
        q = self.losing

        Probabilities_States = []
        for i in range(N):
            subProbabilities_States = []
            for j in range(N):
                subProbabilities_States.append(0)
                j += 1
            Probabilities_States.append(subProbabilities_States)
            i += 1
            
        Broke, Jackpot = "1", "1"
        Probabilities_States[0][0] = Broke
        Probabilities_States[N-1][N-1] = Jackpot
        Probabilities_States = np.array(Probabilities_States, dtype=np.float32)

        for i in range(1, N-1):
            Probabilities_States[i][i+1] = p
            Probabilities_States[i][i-1] = q
        return Probabilities_States
     
class Gambler_Ruin(Probability_Steps):
    def __init__(self):
        super().__init__()
        self.state_now = "$25"
        self.initial_state = next((MStates.index(state) + 1 for state in MStates if self.state_now == state), None)
    
    def Fortune(self):
        N = self.total_state
        p = self.winning
        q = self.losing
        i = self.initial_state
        
        P_i = 0 # Probabilities reaching the Jackpot
        E_i = 0 # Many games until reaching the end, either the Jackpot or bankrupt
        match (p, q):
            case (p, q) if p/q != 0.5:
                P_i = (1 - (q/p)**i)/(1 - (q/p)**N) 
            case (p, q) if p/q == 0.5:
                P_i = i/N

        match (p, q):
            case (p, q) if p > 0.5:
                E_i = (i - N*P_i)/(q - p)
            case (p, q) if p <= 0.5:
                E_i = i(N - i)
        
        return P_i, E_i

class Simulation(Gambler_Ruin):
    def __init__(self):
        super().__init__()
        self.iter = 0

    def Gambling(self, plays):
        iters = self.iter
        Xt = self.state_now
        activityList = [Xt]
        result = []
            
        while iters != plays:
            for state in MStates:
                if Xt == state:
                    break
                else: 
                    pass

            state = Xt
            idx = MStates.index(state)
            pZ = MTrsn_States[idx][idx+1] # State where the prize increases
            nZ = MTrsn_States[idx][idx-1] # State where the prize decreases
            prob_pZ = MProb_States[idx][idx+1]
            prob_nZ = MProb_States[idx][idx-1]
            change = np.random.choice([pZ, nZ], p=[prob_pZ, prob_nZ])
                
            for second_state in MTrsn_States[idx]:
                if change == second_state:
                    break
                else:
                    pass

            second_state = change
            idx2 = MTrsn_States[idx].index(second_state)
            Xt = MStates[idx2]
            activityList.append(MStates[idx2])

            match Xt:
                case Xt if Xt == MStates[-1]:
                    result.append(1)
                    iters = plays - 1
                case "$0":
                    result.append(0)
                    iters = plays - 1
            iters += 1

        return result, activityList 
            

MStates = Phase().States()
MTrsn_States = Steps().Transition_States()
MProb_States = Probability_Steps().Matrix_Prob()
P_i = Gambler_Ruin().Fortune()[0]
E_i = Gambler_Ruin().Fortune()[1]

# Checking the Matrix Transition Probability
I = 0
for i in MProb_States:
    I += np.sum(i)

if int(I) != len(MStates): 	print("There's issue withs probability")
else: 					            print("The Game is Ready to Make you Broke!")

print("-----[REMINDER!]-----")
print("This Gambling Machine has a probability of reaching {} Jackpot of {:.2f}%"
      .format(MStates[-1], P_i*100))
print("The player can only hope they get {} Jackpot at {:.2f} games"
      .format(MStates[-1], E_i))

Simulations = 20 # Basically, many people that plays the gambling machine
Plays = 27       # And each people rolls the gambling machine 
list_activity = []
list_result = []

for iterations in range(Simulations):
		Result_Game, History = Simulation().Gambling(Plays)
		list_result.append(Result_Game)
		list_activity.append(History)
total_broke = list_result.count([0])
total_winning = list_result.count([1])

print("-----[THE OUTCOME]-----")
print(f"Your winning percentage is {(total_winning/Simulations)*100}%")
print(f"Your losing percentage is {(total_broke/Simulations)*100}%")
print(list_activity)
