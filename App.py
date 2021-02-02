import Engine
import time

start = time.time()

item = 8
n = 8
engine = Engine.RecommendationEngine(item, n)
engine.run()

end = time.time()

# total time taken
print(f"Time =  {end - start} seconds")

