import random


# -------------------- STRATEGY FUNCTIONS --------------------
def strategy(my_history: list[int], opponent_history: list[int], rounds: int | None) -> int:
    """
    Simple Baseline Plus - A straightforward strategy that cooperates initially
    and adapts based on opponent's cooperation rate and recent behavior.

    Parameters:
        my_history (list[int]): List of player's past moves (0=defect, 1=cooperate)
        opponent_history (list[int]): List of opponent's past moves (0=defect, 1=cooperate)
        rounds (int | None): Total number of rounds to be played or None if unknown

    Returns:
        int: 0 for defection or 1 for cooperation
    """
    # First move: always cooperate
    if not opponent_history:
        return 1

    current_round = len(my_history)

    # End-game strategy if rounds are known
    if rounds is not None and current_round >= rounds - 3:
        return 0  # Defect in the final 3 rounds

    # Calculate opponent's cooperation rate
    coop_rate = sum(opponent_history) / len(opponent_history)

    # Check recent behavior (last 3 moves)
    recent_window = min(3, len(opponent_history))
    recent_defections = recent_window - sum(opponent_history[-recent_window:])

    # If opponent has defected in the last two consecutive rounds, defect
    if len(opponent_history) >= 2 and opponent_history[-1] == 0 and opponent_history[-2] == 0:
        return 0

    # If opponent has been mostly cooperative (>70%), cooperate most of the time
    if coop_rate > 0.7:
        # Occasionally defect to avoid being too predictable
        if current_round % 7 == 0:
            return 0
        return 1

    # If opponent has been mostly defecting (<30%), defect
    if coop_rate < 0.3:
        return 0

    # In the middle ground, mirror opponent's last move
    return opponent_history[-1]


def strategy_round_3(opponent_id: int, my_history: dict[int, list[int]], opponents_history: dict[int, list[int]]) -> \
tuple[int, int]:
    """Strategy for Round 3 (returns move + next opponent)."""
    # If this is a new opponent, cooperate initially
    if not my_history[opponent_id]:
        return 1, opponent_id  # Cooperate and continue with the same opponent

    # Calculate cooperation rate for this opponent
    coop_rate = sum(opponents_history[opponent_id]) / len(opponents_history[opponent_id]) if opponents_history[
        opponent_id] else 0.5

    # Find the most cooperative opponent to play with next (who has played fewer than 200 rounds)
    next_opponent = opponent_id  # Default to current opponent
    max_coop_rate = -1

    for opp_id in opponents_history:
        # Skip opponents who have reached their round limit
        if len(my_history[opp_id]) >= 200:
            continue

        # Calculate this opponent's cooperation rate
        if opponents_history[opp_id]:
            opp_coop_rate = sum(opponents_history[opp_id]) / len(opponents_history[opp_id])
            if opp_coop_rate > max_coop_rate:
                max_coop_rate = opp_coop_rate
                next_opponent = opp_id

    # Determine move based on opponent's behavior
    # Similar logic to round 1/2 strategy
    if len(opponents_history[opponent_id]) >= 2 and all(move == 0 for move in opponents_history[opponent_id][-2:]):
        return 0, next_opponent  # Defect against consistently defecting opponents

    if coop_rate > 0.7:
        # Mostly cooperate with cooperative opponents
        if len(my_history[opponent_id]) % 7 == 0:
            return 0, next_opponent  # Occasional defection for unpredictability
        return 1, next_opponent

    if coop_rate < 0.3:
        return 0, next_opponent  # Defect against mostly defecting opponents

    # Mirror opponent's last move in the middle ground
    return opponents_history[opponent_id][-1], next_opponent


# ------------------ TESTING FUNCTIONS ---------------------

def random_opponent_strategy():
    """Returns a random move: 0 (defect) or 1 (cooperate)."""
    return random.choice([0, 1])


