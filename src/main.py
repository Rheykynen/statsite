from textnode import TextNode

def main():
    test = TextNode("This is some anchor text", "LINKS", "https://www.boot.dev")
    print(f"TextNode({test})")

if __name__ == "__main__":
    print("Success")
    main()