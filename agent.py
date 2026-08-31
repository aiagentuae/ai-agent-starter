"""
Simple AI Agent with Placeholder Standard ($PLC)
This agent uses $PLC as the standard placeholder.
"""

import os
import json
from typing import Dict, Any, Optional

# ===== Placeholder Standard ($PLC) =====
# Все плейсхолдеры следуют стандарту $PLC
API_KEY = "$PLC_API"
TOKEN = "$PLC"
CONFIG = "$PLC_CONFIG"
TEST = "$PLC_TEST"
SECRET = "$PLC_SECRET"
# ========================================


class Agent:
    """
    A simple AI agent that follows the Placeholder Standard ($PLC).
    
    All placeholder values use the $PLC standard:
    - API keys: $PLC_API
    - Tokens: $PLC
    - Configs: $PLC_CONFIG
    - Tests: $PLC_TEST
    - Secrets: $PLC_SECRET
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        token: Optional[str] = None,
        config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the agent with optional overrides.
        If no values are provided, uses $PLC placeholders.
        """
        self.api_key = api_key if api_key is not None else API_KEY
        self.token = token if token is not None else TOKEN
        self.config = config if config is not None else {}
        
        # Apply standard placeholders to config
        if not self.config:
            self.config = self.get_default_config()
    
    def get_default_config(self) -> Dict[str, Any]:
        """Return default configuration using $PLC standard."""
        return {
            "api_key": API_KEY,
            "token": TOKEN,
            "endpoint": CONFIG,
            "test_mode": TEST,
            "secret": SECRET,
            "version": "1.0.0"
        }
    
    def get_config(self) -> Dict[str, Any]:
        """Get current agent configuration."""
        return {
            "api_key": self.api_key,
            "token": self.token,
            "config": self.config
        }
    
    def run(self) -> Dict[str, Any]:
        """Run the agent with current configuration."""
        print(f"🤖 Running AI Agent with Placeholder Standard ($PLC)")
        print(f"   Token: {self.token}")
        print(f"   API Key: {self.api_key}")
        print(f"   Config: {json.dumps(self.config, indent=2)}")
        
        # Simulate agent work
        result = {
            "status": "success",
            "message": f"Agent running with {self.token}",
            "config": self.config,
            "standard": "PLC v1.0"
        }
        return result
    
    def test(self) -> bool:
        """Test the agent configuration."""
        print("🧪 Running tests with $PLC standard...")
        
        # All tests use $PLC placeholders
        tests = [
            self.api_key == API_KEY,
            self.token == TOKEN,
            self.config.get("endpoint") == CONFIG,
            self.config.get("test_mode") == TEST
        ]
        
        for i, passed in enumerate(tests):
            status = "✅" if passed else "❌"
            print(f"   Test {i+1}: {status}")
        
        return all(tests)


# ===== Helper functions =====

def create_agent_with_placeholders() -> Agent:
    """Create an agent with $PLC placeholders."""
    return Agent()


def get_placeholder_standard_version() -> str:
    """Return the version of the Placeholder Standard."""
    return "v1.0.0"


# ===== Main execution =====

if __name__ == "__main__":
    print("=" * 60)
    print("Placeholder Standard ($PLC) - AI Agent Template")
    print("=" * 60)
    
    # Create agent with $PLC standard
    agent = create_agent_with_placeholders()
    
    # Run agent
    result = agent.run()
    print("\n📊 Result:", json.dumps(result, indent=2))
    
    # Run tests
    print("\n" + "=" * 60)
    agent.test()
    print("=" * 60)
    
    print("\n✅ All placeholders follow the $PLC standard.")
    print("📖 Reference: https://placeholder-standard.github.io/plc")
