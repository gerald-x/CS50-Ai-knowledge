from sys import implementation
from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Base logic for the puzzle: One must be a knight or a knave and not both
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),

    # Sentence can only be true is A is a knave
    Biconditional(And(AKnight, AKnave), AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Base logic for the puzzle: one must be a knight or a knave
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Not(And(AKnave, AKnight)), 
    Not(And(BKnave, BKnight)),


    Implication(AKnave, Not(And(BKnave, AKnave))),
    Implication(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(
        AKnave,
        AKnight,   
    ),
    Not(And(
            AKnave,
            AKnight
    )),
    Or(
        BKnave,
        BKnight
    ),
    Not(And(
        BKnave,
        BKnight
    )),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Or(And(BKnight, AKnave), And(BKnave, AKnight))),
    Implication(BKnave, Not(Or(And(BKnight, AKnave), And(BKnave, AKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(
        AKnave,
        AKnight,
    ),
    Not(And(
        AKnave,
        AKnight
    )),
    Or(
        BKnave,
        BKnight
    ),
    Not(And(BKnave, BKnight)),
    Or(CKnave, CKnight), 
    Not(And(CKnave, CKnight)),

    Biconditional(BKnave, AKnight),
    Implication(CKnave, BKnight),
    Implication(Not(CKnave), BKnave),
    Implication(And(BKnave, Not(CKnave)), AKnight),
    Implication(Not(And(BKnight, Not(CKnave))), AKnave),
    #Implication(AKnight, Implication()),
    #Implication(AKnave, Not(And(BKnave, CKnight))),
    Implication(AKnight, CKnight),
    Implication(Not(AKnight), CKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
