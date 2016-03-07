
"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?

NOTE: suitable for longest/optional matches
"""

def getchar(text,pos):

        if not(pos<0 or pos>=len(words)):
                if words[pos] == ':' or words[pos] == '.':
                        return 'DELIMITER'
                elif words[pos] == '0':
                        return 'ZERO'
                elif words[pos] == '1':
                        return 'ONE'
                elif words[pos] == '2':
                        return 'TWO'
                elif words[pos] == '3':
                        return 'THREE'
                elif words[pos] == '4' or words[pos] == '5':
                        return 'FOUR_OR_FIVE'
                elif words[pos] >= '6' and words[pos] <= '9':
                        return 'SIX_TO_NINE'
                else:
                        return 'OTHER'
        else:
                return None


def scan(text,transition_table,accept_states):
	""" scans `text` while transitions exist in
	'transition_table'. After that, if in a state belonging to
	`accept_states`, it returns the corresponding token, else ERROR.
	"""
	
	# initial state
	pos = 0
	state = 's0'
	# memory for last seen accepting states
	last_seen_token = None
	last_seen_pos = None
	
	
	while True:
		
		c = getchar(text,pos)	# get next char (category)
		
		if c in transition_table[state]:
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
			# remember if current state is accepting but don't return
			if state in accept_states:
				last_seen_token = accept_states[state]
				last_seen_pos = pos
			
		else:	# no transition found

			if last_seen_token is not None:	# if an accepting state already met
				return last_seen_token,last_seen_pos
			
			# else, no accepting state met yet
			return 'ERROR',pos
			
	

# the transition table, as a dictionary
# states that have no outgoing edges need not be in td
td = { 's0':{ 'ZERO':'s1','ONE':'s2', 'TWO':'s3','THREE':'s4','FOUR_OR_FIVE':'s4','SIX_TO_NINE':'s4'},
       's1':{ 'ZERO':'s1','ONE':'s1', 'TWO':'s1','THREE':'s1','FOUR_OR_FIVE':'s1','SIX_TO_NINE':'s1','DELIMITER' : 's5'},
       's2':{ 'ZERO':'s2','ONE':'s2', 'TWO':'s2','THREE':'s2','FOUR_OR_FIVE':'s2','SIX_TO_NINE':'s2','DELIMITER' : 's5' },
       's3':{ 'ZERO':'s3','ONE':'s3', 'TWO':'s3','THREE':'s3', 'DELIMITER' : 's5'},
       's4':{ 'DELIMITER':'s5' },
       's5':{ 'ZERO':'s6','ONE':'s6', 'TWO':'s6','THREE':'s6','FOUR_OR_FIVE' : 's6'},
       's6':{ 'ZERO':'s7','ONE':'s7', 'TWO':'s7','THREE':'s7','FOUR_OR_FIVE':'s7','SIX_TO_NINE':'s7'},
       's7':{ 'DELIMITER':'s8' },
       's8':{ 'ZERO':'s9','ONE':'s9', 'TWO':'s9','THREE':'s9','FOUR_OR_FIVE' : 's9' },
       's9':{ 'ZERO':'s10','ONE':'s10', 'TWO':'s10','THREE':'s10','FOUR_OR_FIVE' : 's10','SIX_TO_NINE':'s10'},
       's10':{},
     } 

# the dictionary of accepting states and their
# corresponding token
ad = { 's7':'TIME_TOKEN',
       's10':'TIME_TOKEN'	
     }


# get a string from input
words = input('give some input>')

# scan text until no more input
while len(words)>0:
	# get next token and position after last char recognized
	tok,pos = scan(words,td,ad)
	if tok=='ERROR':
		print('unrecognized input at pos',pos,'of',words)
		break
	print("token:",tok,"text:",words[:pos])
	# new text for next scan
	words = words[pos:]
	
