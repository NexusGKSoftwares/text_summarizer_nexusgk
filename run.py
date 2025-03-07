from main.summarizer import extractive_summary, abstractive_summary

def main():
    text = input("Enter text to summarize:\n")
    method = input("Choose method (abstractive/extractive): ").strip().lower()

    summary = (
        abstractive_summary(text) if method == "abstractive"
        else extractive_summary(text)
    )
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()
