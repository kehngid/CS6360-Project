from Partial_Order.partialOrder import runPartialOrder

# Pick dateset file or import your own
#filename ="./data/testing.csv"
filename = "./data/electricityConsumptionOfEasternChina.csv"
#filename = "./data/FlightDelayStatistics2015.csv"
#filename = "./data/Foreign Visitor Arrivals By Purpose(Jan-Dec 2015).csv"
#filename = "./data/happinessRanking(2015-2016).csv"
#filename = "./data/HollywoodsMostProfitableStories.csv"    # Causing errors
#filename = "./data/MostPopularBaby_Names(NewYork).csv"     
#filename = "./data/SummerOlympic_1896_2008.csv"
#filename = "./data/titanicPassenger.csv"   # Causing errors

#Pick ranking method  
learning_to_rank = False
partial_order = True
hybrid = False
# NOT IMPLEMENTED
if learning_to_rank:
    # run learntorank
    print('Running with learn to rank')
elif partial_order:
    print('Running with partial order')
    # PartialOrder takes two arguments, a filename of a csv 
    # and k, the number of visualizations you want to generate (if you want all, k='all')
    runPartialOrder(filename, k=10)
# NOT IMPLEMENTED
elif hybrid:
    # run hybrid
    print('Running with hybrid')