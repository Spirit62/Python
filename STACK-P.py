
Stack = [None for _ in range(5)]
StartPointer = 0
Boundary = len(Stack)


def push(value):
    global StartPointer, Boundary
    if StartPointer < Boundary:
        Stack[StartPointer] = value
        StartPointer += 1
        print(f"PUSH('{value}') -> Stack: {Stack} | Top: {StartPointer}")
    else:
        print(f"FAILED PUSH('{value}') -> Stack Overflow!")


def pop():
    global StartPointer, Boundary
    if StartPointer > 0:
        StartPointer -= 1
        item = Stack[StartPointer]
        Stack[StartPointer] = None
        print(f"POP() -> Removed '{item}' | Stack: {Stack} | Top: {StartPointer}")
        return item
    else:
        print("FAILED POP() -> Stack Underflow!")
        return None


# ==================== TEST SUITES ====================

print("--- SUITE 1: Base Execution (Your Original Calls) ---")
push(10)
push(20)
pop()
pop()

print("\n--- SUITE 2: Stack Underflow (Popping when empty) ---")
pop()

print("\n--- SUITE 3: Filling the Stack ---")
push(100)
push(200)
push(300)
push(400)
push(500)

print("\n--- SUITE 4: Stack Overflow (Pushing when full) ---")
push(600)

print("\n--- SUITE 5: Interleaved Push & Pop Operations ---")
pop()      
push(999)   

print("\n--- SUITE 6: Draining the Stack Completely ---")
while StartPointer > 0:
    pop()