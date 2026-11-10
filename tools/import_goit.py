"""Compatibility entry point for the collection's read-only snapshot verifier."""
import argparse
from verify_collection import verify

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Verify the consolidated collection without fetching or overwriting sources.")
    parser.add_argument("--verify-only", action="store_true",
                        help="Retained for compatibility; verification is always read-only.")
    parser.parse_args()
    verify()
