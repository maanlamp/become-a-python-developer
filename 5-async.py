# threads vs processes
# process is een instantie van een programma, en omvat zijn data en state
# een thread is een soort "subprocess", maar heeft toegang tot alle resources van de parent process

# Parallelism is code tegelijk uitvoeren
# Concurrency is kleine stukjes code doorelkaar heen uitvoeren

# python programma's zijn threads van het python-interpreter-proces, en worden concurrently uitgevoerd.
# er zijn packages om processes te maken ipv threads, om parallelisme mogelijk te maken.

import threading

def fun():
	i = 0
	while i < 10:
		print(i)
		i += 1

# Een thread opzetten is makkelijk
threading.Thread(target=fun).start()

import multiprocessing as mp

# een process spawnen is bijna net zo makkelijk
if __name__ == "__main__":
	mp.Process(target=fun).start() # Alles wordt doorelkaar geprint!