def compute_score(my_move, opponent_move):
    """Computes the score based on the game rules."""
    if my_move == 1 and opponent_move == 1:
        return 3, 3  # Both cooperate
    elif my_move == 1 and opponent_move == 0:
        return 0, 5  # Player cooperates, opponent defects
    elif my_move == 0 and opponent_move == 1:
        return 5, 0  # Player defects, opponent cooperates
    else:
        return 1, 1  # Both defect


def test_round_1(rounds: int = 100):
    """Tests the strategy in Round 1 (Fixed Rounds, Random Opponent)."""
    my_history = []
    opponent_history = []
    player_score = 0
    opponent_score = 0

    print("\n--- Testing Round 1 ---")
    for round_num in range(1, rounds + 1):
        my_move = strategy(my_history, opponent_history, rounds)
        opponent_move = random_opponent_strategy()

        my_history.append(my_move)
        opponent_history.append(opponent_move)

        # Update scores
        my_points, opp_points = compute_score(my_move, opponent_move)
        player_score += my_points
        opponent_score += opp_points

    print("\nFinal History (Round 1):")
    print("Player:   ", my_history)
    print("Opponent: ", opponent_history)
    print(f"Final Score - Player: {player_score}, Opponent: {opponent_score}")


def test_round_2():
    """Tests the strategy in Round 2 (Unknown Rounds, Random Opponent)."""
    my_history = []
    opponent_history = []
    player_score = 0
    opponent_score = 0
    rounds_played = random.randint(100, 200)  # Unknown number of rounds (at least 50)

    print("\n--- Testing Round 2 ---")
    for round_num in range(1, rounds_played + 1):
        my_move = strategy(my_history, opponent_history, None)
        opponent_move = random_opponent_strategy()

        my_history.append(my_move)
        opponent_history.append(opponent_move)

        # Update scores
        my_points, opp_points = compute_score(my_move, opponent_move)
        player_score += my_points
        opponent_score += opp_points

    print("\nFinal History (Round 2):")
    print("Player:   ", my_history)
    print("Opponent: ", opponent_history)
    print(f"Final Score - Player: {player_score}, Opponent: {opponent_score}")


def test_round_3():
    """Tests the strategy in Round 3 (1000 rounds, opponent selection, dynamic history)."""
    num_opponents = 6
    rounds_played = 0

    # Initialize empty history dictionaries
    my_history = {i: [] for i in range(1, num_opponents + 1)}
    opponents_history = {i: [] for i in range(1, num_opponents + 1)}
    scores = {i: 0 for i in range(1, num_opponents + 1)}  # Track individual scores

    # Start with a random opponent
    current_opponent = random.choice(list(my_history.keys()))

    print("\n--- Testing Round 3 ---")
    for _ in range(1000):
        if len(my_history[current_opponent]) >= 200:
            # Find an opponent who has played less than 200 rounds
            available_opponents = [i for i in my_history if len(my_history[i]) < 200]
            if not available_opponents:
                break  # Stop if all opponents have reached 200 rounds
            current_opponent = random.choice(available_opponents)

        # Get player's move and next opponent choice
        move, next_opponent = strategy_round_3(current_opponent, my_history, opponents_history)
        opponent_move = random_opponent_strategy()  # Opponent moves randomly

        # Store moves in history
        my_history[current_opponent].append(move)
        opponents_history[current_opponent].append(opponent_move)

        # Update scores
        my_points, opp_points = compute_score(move, opponent_move)
        scores[current_opponent] += my_points

        # Print round result
        rounds_played += 1

        # Update next opponent
        current_opponent = next_opponent if next_opponent in my_history else random.choice(list(my_history.keys()))

    # Print final statistics
    print("\n--- Final Results (Round 3) ---")
    for opponent, history in my_history.items():
        print(f"Opponent {opponent}: Played {len(history)} rounds, Score: {scores[opponent]}")


# This conditional allows the file to be imported or run directly
if __name__ == "__main__":
    test_round_1(100)  # Fixed 100 rounds
    test_round_2()  # Unknown rounds
    test_round_3()  # Adaptive opponent selection