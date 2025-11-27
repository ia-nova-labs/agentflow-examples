"""
Basic AgentFlow Example – Qwen Only Edition
Fully compatible with Hamadi's Ollama setup.
"""

import sys
import os

# Prepare import path
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(repo_root, "agentflow"))

from agentflow import Agent, LLMConnectionError, LLMResponseError


MODEL = "qwen2.5-coder:1.5b"   # ✔️ Your working model


def example_single_interaction():
    print("=" * 60)
    print("Example 1: Single Interaction")
    print("=" * 60)

    agent = Agent(model=MODEL)

    prompt = "Hello! In one sentence, who are you?"
    print(f"\nUser: {prompt}")

    response = agent.run(prompt)
    print(f"Agent: {response}")
    print()


def example_multi_turn_conversation():
    print("=" * 60)
    print("Example 2: Multi-turn Conversation")
    print("=" * 60)

    agent = Agent(model=MODEL)

    prompt1 = "My name is Alice. What's a good programming language to learn?"
    print(f"\nUser: {prompt1}")
    response1 = agent.run(prompt1)
    print(f"Agent: {response1}")

    prompt2 = "Do you remember my name?"
    print(f"\nUser: {prompt2}")
    response2 = agent.run(prompt2)
    print(f"Agent: {response2}")

    print(f"\nConversation history: {len(agent.get_history())} messages")
    print()


def example_error_handling():
    print("=" * 60)
    print("Example 3: Error Handling")
    print("=" * 60)

    # Wrong URL on purpose → expected to fail
    agent = Agent(model=MODEL, base_url="http://localhost:99999")

    try:
        response = agent.run("Hello")
        print(f"Agent: {response}")
    except LLMConnectionError as e:
        print(f"\n❌ Connection Error (expected): {e}")
    except LLMResponseError as e:
        print(f"\n❌ Response Error: {e}")

    print()


def example_clear_history():
    print("=" * 60)
    print("Example 4: Clear History")
    print("=" * 60)

    agent = Agent(model=MODEL)

    print("\nFirst conversation:")
    agent.run("My favorite color is blue.")
    print(f"Messages in history: {len(agent.get_history())}")

    agent.clear_history()
    print("\nAfter clearing history:")
    print(f"Messages in history: {len(agent.get_history())}")

    print("\nNew conversation (agent won't remember blue):")
    response = agent.run("What's my favorite color?")
    print(f"Agent: {response}")
    print()


def main():
    print("\n" + "🤖 AgentFlow Basic Examples (Qwen Edition)".center(60))
    print()

    try:
        example_single_interaction()
        example_multi_turn_conversation()
        example_clear_history()
        example_error_handling()

        print("=" * 60)
        print("✅ All examples completed successfully with Qwen!")
        print("=" * 60)

    except LLMConnectionError as e:
        print(f"\n❌ Could not connect to Ollama: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
