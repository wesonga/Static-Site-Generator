from textnode import TextNode, TextType

def main():
    # Create a new TextNode object with some dummy values
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    
    # Print the object
    print(node)

# Call the main function to run the code
if __name__ == "__main__":
    main()
