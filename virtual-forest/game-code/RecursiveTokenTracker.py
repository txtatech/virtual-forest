class RecursiveTokenTracker:
    def __init__(self, document):
        self.document = document
        self.tokens = self.document.split()

    def count_tokens(self, target_token):
        if not self.tokens:
            return 0
        else:
            current_token = self.tokens.pop(0)
            count = self.count_tokens(target_token)
            if current_token == target_token:
                count += 1
            return count

    def explain_token_tracking(self, target_token):
        count = self.count_tokens(target_token)
        print(f"The token '{target_token}' appears {count} times in the document.")

    def main(self):
        print("Welcome to the Recursive Token Tracking Adventure!")
        print("In this interactive experience, we'll use recursion to track tokens in a document.")

        target_token = input("Enter the token you want to track: ")
        self.explain_token_tracking(target_token)

        print("Thank you for exploring the Recursive Token Tracking Adventure!")

if __name__ == "__main__":
    tracker = RecursiveTokenTracker(document="This is a sample document containing tokens. Tokens are tracked using recursion.")
    tracker.main()
