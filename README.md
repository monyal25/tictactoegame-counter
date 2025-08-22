# Tic-Tac-Toe Game State Generator

## Overview

This is a Python-based tic-tac-toe game state generator that systematically explores all possible valid game sequences following proper tic-tac-toe rules. The program generates and counts unique completed game states by simulating games where X always goes first, players alternate turns, and games end when someone wins or the board is full. The primary purpose is to analyze the complete game tree of tic-tac-toe and identify all possible unique end states.

## System Architecture

**Core Design Pattern**: Recursive Game Tree Exploration
The application uses a recursive depth-first search approach to explore all possible game sequences. This design choice allows for systematic enumeration of every valid game path while maintaining game state integrity.

**State Management**: Immutable Board Representation
- Board states are represented as 9-element lists and converted to tuples for hashing
- Uses Python sets to automatically handle duplicate state detection
- Ensures that only unique completed game states are counted

**Game Logic Architecture**: Rule-Based Validation
- Implements proper tic-tac-toe rules with X starting first and alternating turns
- Winner detection uses predefined winning position combinations (rows, columns, diagonals)
- Game termination logic handles both win conditions and tie scenarios

**Data Structures**: Memory-Efficient Storage
- Uses sets for O(1) duplicate detection of completed states
- Tuple-based board representation enables efficient hashing and comparison
- Counters track both unique end states and total games explored for analysis

**Algorithm Choice**: Complete Enumeration vs Optimization
The system prioritizes completeness over performance, exploring every possible valid game sequence to ensure no unique end states are missed. This brute-force approach is suitable given tic-tac-toe's limited state space.

Make sure you have Python 3.9+ installed, then run:

```bash
python main.py
```

### Expected output
number of valid states


## Running tests

A small test suite is included. To run it:

```bash
python test_tictactoe.py
```

## External Dependencies

**Runtime Environment**: Python 3.x
- No external libraries or frameworks required
- Uses only Python standard library features (sets, lists, tuples)
- Self-contained implementation with no network dependencies
