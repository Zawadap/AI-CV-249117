from pomegranate import *
# First node

#Independent nodes
work_experience = Node(DiscreteDistribution({
    "short": 0.0770,
    "medium": 0.365,
    "long": 0.558
}), name="work_experience")

training = Node(DiscreteDistribution({
    "no": 0.413,
    "yes": 0.587
}), name="training")

past_experience = Node(DiscreteDistribution({
    "none": 0,
    "little": 1,
    "advanced": 0
}), name="past_experience")

supervision = Node(DiscreteDistribution({
    "no": 0,
    "yes": 1
}), name="supervision")

social_pressure = Node(DiscreteDistribution({
    "no": 0.338,
    "yes": 0.662
}), name="social_pressure")

#dependent nodes
awareness_of_consequences = Node(ConditionalProbabilityTable([
    ["no", "short","none","not aware", 0.1],
    ["no", "short","none","aware", 0.4],
    ["no", "short","none","fully aware", 0.6],
    ["no", "short","little","not aware", 0.05],
    ["no", "short","little","aware", 0.15],
    ["no", "short","little","fully aware", 0.8],
    ["no", "short","advanced","not aware", 0.25],
    ["no", "short","advanced","aware", 0.25],
    ["no", "short","advanced","fully aware", 0.5],
    ["no", "medium","none","not aware", 0.15],
    ["no", "medium","none","aware", 0.25],
    ["no", "medium","none","fully aware", 0.6],
    ["no", "medium","little","not aware", 0.09],
    ["no", "medium","little","aware", 0.18],
    ["no", "medium","little","fully aware",0.73],
    ["no", "medium","advanced","not aware", 0.17],
    ["no", "medium","advanced","aware", 0.33],
    ["no", "medium","advanced","fully aware", 0.5],
    ["no", "long","none","not aware", 0.05],
    ["no", "long","none","aware", 0.10],
    ["no", "long","none","fully aware", 0.85],
    ["no", "long","little","not aware", 0.1],
    ["no", "long","little","aware", 0.6],
    ["no", "long","little","fully aware", 0.3],
    ["no", "long","advanced","not aware", 0.08],
    ["no", "long","advanced","aware", 0.5],
    ["no", "long","advanced","fully aware", 0.42],
    ["yes", "short","none","not aware", 0.20],
    ["yes", "short","none","aware", 0.25],
    ["yes", "short","none","fully aware", 0.55],
    ["yes", "short","little","not aware", 0.17],
    ["yes", "short","little","aware", 0.23],
    ["yes", "short","little","fully aware", 0.5],
    ["yes", "short","advanced","not aware", 0.15],
    ["yes", "short","advanced","aware", 0.15],
    ["yes", "short","advanced","fully aware", 0.7],
    ["yes", "medium","none","not aware", 0.6],
    ["yes", "medium","none","aware", 0.2],
    ["yes", "medium","none","fully aware", 0.2],
    ["yes", "medium","little","not aware", 0.30],
    ["yes", "medium","little","aware", 0.35],
    ["yes", "medium","little","fully aware", 0.35],
    ["yes", "medium","advanced","not aware", 0.2],
    ["yes", "medium","advanced","aware", 0.4],
    ["yes", "medium","advanced","fully aware", 0.4],
    ["yes", "long","none","not aware", 0.23],
    ["yes", "long","none","aware", 0.25],
    ["yes", "long","none","fully aware", 0.52],
    ["yes", "long","little","not aware", 0.13],
    ["yes", "long","little","aware", 0.73],
    ["yes", "long","little","fully aware", 0.14],
    ["yes", "long","advanced","not aware", 0.1],
    ["yes", "long","advanced","aware", 0.4],
    ["yes", "long","advanced","fully aware", 0.5]
], [training.distribution , work_experience.distribution , past_experience.distribution]), name="awareness_of_consequences")

attitude_towards_cwm = Node(ConditionalProbabilityTable([
    ["not aware", "negative", 0],
    ["aware", "negative", 0],
    ["fully aware", "negative", 0],
    ["not aware", "neutral", 0],
    ["aware", "neutral", 0],
    ["fully aware", "neutral", 0],
    ["not aware", "positive", 1],
    ["aware", "positive", 1],
    ["fully aware", "positive", 1]


], [awareness_of_consequences.distribution]), name="attitude_towards_cwm")

