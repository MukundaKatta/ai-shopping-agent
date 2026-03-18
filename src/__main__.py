"""CLI for ai-shopping-agent."""
import sys, json, argparse
from .core import AiShoppingAgent

def main():
    parser = argparse.ArgumentParser(description="AI shopping assistant that finds deals, compares products, and tracks prices")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = AiShoppingAgent()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.search(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"ai-shopping-agent v0.1.0 — AI shopping assistant that finds deals, compares products, and tracks prices")

if __name__ == "__main__":
    main()
