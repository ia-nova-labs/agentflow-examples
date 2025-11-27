"""
AgentFlow Testing Example

This example demonstrates how to test AgentFlow agents without making real LLM API calls.

It shows:
1. Using MockModel to simulate LLM responses
2. Using AgentTestClient for easy testing
3. Assertion helpers for verifying behavior
4. Testing patterns for unit tests

Requirements:
- No LLM required! This runs completely offline.
"""

import sys
import os

# Add parent directory to path
# We need to point to the directory containing agentflow.py, which is the 'agentflow' directory
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(repo_root, "agentflow"))

from agentflow import Agent
from testing import MockModel, AgentTestClient


def example_basic_mocking():
    """Example 1: Basic mocking without real LLM."""
    print("=" * 60)
    print("Example 1: Basic Mocking (No Real LLM)")
    print("=" * 60)
    
    # Create a mock model with predefined responses
    model = MockModel(responses=[
        "Hello! I'm a helpful AI assistant.",
        "Python is a high-level programming language."
    ])
    
    agent = Agent(model=model)
    
    print("\n✅ Running agent with MOCK LLM (no API calls)")
    
    response1 = agent.run("Hello!")
    print(f"Q: Hello!")
    print(f"A: {response1}")
    
    response2 = agent.run("What is Python?")
    print(f"\nQ: What is Python?")
    print(f"A: {response2}")
    
    print(f"\n📊 Mock model was called {model.call_count} times")
    print()


def example_test_client():
    """Example 2: Using AgentTestClient."""
    print("=" * 60)
    print("Example 2: Using AgentTestClient")
    print("=" * 60)
    
    model = MockModel(responses=["Paris is the capital of France."])
    agent = Agent(model=model)
    
    # Wrap agent in test client
    client = AgentTestClient(agent)
    
    print("\n✅ Using TestClient for enhanced testing")
    
    response = client.run("What is the capital of France?")
    print(f"Response: {response}")
    
    # Use assertion helper
    try:
        client.assert_response_contains("Paris")
        print("✅ Assertion passed: Response contains 'Paris'")
    except AssertionError as e:
        print(f"❌ Assertion failed: {e}")
    
    print()


def example_tool_testing():
    """Example 3: Testing agents with tools."""
    print("=" * 60)
    print("Example 3: Testing Tools")
    print("=" * 60)
    
    # Mock responses: first a tool call, then final answer
    model = MockModel(responses=[
        '{"tool": "calculate", "arguments": {"expression": "25 * 4"}}',
        "The result is 100."
    ])
    
    agent = Agent(model=model)
    
    # Register tool
    @agent.tool
    def calculate(expression: str) -> float:
        """Calculate a mathematical expression."""
        return eval(expression)
    
    client = AgentTestClient(agent)
    
    print("\n✅ Testing agent with tools")
    
    response = client.run("What is 25 times 4?")
    print(f"Response: {response}")
    
    # Verify tool was called
    try:
        client.assert_tool_called("calculate")
        print("✅ Tool 'calculate' was called")
    except AssertionError as e:
        print(f"❌ {e}")
    
    # Verify response
    try:
        client.assert_response_contains("100")
        print("✅ Response contains '100'")
    except AssertionError as e:
        print(f"❌ {e}")
    
    print()


def example_unit_test_pattern():
    """Example 4: Unit test pattern."""
    print("=" * 60)
    print("Example 4: Unit Test Pattern")
    print("=" * 60)
    
    print("\n✅ Demonstrating unit test pattern\n")
    
    def test_agent_greets_user():
        """Test that agent greets user properly."""
        model = MockModel(responses=["Hello! How can I help you today?"])
        agent = Agent(model=model)
        client = AgentTestClient(agent)
        
        response = client.run("Hi!")
        
        # Assertions
        assert "Hello" in response or "help" in response
        print("✅ test_agent_greets_user PASSED")
    
    def test_agent_uses_calculator():
        """Test that agent uses calculator tool."""
        model = MockModel(responses=[
            '{"tool": "calc", "arguments": {"expr": "10+20"}}',
            "The answer is 30"
        ])
        agent = Agent(model=model)
        
        @agent.tool
        def calc(expr: str) -> int:
            return eval(expr)
        
        client = AgentTestClient(agent)
        response = client.run("What is 10+20?")
        
        # Assertions
        client.assert_tool_called("calc")
        assert "30" in response
        print("✅ test_agent_uses_calculator PASSED")
    
    # Run tests
    try:
        test_agent_greets_user()
        test_agent_uses_calculator()
        print("\n🎉 All tests passed!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    
    print()


def example_assertion_helpers():
    """Example 5: All assertion helpers."""
    print("=" * 60)
    print("Example 5: Assertion Helpers")
    print("=" * 60)
    
    model = MockModel(responses=[
        '{"tool": "search", "arguments": {"query": "Python"}}',
        "Python is a programming language."
    ])
    
    agent = Agent(model=model)
    
    @agent.tool
    def search(query: str) -> str:
        return f"Results for: {query}"
    
    @agent.tool
    def unused_tool(x: int) -> int:
        return x * 2
    
    client = AgentTestClient(agent)
    response = client.run("Tell me about Python")
    
    print("\n✅ Testing assertion helpers:\n")
    
    # Helper 1: assert_tool_called
    try:
        client.assert_tool_called("search")
        print("✅ assert_tool_called('search') - PASSED")
    except AssertionError:
        print("❌ assert_tool_called('search') - FAILED")
    
    # Helper 2: assert_tool_not_called
    try:
        client.assert_tool_not_called("unused_tool")
        print("✅ assert_tool_not_called('unused_tool') - PASSED")
    except AssertionError:
        print("❌ assert_tool_not_called('unused_tool') - FAILED")
    
    # Helper 3: assert_response_contains
    try:
        client.assert_response_contains("Python")
        print("✅ assert_response_contains('Python') - PASSED")
    except AssertionError:
        print("❌ assert_response_contains('Python') - FAILED")
    
    print()


def main():
    """Run all examples."""
    print("\n" + "🧪 AgentFlow Testing Examples (v0.7)".center(60))
    print()
    
    example_basic_mocking()
    print("-" * 60 + "\n")
    
    example_test_client()
    print("-" * 60 + "\n")
    
    example_tool_testing()
    print("-" * 60 + "\n")
    
    example_unit_test_pattern()
    print("-" * 60 + "\n")
    
    example_assertion_helpers()
    
    print("=" * 60)
    print("✅ All examples completed!")
    print("=" * 60)
    print("\n💡 Key Takeaways:")
    print("   • MockModel = Test without real LLM")
    print("   • AgentTestClient = FastAPI-inspired testing")
    print("   • Assertion helpers = Easy verification")
    print("   • Perfect for unit tests!")
    print("\n🚀 No other agent framework has this!")


if __name__ == "__main__":
    main()