#from left social pressure,past experience, attitude, training,supervision
behaviour_towards_cwm = Node(ConditionalProbabilityTable([
    ["no","no","negative","none","no", "negative", 0.1],
    ["no","no","negative","none","no", "positive", 0.9],
    ["no","no","negative","none","yes", "negative", 0.12],
    ["no","no","negative","none","yes", "positive", 0.88],
    ["no","no","negative","little","no", "negative", 0.15],
    ["no","no","negative","little","no", "positive", 0.85],
    ["no","no","negative","little","yes", "negative", 0.15],
    ["no","no","negative","little","yes", "positive", 0.85],
    ["no","no","negative","advanced","no", "negative", 0.20],
    ["no","no","negative","advanced","no", "positive", 0.8],
    ["no","no","negative","advanced","yes", "negative", 0.28],
    ["no","no","negative","advanced","yes", "positive", 0.72],
    ["no","no","neutral","none","no", "negative", 0.3],
    ["no","no","neutral","none","no", "positive", 0.70],
    ["no","no","neutral","none","yes", "negative", 0.27],
    ["no","no","neutral","none","yes", "positive", 0.73],
    ["no","no","neutral","little","no", "negative", 0.24],
    ["no","no","neutral","little","no", "positive", 0.76],
    ["no","no","neutral","little","yes", "negative", 0.25],
    ["no","no","neutral","little","yes", "positive", 0.75],
    ["no","no","neutral","advanced","no", "negative", 0.25],
    ["no","no","neutral","advanced","no", "positive", 0.75],
    ["no","no","neutral","advanced","yes", "negative", 0.25],
    ["no","no","neutral","advanced","yes", "positive", 0.75],
    ["no","no","positive","none","no", "negative", 0.25],
    ["no","no","positive","none","no", "positive", 0.75],
    ["no","no","positive","none","yes", "negative", 0.2],
    ["no","no","positive","none","yes", "positive", 0.8],
    ["no","no","positive","little","no", "negative", 0.2],
    ["no","no","positive","little","no", "positive", 0.8],
    ["no","no","positive","little","yes", "negative", 0.16],
    ["no","no","positive","little","yes", "positive", 0.84],
    ["no","no","positive","advanced","no", "negative", 0.15],
    ["no","no","positive","advanced","no", "positive", 0.85],
    ["no","no","positive","advanced","yes", "negative", 0.1],
    ["no","no","positive","advanced","yes", "positive", 0.90],
    ["no","yes","negative","none","no", "negative", 0.28],
    ["no","yes","negative","none","no", "positive", 0.72],
    ["no","yes","negative","none","yes", "negative", 0.3],
    ["no","yes","negative","none","yes", "positive", 0.70],
    ["no","yes","negative","little","no", "negative", 0.26],
    ["no","yes","negative","little","no", "positive", 0.74],
    ["no","yes","negative","little","yes", "negative", 0.22],
    ["no","yes","negative","little","yes", "positive", 0.78],
    ["no","yes","negative","advanced","no", "negative", 0.22],
    ["no","yes","negative","advanced","no", "positive", 0.78],
    ["no","yes","negative","advanced","yes", "negative", 0.19],
    ["no","yes","negative","advanced","yes", "positive", 0.81],
    ["no","yes","neutral","none","no", "negative", 0.22],
    ["no","yes","neutral","none","no", "positive", 0.78],
    ["no","yes","neutral","none","yes", "negative", 0.29],
    ["no","yes","neutral","none","yes", "positive", 0.71],
    ["no","yes","neutral","little","no", "negative", 0.25],
    ["no","yes","neutral","little","no", "positive", 0.75],
    ["no","yes","neutral","little","yes", "negative", 0.2],
    ["no","yes","neutral","little","yes", "positive", 0.8],
    ["no","yes","neutral","advanced","no", "negative", 0.27],
    ["no","yes","neutral","advanced","no", "positive", 0.73],
    ["no","yes","neutral","advanced","yes", "negative", 0.3],
    ["no","yes","neutral","advanced","yes", "positive", 0.70],
    ["no","yes","positive","none","no", "negative", 0.24],
    ["no","yes","positive","none","no", "positive", 0.76],
    ["no","yes","positive","none","yes", "negative", 0.25],
    ["no","yes","positive","none","yes", "positive", 0.75],
    ["no","yes","positive","little","no", "negative", 0.22],
    ["no","yes","positive","little","no", "positive", 0.78],
    ["no","yes","positive","little","yes", "negative", 0.30],
    ["no","yes","positive","little","yes", "positive", 0.70],
    ["no","yes","positive","advanced","no", "negative", 0.28],
    ["no","yes","positive","advanced","no", "positive", 0.72],
    ["no","yes","positive","advanced","yes", "negative", 0.25],
    ["no","yes","positive","advanced","yes", "positive", 0.75],
    ["yes","no","negative","none","no", "negative", 0.21],
    ["yes","no","negative","none","no", "positive", 0.79],
    ["yes","no","negative","none","yes", "negative", 0.21],
    ["yes","no","negative","none","yes", "positive", 0.79],
    ["yes","no","negative","little","no", "negative", 0.22],
    ["yes","no","negative","little","no", "positive", 0.78],
    ["yes","no","negative","little","yes", "negative", 0.25],
    ["yes","no","negative","little","yes", "positive", 0.75],
    ["yes","no","negative","advanced","no", "negative", 0.24],
    ["yes","no","negative","advanced","no", "positive", 0.76],
    ["yes","no","negative","advanced","yes", "negative", 0.2],
    ["yes","no","negative","advanced","yes", "positive", 0.8],
    ["yes","no","neutral","none","no", "negative", 0.3],
    ["yes","no","neutral","none","no", "positive", 0.7],
    ["yes","no","neutral","none","yes", "negative", 0.26],
    ["yes","no","neutral","none","yes", "positive", 0.74],
    ["yes","no","neutral","little","no", "negative", 0.3],
    ["yes","no","neutral","little","no", "positive", 0.70],
    ["yes","no","neutral","little","yes", "negative", 0.29],
    ["yes","no","neutral","little","yes", "positive", 0.71],
    ["yes","no","neutral","advanced","no", "negative", 0.27],
    ["yes","no","neutral","advanced","no", "positive", 0.73],
    ["yes","no","neutral","advanced","yes", "negative", 0.22],
    ["yes","no","neutral","advanced","yes", "positive", 0.78],
    ["yes","no","positive","none","no", "negative", 0.24],
    ["yes","no","positive","none","no", "positive", 0.76],
    ["yes","no","positive","none","yes", "negative", 0.25],
    ["yes","no","positive","none","yes", "positive", 0.75],
    ["yes","no","positive","little","no", "negative", 0.24],
    ["yes","no","positive","little","no", "positive", 0.76],
    ["yes","no","positive","little","yes", "negative", 0.21],
    ["yes","no","positive","little","yes", "positive", 0.79],
    ["yes","no","positive","advanced","no", "negative", 0.21],
    ["yes","no","positive","advanced","no", "positive", 0.79],
    ["yes","no","positive","advanced","yes", "negative", 0.2],
    ["yes","no","positive","advanced","yes", "positive", 0.8],
    ["yes","yes","negative","none","no", "negative", 0.23],
    ["yes","yes","negative","none","no", "positive", 0.67],
    ["yes","yes","negative","none","yes", "negative", 0.23],
    ["yes","yes","negative","none","yes", "positive", 0.67],
    ["yes","yes","negative","little","no", "negative", 0.34],
    ["yes","yes","negative","little","no", "positive", 0.66],
    ["yes","yes","negative","little","yes", "negative", 0.30],
    ["yes","yes","negative","little","yes", "positive", 0.70],
    ["yes","yes","negative","advanced","no", "negative", 0.26],
    ["yes","yes","negative","advanced","no", "positive", 0.74],
    ["yes","yes","negative","advanced","yes", "negative", 0.24],
    ["yes","yes","negative","advanced","yes", "positive", 0.76],
    ["yes","yes","neutral","none","no", "negative", 0.36],
    ["yes","yes","neutral","none","no", "positive", 0.64],
    ["yes","yes","neutral","none","yes", "negative", 0.33],
    ["yes","yes","neutral","none","yes", "positive", 0.67],
    ["yes","yes","neutral","little","no", "negative", 0.3],
    ["yes","yes","neutral","little","no", "positive", 0.7],
    ["yes","yes","neutral","little","yes", "negative", 0.26],
    ["yes","yes","neutral","little","yes", "positive", 0.74],
    ["yes","yes","neutral","advanced","no", "negative", 0.27],
    ["yes","yes","neutral","advanced","no", "positive", 0.73],
    ["yes","yes","neutral","advanced","yes", "negative", 0.22],
    ["yes","yes","neutral","advanced","yes", "positive",0.78 ],
    ["yes","yes","positive","none","no", "negative", 0.3],
    ["yes","yes","positive","none","no", "positive", 0.70],
    ["yes","yes","positive","none","yes", "negative", 0.40],
    ["yes","yes","positive","none","yes", "positive", 0.60],
    ["yes","yes","positive","little","no", "negative", 0.24],
    ["yes","yes","positive","little","no", "positive", 0.76],
    ["yes","yes","positive","little","yes", "negative", 0.25],
    ["yes","yes","positive","little","yes", "positive", 0.75],
    ["yes","yes","positive","advanced","no", "negative", 0.21],
    ["yes","yes","positive","advanced","no", "positive", 0.79],
    ["yes","yes","positive","advanced","yes", "negative", 0.2],
    ["yes","yes","positive","advanced","yes", "positive", 0.8]
], [supervision.distribution,training.distribution,attitude_towards_cwm.distribution,past_experience.distribution,social_pressure.distribution]), name="behaviour_towards_cwm")

# Create a Bayesian Network and add states
universe = BayesianNetwork()
universe.add_states(work_experience,training,past_experience,supervision,social_pressure, awareness_of_consequences, attitude_towards_cwm, behaviour_towards_cwm)

# Add edges connecting nodes
universe.add_edge(work_experience,awareness_of_consequences)
universe.add_edge(training,awareness_of_consequences)
universe.add_edge(training,behaviour_towards_cwm)
universe.add_edge(supervision,behaviour_towards_cwm)
universe.add_edge(past_experience,awareness_of_consequences)
universe.add_edge(past_experience,behaviour_towards_cwm)
universe.add_edge(social_pressure,behaviour_towards_cwm)
universe.add_edge(awareness_of_consequences,attitude_towards_cwm)
universe.add_edge(attitude_towards_cwm,behaviour_towards_cwm)

# Finalize model
universe.bake()
