Queue=[None for i in range(5)]
StartPointer=0
TopPointer=0
def Enqueue(value):
  global StartPointer, NullPointer, TopPointer,Queue

  if TopPointer<=len(Queue)-1:
    Queue[TopPointer]=value
    print(f"{value} added to index {TopPointer}")
    print(Queue)
    TopPointer+=1
  else:
    print("Queue is full")
def Dequeue():
  global StartPointer, NullPointer, TopPointer,Queue

  if StartPointer<TopPointer:
    item = Queue[StartPointer]
    Queue[StartPointer] = None  # Clear the slot
    StartPointer += 1
    print ("Removed succesfully")

    if StartPointer==TopPointer:
      StartPointer=0
      TopPointer=0
    return item
  else:
    print("Queue is empty")
    return None


print("--- TEST 1: Dequeue from empty queue ---")
Dequeue()

print("\n--- TEST 2: Enqueue until full ---")
Enqueue("A")
Enqueue("B")
Enqueue("C")
Enqueue("D")
Enqueue("E")

print("\n--- TEST 3: Enqueue to a full queue (Edge Case) ---")
Enqueue("F")

print("\n--- TEST 4: Partial Dequeue ---")
Dequeue()
Dequeue()

print("\n--- TEST 5: Complete Dequeue (Triggers Pointer Reset) ---")
Dequeue()
Dequeue()
Dequeue()

print("\n--- TEST 6: Enqueue after pointer reset (Verifies reuse of array) ---")
Enqueue("X")
Enqueue("Y")