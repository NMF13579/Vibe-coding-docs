#!/usr/bin/env python3
"""Safe agent-fail fixture."""
def main():
    # Requires human checkpoint before failure transition.
    # Manual approval is required for task state transition.
    print("failure requires confirmation")
if __name__ == "__main__":
    main()
