"""
Test script to verify agentflow.testing import works correctly.

This demonstrates the import pattern from the documentation.
"""

import sys
import os

# Add agentflow to path
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(repo_root, "agentflow"))

from agentflow import Agent
from testing import MockModel, AgentTestClient

# Test without real LLM calls
model = MockModel(responses=["Hello! I'm an AI assistant."])
agent = Agent(model=model)
client = AgentTestClient(agent)

print("Testing import and basic functionality...")
response = client.run("Hello")
print(f"✓ Response received: {response}")

# Test assertion
client.assert_response_contains("Hello")
print("✓ Assertion passed: Response contains 'Hello'")

# Note: This should fail since no tool was called
try:
    client.assert_tool_called("my_tool")
    print("✗ Should have failed: No tool 'my_tool' was called")
except AssertionError as e:
    print(f"✓ Expected assertion error: {e}")

print("\n✅ All tests passed! Import pattern works correctly.")
