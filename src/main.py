"""Command-line entry point for the fashion-agentic-assistant lesson."""

import argparse
from pathlib import Path

from src.agents.orchestrator import Orchestrator
from src.config import DEFAULT_IMAGE_PATH, DEFAULT_REQUEST
from src.generation.response_builder import ResponseBuilder
from src.utils.image_io import load_image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the agentic fashion lesson.")
    parser.add_argument("--image", type=Path, default=DEFAULT_IMAGE_PATH)
    parser.add_argument("--request", default=DEFAULT_REQUEST)
    parser.add_argument(
        "--show-trace", action="store_true", help="Print each agent decision."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    image = load_image(str(args.image))
    state = Orchestrator().run(image, args.request, image_path=str(args.image))

    print("Fashion Agentic Assistant\n")
    print(ResponseBuilder().build(state))

    if args.show_trace:
        print("\nWorkflow trace")
        for index, event in enumerate(state["trace"], start=1):
            print(f"{index}. {event}")


if __name__ == "__main__":
    main()
