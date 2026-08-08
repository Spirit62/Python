Queue=[None for i in range(5)]
StartPointer=0
TopPointer=0
Count=0
def Enqueue(value):
  global StartPointer,TopPointer,Queue,Count

  if Count<len(Queue):
    Queue[TopPointer]=value
    print(f"{value} added to index {TopPointer}")
    print(Queue)
    TopPointer+=1
    Count+=1
    if TopPointer==len(Queue):
      TopPointer=0
  else:
    print("Queue is full")
def Dequeue():
  global StartPointer, TopPointer,Queue,Count

  if Count!=0:
    item = Queue[StartPointer]
    Queue[StartPointer] = None  
    StartPointer += 1
    if StartPointer==len(Queue):
      StartPointer=0
    Count-=1
    print ("Removed succesfully")
    return item
  else:
    print("Queue is empty")
    return None


print("=== TEST 1: Underflow Check ===")
Dequeue()

print("\n=== TEST 2: Partial Fill & Partial Empty ===")
# Creates space at indices 0 and 1
Enqueue("A")  # index 0
Enqueue("B")  # index 1
Enqueue("C")  # index 2
Dequeue()      # Removes A (index 0 is now free)
Dequeue()      # Removes B (index 1 is now free)

print("\n=== TEST 3: Wrap-Around Enqueue (Core Circular Test) ===")
# TopPointer will cross index 4 and wrap around to fill indices 0 and 1
Enqueue("D")  # index 3
Enqueue("E")  # index 4 (TopPointer hits boundary and wraps to 0)
Enqueue("F")  # index 0 (WRAPS TO FRONT while 'C' is still at index 2!)
Enqueue("G")  # index 1 

print("\n=== TEST 4: Overflow Check Across Wrapped Boundary ===")
Enqueue("H")  # Queue is full ([F, G, C, D, E])

print("\n=== TEST 5: Wrap-Around Dequeue (Verifies FIFO Order) ===")
# StartPointer must read C(2), D(3), E(4), then wrap to F(0), G(1)
while Count > 0:
    Dequeue()

print("\n=== TEST 6: Empty Check After Wrap ===")
Dequeue()

print("\n=== TEST 7: Reuse Queue From Non-Zero Pointer Position ===")
# Proves the queue works when StartPointer and TopPointer start mid-array
Enqueue("X")  # index 2
Enqueue("Y")  # index 3