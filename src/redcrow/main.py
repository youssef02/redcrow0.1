#!/usr/bin/env python
import sys
from redcrow.crew import RedcrowCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the WebKit Vulnerability Discovery Crew.
    """
    inputs = {
        'target': 'JavaScriptCore in WebKit 2024',
        'focus': 'Memory corruption and browser isolation bypass'
    }
    RedcrowCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'target': 'JavaScriptCore in WebKit 2024',
        'focus': 'Memory corruption and browser isolation bypass'
    }
    try:
        RedcrowCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        RedcrowCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        'target': 'JavaScriptCore in WebKit 2024',
        'focus': 'Memory corruption and browser isolation bypass'
    }
    try:
        RedcrowCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an action (run, train, replay, test).")
        sys.exit(1)

    action = sys.argv[1]

    if action == "run":
        run()
    elif action == "train":
        train()
    elif action == "replay":
        replay()
    elif action == "test":
        test()
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)