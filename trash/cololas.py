import queue

cola=queue.Queue()

cola.put("primero")
cola.put("segundo")
cola.put("tercero")

print(cola.get())

