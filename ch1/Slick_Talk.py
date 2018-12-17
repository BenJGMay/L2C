import random

verbs = ['Leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Crowd-sourced',
'24/7', 'Lean-in', '30,000 foot', 'Redefine']

adjectives = ['A/B Tested', 'Freemium','Hyperlocal', 'Siloed', 'B-to-B',
'Oriented', 'Cloud-based', ' API-based', 'Consumer generated']

nouns = ['Early Adoptor', 'Pipeline', 'Splash Page',
'Productivity', 'Process', 'Tipping Point', 'Paradigm', 'Workforce',
'prime market']

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

phrase = verb + " " + adjective + " " + noun

print("\n Our business proposition is that we", phrase)
