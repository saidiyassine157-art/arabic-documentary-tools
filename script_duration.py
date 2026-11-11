
def estimate_duration(script, words_per_minute=130):
    """Estimate narration duration from a script."""
    if words_per_minute <= 0:
        raise ValueError("Reading speed must be positive.")

    word_count = len(script.split())
    total_seconds = round(word_count / words_per_minute * 60)

    minutes, seconds = divmod(total_seconds, 60)

    return {
        "words": word_count,
        "minutes": minutes,
        "seconds": seconds,
    }


if __name__ == "__main__":
    script = input("Enter your documentary script: ")
    result = estimate_duration(script)

    print(f"Words: {result['words']}")
    print(
        f"Estimated duration: "
        f"{result['minutes']} min {result['seconds']} sec"
    )
